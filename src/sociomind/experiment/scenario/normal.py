from physix.world.obstacle import Obstacle
from robotix.mrs.experiment.scenario import Scenario as MrsScenario
from sociomind.lab.scenario.world.hollow_nested_cubes import HollowNestedCubes
from sociomind.lab.type.oldest.scenrios import Scenrios

from robotix.mental.cognition.memory.long_term.explicit.episodic.experience.level.type.misson_preplan_sensor import MissionPrePlanSensor  as TraceCollectionLevel
from utilix.data.storage.storage import Storage


class Normal(MrsScenario):
    def __init__(self):
        self.__name = Scenrios.get_scnario_configs()["members"]["normal"]["name"]
        self._experience_name = self.__name
        world = HollowNestedCubes([Obstacle()])

        self._robots = Scenrios.get_robots()

        # pose points from normal scenario points
        self._uav1 = self._robots[0]
        self._uav1_plan = Scenrios.get_scnario_plan(self._uav1.get_name(), self.__name)
        self._uav1_mission = Scenrios.get_mission(self._uav1.get_name())

        self._uav2 = self._robots[1]
        self._uav2_plan = Scenrios.get_scnario_plan(self._uav2.get_name(), self.__name)
        self._uav2_mission = Scenrios.get_mission(self._uav2.get_name())

        robots_missions_plans = []
        robots_missions_plans.append([self._uav1, self._uav1_mission, self._uav1_plan])
        robots_missions_plans.append([self._uav2, self._uav2_mission, self._uav2_plan])



        # for the moment we use single robot scenario since follower is totally dependent on the leader during running
        super().__init__(robots_missions_plans, world, self.__name)


    def remember(self)->None:
        uav1_lowest_normal_experience_level_storage:Storage = self._uav1.get_experience_by_name(self._experience_name).get_lowest_level().get_storage()

        trace_collection = TraceCollectionLevel(self._uav1_mission, self._uav1_plan)
        uav1_lowest_normal_experience_level_storage.attach_add_value_observer(trace_collection)

        slc = slice(1,100)
        ram = uav1_lowest_normal_experience_level_storage.get_values_by_slice(slc)

        traces = trace_collection.get_traces()
        print(ram)