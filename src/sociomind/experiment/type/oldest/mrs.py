from functools import cache
from robotix.mrs.type.homogeneous.factory import Factory
from typing import Tuple
from robotix.type.uav.quad_copter.model.tarot_t650_oldest import TarotT650Oldest
from sensorx.sensor_set import SensorSet
from robotix.mrs.mrs import Mrs as BaseMrs
from utilix.data.storage.factory.uniformated_multi_valued_yaml_file import UniformatedMultiValuedYamlFile
from utilix.data.storage.factory.single_yaml_file import SingleYamlFile
from utilix.os.path import Path


class Mrs(BaseMrs):
    @staticmethod
    @cache
    def get_robots() -> Tuple[TarotT650Oldest, TarotT650Oldest]:
        """
        Create the two UAVs only once and reuse them forever.
        """
        scenarios_conf = SingleYamlFile("../../configs/scenarios.yaml")
        scenario_configs = scenarios_conf.get_ram_dict()
        print(scenario_configs)


        normal_scenario_storage_path = scenario_configs["ros"]["bag"]["dir"]+scenario_configs["members"]["normal"]["ros"]["bag"]["dir"]+ scenario_configs["ros"]["bag"]["file"]


        path = Path(normal_scenario_storage_path)
        normal_scenario_storage = UniformatedMultiValuedYamlFile(path)

        sample_robot = TarotT650Oldest(normal_scenario_storage)

        homogenous_robot_factory = Factory(sample_robot)
        homogenous_robot_factory.add_robots(["uav1", "uav2"])
        robots = homogenous_robot_factory.get_robots()

        return (robots[0], robots[1])



