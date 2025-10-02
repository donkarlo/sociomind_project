from typing import List

from robotix.experiment.experiment import Experiment as RobotixExperiment
from robotix.robot import Robot
from sociomind.experiment.scenario.normal import Normal as NormalScenario
from sociomind.experiment.scenario.follow import Follow as FollowScenario
from sociomind.experiment.scenario.next_to import NextTo as NextToScenario
from utilix.conf.factory.uniqued_yaml_file import UniquedYamlFile
from robotix.type.uav.quad_copter.model.tarot_t650 import TarotT650


class Oldest(RobotixExperiment):
    def __init__(self):
        print("Oldest experiment is initializing ...")
        learning_scenarios = [NormalScenario()]
        test_scenarios = [FollowScenario(), NextToScenario()]
        super().__init__(learning_scenarios, test_scenarios)

    @staticmethod
    def get_robots()->List[Robot]:
        exp = UniquedYamlFile("configs/experiments.yaml")
        uav1 = TarotT650()#uav1 or the leader
        uav2 = TarotT650()
        return [uav1, uav2]

