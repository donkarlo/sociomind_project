from typing import List

from robotix.experiment.experiment import Experiment as RobotixExperiment
from robotix.robot import Robot
from sociomind.experiment.scenario.normal import Normal as NormalScenario
from sociomind.experiment.scenario.follow import Follow as FollowScenario
from sociomind.experiment.scenario.next_to import NextTo as NextToScenario




class Oldest(RobotixExperiment):
    def __init__(self):
        print("Oldest experiment is initializing ...")
        learning_scenarios = [NormalScenario()]
        test_scenarios = [FollowScenario(), NextToScenario()]
        super().__init__(learning_scenarios, test_scenarios)
