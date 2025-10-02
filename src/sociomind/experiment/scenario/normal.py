from mathx.linalg.vec.vec import Vec
from physix.kinematics.pose import Pose
from physix.world.obstacle import Obstacle
from robotix.experiment.scenario import Scenario
from robotix.spa.action.action_set import ActionSet
from robotix.type.uav.quad_copter.action.go_to import GoTo
from sociomind.experiment.scenario.world.hollow_nested_cubes import HolloNestedCubes
from sociomind.experiment.scenario.plan.normal import Normal as NormalPlan
from sociomind.experiment.scenario.goal.synced_turning_arround_corridor import SyncedTurningAroundCorridor



class Normal(Scenario):
    def __init__(self):
        self._world = HolloNestedCubes([Obstacle()])
        # pose points from normal scenario points
        self._plan = NormalPlan(ActionSet([GoTo(Pose(Vec([1,2,3]),Vec([1,2,3,4])))]))
        self._goal = SyncedTurningAroundCorridor()

        from sociomind.experiment.type.oldest import Oldest
        self._robots = Oldest.get_robots()[0]

        super().__init__(self._robots, self._goal, self._world, self._plan)# for the moment we use single robot scenario since follower is totally dependent on the leader during running

    def learn(self)->None:
        print("I am in Normal scenario Learn")