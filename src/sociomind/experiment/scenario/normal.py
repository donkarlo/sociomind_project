from mathx.linalg.vec.vec import Vec
from physix.kinematics.pose import Pose
from physix.world.obstacle import Obstacle
from robotix.experiment.scenario import Scenario
from robotix.act.action_set import ActionSet
from robotix.type.uav.quad_copter.action.go_to import GoTo
from sociomind.experiment.scenario.world.hollow_nested_cubes import HollowNestedCubes
from sociomind.experiment.scenario.plan.normal import Normal as NormalPlan
from sociomind.experiment.scenario.mission.synced_turning_arround_corridor import SyncedTurningAroundCorridor
from sociomind.experiment.type.oldest.robots import Robots



class Normal(Scenario):
    def __init__(self):
        self._world = HollowNestedCubes([Obstacle()])
        # pose points from normal scenario points
        self._plan = NormalPlan(ActionSet([GoTo(Pose(Vec([1,2,3]),Vec([1,2,3,4])))]))
        self._mission = SyncedTurningAroundCorridor()

        self._robots = Robots.get_robots()

        super().__init__(self._robots, self._mission, self._world, self._plan)# for the moment we use single robot scenario since follower is totally dependent on the leader during running

    def learn(self)->None:
        print("I am in Normal scenario Learn")