from mathx.linalg.tensor.vector.vector import Vector
from physix.quantity.type.kinematic.pose.type.quaternion_pose import QuaternionPose
from physix.world.obstacle import Obstacle
from robotix.experiment.scenario import Scenario
from robotix.act.action_collection import ActionCollection
from robotix.type.uav.quad_copter.act.action.go_to import GoTo
from sociomind.experiment.scenario.world.hollow_nested_cubes_narrowed_on_a_side import HollowNestedCubesNarrowedOnASide
from sociomind.experiment.scenario.plan.follow import Follow as FollowPlan
from sociomind.experiment.scenario.mission.synced_turning_arround_corridor import SyncedTurningAroundCorridor
from sociomind.experiment.type.oldest.scenrios import Scenrios


class Follow(Scenario):
    def __init__(self):
        self._world = HollowNestedCubesNarrowedOnASide([Obstacle()])
        self._plan = FollowPlan(ActionCollection([GoTo(QuaternionPose(Vector([1, 2, 3]), Vector([1, 2, 3, 4])))]))  # pose points from normal scenario points
        self._mission = SyncedTurningAroundCorridor()

        self._robots = Scenrios.get_robots()

        super().__init__(self._robots, self._mission, self._world, self._plan, "follow")

    def learn(self) -> None:
        print("I am in Follow scenario Learn")