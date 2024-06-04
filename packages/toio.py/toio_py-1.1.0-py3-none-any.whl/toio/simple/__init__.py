# -*- coding: utf-8 -*-
# ************************************************************
#
#     toio/simple/__init__.py
#
#     Copyright 2023 Sony Interactive Entertainment Inc.
#
# ************************************************************

from __future__ import annotations

import asyncio
import inspect
import math
import threading
import time
from enum import Enum
from logging import NOTSET, NullHandler, StreamHandler, getLogger

from typing_extensions import ClassVar, Optional, Tuple, Type

from ..coordinate_systems import (
    LocalCoordinateSystem,
    VisualProgrammingCoordinateSystem,
)
from ..cube import ToioCoreCube
from ..cube.api.base_class import CubeCharacteristic, NotificationHandlerTypes
from ..cube.api.button import Button, ButtonInformation
from ..cube.api.configuration import (
    MagneticSensorCondition,
    MagneticSensorFunction,
    PostureAngleDetectionCondition,
    PostureAngleDetectionType,
)
from ..cube.api.id_information import (
    IdInformation,
    PositionId,
    PositionIdMissed,
    StandardId,
    StandardIdMissed,
)
from ..cube.api.indicator import Color, IndicatorParam
from ..cube.api.motor import (
    Motor,
    MotorResponseCode,
    MovementType,
    ResponseMotorControlMultipleTargets,
    ResponseMotorControlTarget,
    RotationOption,
    Speed,
    TargetPosition,
)
from ..cube.api.sensor import (
    MagneticSensorData,
    MotionDetectionData,
    PostureAngleEulerData,
    PostureDataType,
    Sensor,
)
from ..cube.api.sound import MidiNote, Note
from ..position import (
    STAY_CURRENT,
    CubeLocation,
    MatRect,
    Point,
    RelativeCubeLocation,
    ToioMat,
)
from ..scanner import BLEScanner
from ..standard_id import StandardIdCard
from ..utility import clip
from .async_simple import AsyncSimpleCube, Direction

logger = getLogger(__name__)
logger.setLevel(NOTSET)
handler = NullHandler()
handler.setLevel(NOTSET)
logger.addHandler(handler)


class SimpleCube_v1_0:
    """
    Access to toio core cube by easier method
    Functions that like blocks in visual programming
    """

    DEFAULT_ROTATION_OPTION: ClassVar[RotationOption] = RotationOption.AbsoluteOptimal
    DEFAULT_MOVEMENT_TYPE: ClassVar[MovementType] = MovementType.Curve
    DEFAULT_TIMEOUT: ClassVar[int] = 10
    DEFAULT_ONE_STEP: ClassVar[int] = 1
    CELL_SIZE: ClassVar[float] = 43.43
    MONITORING_CYCLE: ClassVar[float] = 0.01
    _T_LOCK = threading.Lock()
    _LOCK: Optional[asyncio.Lock] = None

    @staticmethod
    def ensure_event_loop() -> asyncio.AbstractEventLoop:
        try:
            return asyncio.get_running_loop()
        except RuntimeError:
            event_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(event_loop)
            return event_loop

    @classmethod
    async def search(cls, name: Optional[str] = None, timeout: int = 5) -> ToioCoreCube:
        if name is not None:
            logger.info(f"search {name} in my registered devices")
            devices = await BLEScanner.scan_registered_cubes_with_id(cube_id={name})
            if len(devices) == 0:
                logger.info(f"search {name}")
                devices = await BLEScanner.scan_with_id(cube_id={name})
        else:
            logger.info("scan registered devices")
            devices = await BLEScanner.scan_registered_cubes(1, timeout=timeout)
            if len(devices) == 0:
                logger.info("scan all devices")
                devices = await BLEScanner.scan(1, timeout=timeout)
                logger.info("scan complete")
                logger.debug(devices)
        if len(devices) != 1:
            raise ValueError
        return ToioCoreCube(interface=devices[0].interface, name=devices[0].name)

    async def _scan_and_connect(
        self, name: Optional[str], timeout: int
    ) -> ToioCoreCube:
        assert SimpleCube_v1_0._LOCK is not None
        print(self._dbg_name, "try to get async lock")
        async with SimpleCube_v1_0._LOCK:
            print(self._dbg_name, "got async lock")
            print(self._dbg_name, "scan_and_connect")
            logger.debug("scanning")
            cube: ToioCoreCube = await self.search(name=name, timeout=timeout)
            logger.debug("connecting")
            await cube.connect()
            print(self._dbg_name, "connected", cube.name)
            logger.debug(f"connected ({cube.name})")
            print(self._dbg_name, "release async lock")
        return cube

    def __init__(
        self,
        name: Optional[str] = None,
        timeout: int = 5,
        coordinate_system_class: Type[
            LocalCoordinateSystem
        ] = VisualProgrammingCoordinateSystem,
        log_level: int = NOTSET,
        dbg_name: str = "",
    ) -> None:
        self._event_loop = self.ensure_event_loop()
        self._dbg_name = dbg_name
        print(self._dbg_name, "check lock")
        with SimpleCube_v1_0._T_LOCK:
            if SimpleCube_v1_0._LOCK is None:
                print(self._dbg_name, "create async lock")
                SimpleCube_v1_0._LOCK = asyncio.Lock()
            else:
                print(self._dbg_name, "async lock is already created")

        print(self._dbg_name, "__init__ start")
        self._native_location: Optional[CubeLocation] = None
        self._location: Optional[RelativeCubeLocation] = None
        self._standard_id: Optional[StandardId] = None
        self._on_position_id: bool = False
        self._on_standard_id: bool = False
        self._mat: Optional[MatRect] = None
        self._arrived: bool = False
        self._coordinate_system_class: Type[LocalCoordinateSystem] = (
            coordinate_system_class
        )

        if log_level is not NOTSET:
            logger.setLevel(log_level)
            log_handler = StreamHandler()
            log_handler.setLevel(log_level)
            logger.addHandler(log_handler)

        self._motion: Optional[MotionDetectionData] = None
        self._cube_angle: Optional[PostureAngleEulerData] = None
        self._magnet: Optional[MagneticSensorData] = None

        with SimpleCube._T_LOCK:
            self._cube = self._event_loop.run_until_complete(
                self._scan_and_connect(name, timeout)
            )
            print(self._dbg_name, "release thread lock")

        self._button: Optional[ButtonInformation] = self._event_loop.run_until_complete(
            self._cube.api.button.read()
        )
        self._set_sensor_configurations()
        self._request_initial_information()

        handlers: Tuple[Tuple[CubeCharacteristic, NotificationHandlerTypes], ...] = (
            (self._cube.api.id_information, self._id_notification_handler),
            (self._cube.api.motor, self._motor_notification_handler),
            (self._cube.api.sensor, self._motion_sensor_notification_handler),
            (self._cube.api.button, self._button_notification_handler),
        )
        for characteristic, notification_handler in handlers:
            self._event_loop.run_until_complete(
                characteristic.register_notification_handler(notification_handler)
            )
        self._wait_to_obtain_initial_information()

    def _set_sensor_configurations(self):
        self._event_loop.run_until_complete(
            self._cube.api.configuration.set_magnetic_sensor(
                function_type=MagneticSensorFunction.MagnetState,
                # function_type=MagneticSensorFunction.MagneticForce,
                interval_ms=60,
                condition=MagneticSensorCondition.ChangeDetection,
            )
        )
        self._event_loop.run_until_complete(
            self._cube.api.configuration.set_posture_angle_detection(
                detection_type=PostureAngleDetectionType.Euler,
                interval_ms=50,
                condition=PostureAngleDetectionCondition.ChangeDetection,
            )
        )

    def _request_initial_information(self):
        self._event_loop.run_until_complete(
            self._cube.api.sensor.request_motion_information()
        )
        self._event_loop.run_until_complete(
            self._cube.api.sensor.request_posture_angle_information(
                PostureDataType.Euler
            )
        )
        self._event_loop.run_until_complete(
            self._cube.api.sensor.request_magnetic_sensor_information()
        )

    def _wait_to_obtain_initial_information(self):
        while not self._motion or not self._cube_angle or not self._magnet:
            self._request_initial_information()
            self._event_loop.run_until_complete(asyncio.sleep(0.1))

    def __del__(self):
        self.disconnect()

    def __enter__(self):
        return self

    def __exit__(self, _exc_type, _exc_value, _traceback):
        self.disconnect()

    def disconnect(self):
        logger.debug("disconnecting")
        self._event_loop.run_until_complete(self._cube.disconnect())
        logger.debug("disconnected")

    def sleep(self, sleep_second: float):
        start = time.time()
        while True:
            self._event_loop.run_until_complete(asyncio.sleep(0))
            time.sleep(0)
            if (time.time() - start) >= sleep_second:
                break

    def _id_notification_handler(self, payload: bytearray) -> None:
        id_info = IdInformation.is_my_data(payload)
        logger.debug(id_info)
        if isinstance(id_info, PositionId):
            self._native_location = id_info.center
            for mat in ToioMat.mats:
                if self._native_location.point in mat:
                    if mat != self._mat:
                        logger.debug(str(mat))
                        self._mat = mat
                        self._location = RelativeCubeLocation.new()
                        coordinate_system = self._coordinate_system_class(
                            origin=mat.center()
                        )
                        self._location.change_coordinate_system(coordinate_system)
                    else:
                        assert self._location is not None
                    self._location.from_absolute_location(self._native_location)
                    break
            assert self._location is not None
            self._on_position_id = True
        elif isinstance(id_info, StandardId):
            coordinate_system = self._coordinate_system_class()
            id_info.angle = coordinate_system.from_native_angle(id_info.angle)
            self._standard_id = id_info
            self._on_standard_id = True
        elif isinstance(id_info, PositionIdMissed):
            self._location = None
            self._mat = None
            self._native_location = None
            self._on_position_id = False
        elif isinstance(id_info, StandardIdMissed):
            self._standard_id = None
            self._on_standard_id = False

    def _motor_notification_handler(self, payload: bytearray) -> None:
        motor_response = Motor.is_my_data(payload)
        logger.debug(motor_response)
        if isinstance(
            motor_response,
            (ResponseMotorControlTarget, ResponseMotorControlMultipleTargets),
        ):
            if (
                motor_response.response_code == MotorResponseCode.SUCCESS
                or motor_response.response_code
                == MotorResponseCode.SUCCESS_WITH_OVERWRITE
            ):
                self._arrived = True

    def _motion_sensor_notification_handler(self, payload: bytearray) -> None:
        sensor_info = Sensor.is_my_data(payload)
        logger.debug(sensor_info)
        if isinstance(sensor_info, MotionDetectionData):
            self._motion = sensor_info
        elif isinstance(sensor_info, PostureAngleEulerData):
            self._cube_angle = sensor_info
        elif isinstance(sensor_info, MagneticSensorData):
            self._magnet = sensor_info

    def _button_notification_handler(self, payload: bytearray) -> None:
        button_info = Button.is_my_data(payload)
        logger.debug(button_info)
        if isinstance(button_info, ButtonInformation):
            self._button = button_info

    def move(self, speed: int, duration: float, wait_to_complete: bool = True) -> None:
        duration = max(duration, 0)
        duration_ms = int(duration * 1000)
        self._event_loop.run_until_complete(
            self._cube.api.motor.motor_control(speed, speed, duration_ms)
        )
        if wait_to_complete:
            self.sleep(duration)

    def spin(self, speed: int, duration: float, wait_to_complete: bool = True) -> None:
        """
        speed: (negative value: anticlockwise)
        """
        duration = max(duration, 0)
        duration_ms = int(duration * 1000)
        self._event_loop.run_until_complete(
            self._cube.api.motor.motor_control(speed, -speed, duration_ms)
        )
        if wait_to_complete:
            self.sleep(duration)

    def run_motor(
        self,
        left_speed: int,
        right_speed: int,
        duration: float,
        wait_to_complete: bool = True,
    ) -> None:
        duration = max(duration, 0)
        duration_ms = int(duration * 1000)
        self._event_loop.run_until_complete(
            self._cube.api.motor.motor_control(left_speed, right_speed, duration_ms)
        )
        if wait_to_complete:
            self.sleep(duration)

    def stop_motor(self) -> None:
        self._event_loop.run_until_complete(self._cube.api.motor.motor_control(0, 0))

    def move_steps(self, direction: Direction, speed: int, step: int) -> bool:
        if not self._on_position_id:
            return False
        assert self._native_location is not None
        if direction == Direction.Forward:
            distance = self._step_to_point(step)
        elif direction == Direction.Backward:
            distance = -1 * self._step_to_point(step)
        else:
            return False
        native_location = self._native_location
        target_x = native_location.point.x + round(
            distance * math.cos(math.radians(native_location.angle))
        )
        target_y = native_location.point.y + round(
            distance * math.sin(math.radians(native_location.angle))
        )
        target_location = CubeLocation(
            point=Point(x=target_x, y=target_y), angle=native_location.angle
        )
        boundary_location = native_location.get_boundary_point(target_location)
        target_param = TargetPosition(
            cube_location=boundary_location,
            rotation_option=RotationOption.WithoutRotation,
        )
        speed_param = Speed(
            max=clip(abs(speed), 0, 255),
        )
        return self._wait_arrival(self._move_to_target(speed_param, target_param))

    def _step_to_point(self, step: int) -> int:
        return step * self.DEFAULT_ONE_STEP

    def _move_to_target(self, speed: Speed, target: TargetPosition) -> float:
        self._arrived = False
        executed_time = time.time()
        self._event_loop.run_until_complete(
            self._cube.api.motor.motor_control_target(
                timeout=self.DEFAULT_TIMEOUT,
                movement_type=self.DEFAULT_MOVEMENT_TYPE,
                speed=speed,
                target=target,
            )
        )
        return executed_time

    def _wait_arrival(self, executed_time: float):
        while not self._arrived:
            if not self._on_position_id:
                logger.debug("Position ID Missed")
                return False
            elif time.time() - executed_time < self.DEFAULT_TIMEOUT:
                self._event_loop.run_until_complete(
                    asyncio.sleep(self.MONITORING_CYCLE)
                )
            else:
                break
        return self._arrived

    def turn(self, speed: int, degree: int) -> bool:
        if not self._on_position_id:
            return False
        assert self._location is not None
        if degree >= 0:
            rotation = RotationOption.RelativePositive
        else:
            rotation = RotationOption.RelativeNegative
            degree = -1 * degree
        current_location = CubeLocation(
            point=Point(x=STAY_CURRENT, y=STAY_CURRENT), angle=degree
        )
        target_param = TargetPosition(
            cube_location=current_location,
            rotation_option=rotation,
        )
        speed_param = Speed(
            max=clip(abs(speed), 0, 255),
        )
        return self._wait_arrival(self._move_to_target(speed_param, target_param))

    def move_to(self, speed: int, x: int, y: int) -> bool:
        if not self._on_position_id:
            return False
        assert self._native_location is not None
        assert self._location is not None
        relative_location = self._location
        relative_location.relative_location = CubeLocation(
            point=Point(x=x, y=y), angle=0
        )
        boundary_location = self._native_location.get_boundary_point(
            relative_location.to_absolute_location()
        )
        target_param = TargetPosition(
            cube_location=boundary_location,
            rotation_option=RotationOption.WithoutRotation,
        )
        speed_param = Speed(
            max=clip(abs(speed), 0, 255),
        )
        return self._wait_arrival(self._move_to_target(speed_param, target_param))

    def set_orientation(self, speed: int, degree: int) -> bool:
        if not self._on_position_id:
            return False
        assert self._native_location is not None
        if degree >= 0:
            rotation = RotationOption.AbsolutePositive
        else:
            rotation = RotationOption.AbsoluteNegative
            degree = -1 * degree
        coordinate_system = self._coordinate_system_class()
        degree = round(coordinate_system.to_native_angle(degree))
        current_location = CubeLocation(
            point=Point(x=STAY_CURRENT, y=STAY_CURRENT), angle=degree
        )
        target_param = TargetPosition(
            cube_location=current_location,
            rotation_option=rotation,
        )
        speed_param = Speed(
            max=clip(abs(speed), 0, 255),
        )
        return self._wait_arrival(self._move_to_target(speed_param, target_param))

    def move_to_the_grid_cell(self, speed: int, cell_x: int, cell_y: int) -> bool:
        if not self._on_position_id:
            return False
        cell_point = self._cell_to_point(cell_x, cell_y)
        return self.move_to(speed, cell_point.x, cell_point.y)

    def get_current_position(self) -> Optional[Tuple[int, int]]:
        if self._location:
            return (
                self._location.relative_location.point.x,
                self._location.relative_location.point.y,
            )
        else:
            return None

    def get_x(self) -> Optional[int]:
        if self._location:
            return self._location.relative_location.point.x
        else:
            return None

    def get_y(self) -> Optional[int]:
        if self._location:
            return self._location.relative_location.point.y
        else:
            return None

    def get_orientation(self) -> Optional[int]:
        if self._location:
            return self._location.relative_location.angle
        else:
            return None

    def get_grid(self) -> Optional[Tuple[int, int]]:
        if not self._on_position_id:
            return None
        assert self._location is not None
        (cell_x, cell_y) = self._point_to_cell(self._location.relative_location.point)
        return cell_x, cell_y

    def get_grid_x(self) -> Optional[int]:
        if not self._on_position_id:
            return None
        assert self._location is not None
        (cell_x, _) = self._point_to_cell(self._location.relative_location.point)
        return cell_x

    def get_grid_y(self) -> Optional[int]:
        if not self._on_position_id:
            return None
        assert self._location is not None
        (_, cell_y) = self._point_to_cell(self._location.relative_location.point)
        return cell_y

    def is_on_the_gird_cell(self, cell_x: int, cell_y: int) -> bool:
        if not self._on_position_id:
            return False
        assert self._location is not None
        (current_cell_x, current_cell_y) = self._point_to_cell(
            self._location.relative_location.point
        )
        return (cell_x, cell_y) == (current_cell_x, current_cell_y)

    def _cell_to_point(self, cell_x: int, cell_y: int) -> Point:
        return Point(x=round(self.CELL_SIZE * cell_x), y=round(self.CELL_SIZE * cell_y))

    def _point_to_cell(self, relative_point: Point) -> Tuple[int, int]:
        cell = relative_point / self.CELL_SIZE
        return cell.x, cell.y

    def is_touched(self, item: StandardIdCard) -> bool:
        if not self._standard_id:
            return False
        try:
            current_item = StandardIdCard(self._standard_id.value)
        except ValueError:
            logger.debug(
                f"ValueError: Wrong Standard ID is detected:{self._standard_id.value}"
            )
            return False
        return current_item == item

    def get_touched_card(self) -> Optional[int]:
        if not self._standard_id:
            return None
        try:
            current_item: Enum = StandardIdCard(self._standard_id.value)
        except ValueError:
            logger.debug(
                f"ValueError: Wrong Standard ID is detected:{self._standard_id.value}"
            )
            return None
        logger.info(current_item.name)
        return current_item.value

    def get_cube_name(self) -> Optional[str]:
        return self._cube.name

    def get_battery_level(self) -> Optional[int]:
        battery_info = self._event_loop.run_until_complete(
            self._cube.api.battery.read()
        )
        if battery_info is not None:
            return battery_info.battery_level
        else:
            return None

    def get_3d_angle(self) -> Optional[Tuple[int, int, int]]:
        if self._cube_angle is None:
            return None
        return self._cube_angle.roll, self._cube_angle.pitch, self._cube_angle.yaw

    def get_posture(self) -> Optional[int]:
        if self._motion is None:
            return None
        else:
            return self._motion.posture.value

    def is_button_pressed(self) -> Optional[int]:
        if self._button is None:
            return None
        else:
            return self._button.state

    def turn_on_cube_lamp(self, r: int, g: int, b: int, duration: float) -> None:
        duration = max(duration, 0)
        indicator_param = IndicatorParam(
            duration_ms=0,
            color=Color(r=r, g=g, b=b),
        )
        self._event_loop.run_until_complete(
            self._cube.api.indicator.turn_on(indicator_param)
        )
        if duration > 0:
            self.sleep(duration)
            self._event_loop.run_until_complete(self._cube.api.indicator.turn_off_all())

    def turn_off_cube_lamp(self) -> None:
        self._event_loop.run_until_complete(self._cube.api.indicator.turn_off_all())

    def play_sound(
        self, note: int, duration: float, wait_to_complete: bool = True
    ) -> bool:
        duration_ms = clip(int(duration * 1000), 1, 2550)
        try:
            note_name = Note(note)
        except ValueError:
            logger.debug(f"ValueError: note number {note} is unsupported")
            return False
        midi_notes = [
            MidiNote(
                duration_ms=duration_ms,
                note=note_name,
                volume=255,
            )
        ]
        self._event_loop.run_until_complete(
            self._cube.api.sound.play_midi(
                repeat=1,
                midi_notes=midi_notes,
            )
        )
        if wait_to_complete:
            self.sleep(duration)
        return True

    def stop_sound(self) -> None:
        self._event_loop.run_until_complete(self._cube.api.sound.stop())

    def is_magnet_in_contact(self) -> Optional[int]:
        if self._magnet is None:
            return None
        else:
            return self._magnet.state


class SimpleCube:
    """
    Access to toio core cube by easier method
    Functions that like blocks in visual programming
    """

    _T_LOCK: threading.Lock = threading.Lock()

    def __init__(
        self,
        name: Optional[str] = None,
        timeout: int = 5,
        coordinate_system_class: Type[
            LocalCoordinateSystem
        ] = VisualProgrammingCoordinateSystem,
        log_level: int = NOTSET,
    ) -> None:
        self._event_loop = AsyncSimpleCube.ensure_event_loop()
        self._async = AsyncSimpleCube(
            name=name,
            timeout=timeout,
            coordinate_system_class=coordinate_system_class,
            log_level=log_level,
        )
        with SimpleCube._T_LOCK:
            self._event_loop.run_until_complete(self._async.__aenter__())
        self._cube = self._async._cube

    def __getattr__(self, attr):
        try:
            f = self._async.__getattribute__(attr)
        except AttributeError as ex:
            raise ex

        if inspect.iscoroutinefunction(f):

            def synchronizer(async_attr):
                def wrap_f(*args, **kwargs):
                    return self._event_loop.run_until_complete(
                        async_attr(*args, **kwargs)
                    )

                return wrap_f

            return synchronizer(f)
        else:
            return f

    def __enter__(self):
        return self

    def __exit__(self, _exc_type, _exc_value, _traceback):
        with SimpleCube._T_LOCK:
            self._event_loop.run_until_complete(self._async.disconnect())

    def move(self, speed: int, duration: float, wait_to_complete: bool = True) -> None:
        return self._event_loop.run_until_complete(
            self._async.move(speed, duration, wait_to_complete)
        )

    def spin(self, speed: int, duration: float, wait_to_complete: bool = True) -> None:
        return self._event_loop.run_until_complete(
            self._async.spin(speed, duration, wait_to_complete)
        )

    def run_motor(
        self,
        left_speed: int,
        right_speed: int,
        duration: float,
        wait_to_complete: bool = True,
    ) -> None:
        return self._event_loop.run_until_complete(
            self._async.run_motor(left_speed, right_speed, duration, wait_to_complete)
        )

    def stop_motor(self) -> None:
        return self._event_loop.run_until_complete(self._async.stop_motor())

    def move_steps(self, direction: Direction, speed: int, step: int) -> bool:
        return self._event_loop.run_until_complete(
            self._async.move_steps(direction, speed, step)
        )

    def turn(self, speed: int, degree: int) -> bool:
        return self._event_loop.run_until_complete(self._async.turn(speed, degree))

    def move_to(self, speed: int, x: int, y: int) -> bool:
        return self._event_loop.run_until_complete(self._async.move_to(speed, x, y))

    def set_orientation(self, speed: int, degree: int) -> bool:
        return self._event_loop.run_until_complete(
            self._async.set_orientation(speed, degree)
        )

    def move_to_the_grid_cell(self, speed: int, cell_x: int, cell_y: int) -> bool:
        return self._event_loop.run_until_complete(
            self._async.move_to_the_grid_cell(speed, cell_x, cell_y)
        )

    def get_current_position(self) -> Optional[Tuple[int, int]]:
        return self._event_loop.run_until_complete(self._async.get_current_position())

    def get_x(self) -> Optional[int]:
        return self._event_loop.run_until_complete(self._async.get_x())

    def get_y(self) -> Optional[int]:
        return self._event_loop.run_until_complete(self._async.get_y())

    def get_orientation(self) -> Optional[int]:
        return self._event_loop.run_until_complete(self._async.get_orientation())

    def get_grid(self) -> Optional[Tuple[int, int]]:
        return self._event_loop.run_until_complete(self._async.get_grid())

    def get_grid_x(self) -> Optional[int]:
        return self._event_loop.run_until_complete(self._async.get_grid_x())

    def get_grid_y(self) -> Optional[int]:
        return self._event_loop.run_until_complete(self._async.get_grid_y())

    def is_on_the_gird_cell(self, cell_x: int, cell_y: int) -> bool:
        return self._event_loop.run_until_complete(
            self._async.is_on_the_gird_cell(cell_x, cell_y)
        )

    def is_touched(self, item: StandardIdCard) -> bool:
        return self._event_loop.run_until_complete(self._async.is_touched(item))

    def get_touched_card(self) -> Optional[int]:
        return self._event_loop.run_until_complete(self._async.get_touched_card())

    def get_cube_name(self) -> Optional[str]:
        return self._event_loop.run_until_complete(self._async.get_cube_name())

    def get_battery_level(self) -> Optional[int]:
        return self._event_loop.run_until_complete(self._async.get_battery_level())

    def get_3d_angle(self) -> Optional[Tuple[int, int, int]]:
        return self._event_loop.run_until_complete(self._async.get_3d_angle())

    def get_posture(self) -> Optional[int]:
        return self._event_loop.run_until_complete(self._async.get_posture())

    def is_button_pressed(self) -> Optional[int]:
        return self._event_loop.run_until_complete(self._async.is_button_pressed())

    def turn_on_cube_lamp(self, r: int, g: int, b: int, duration: float) -> None:
        return self._event_loop.run_until_complete(
            self._async.turn_on_cube_lamp(r, g, b, duration)
        )

    def turn_off_cube_lamp(self) -> None:
        return self._event_loop.run_until_complete(self._async.turn_off_cube_lamp())

    def play_sound(
        self, note: int, duration: float, wait_to_complete: bool = True
    ) -> bool:
        return self._event_loop.run_until_complete(
            self._async.play_sound(note, duration, wait_to_complete)
        )

    def stop_sound(self) -> None:
        return self._event_loop.run_until_complete(self._async.stop_sound())

    def is_magnet_in_contact(self) -> Optional[int]:
        return self._event_loop.run_until_complete(self._async.is_magnet_in_contact())


__all__ = [
    "SimpleCube",
    "AsyncSimpleCube",
    "SimpleCube_v1_0",
]
