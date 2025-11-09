from robotix.experiment.experiment import Experiment as RobotixExperiment
from sociomind.experiment.type.oldest.scenario.normal import Normal as NormalScenario
from sociomind.experiment.type.oldest.scenario.follow import Follow as FollowScenario
from sociomind.experiment.type.oldest.scenario.next_to import NextTo as NextToScenario
from sociomind.experiment.type.oldest.scenrios import Scenrios


class Oldest(RobotixExperiment):
    def __init__(self):
        print("Oldest experiment is initializing ...")
        learning_scenarios = [NormalScenario()]
        test_scenarios = [FollowScenario(), NextToScenario()]
        super().__init__(learning_scenarios, test_scenarios)

        # arming robots
        ##first, remeber
        for robot in Scenrios.get_robots():
            robot.remember()
