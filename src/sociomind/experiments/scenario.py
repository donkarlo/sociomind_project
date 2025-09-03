rom robotix.goal.goal import Goal
from robotix.type.uav.quad_copter.quad_copter import QuadCopter
from sensorx.obs.sensor_set_obss import SensorSetObss
class Scenario:
    def __init__(self, obss:SensorSetObss , quad_copters:list[QuadCopter,...]):
        pass

    def learn(self)->None:
        pass

    def achieve(self, goals:tuple[Goal,...]) -> None:
        pass