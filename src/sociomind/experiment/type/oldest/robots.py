from functools import cache
from typing import Tuple, List

from robotix.type.uav.quad_copter.model.tarot_t650 import TarotT650
from sensorx.sensor_set import SensorSet
from sensorx.type.lidar.rp_a2.sensor import Sensor as RpA2Lidar
from sensorx.type.gps.odom.sensor import Sensor as GpsOdomSensor

from robotix.mind.mind import Mind
from robotix.mind.memory.memory import Memory
from robotix.mind.memory.memorizing import Memorizing
from robotix.mind.memory.remembering import Remembering
from robotix.mind.memory.storage.storage import Storage
from robotix.mind.memory.storage.level.levels import Levels
from robotix.mind.memory.storage.level.level import Level
from robotix.mind.learn.learn import Learn


class Robots:
    @staticmethod
    @cache
    def get_robots() -> Tuple[TarotT650, TarotT650]:
        """Create the two UAVs only once and reuse them forever."""
        sensor_set = SensorSet([RpA2Lidar(), GpsOdomSensor()])
        memory_levels = Levels(Level(0))
        memory = Memory(Memorizing(), Remembering(), Storage(memory_levels))
        mind = Mind(memory, Learn())

        uav1 = TarotT650(sensor_set, mind)
        uav2 = TarotT650(sensor_set, mind)
        return (uav1, uav2)
