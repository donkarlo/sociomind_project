from mathx.linalg.tensor.vector.vector import Vector
from physix.quantity.kind.dynamic.kinematic.pose.kind.quaternion_pose import QuaternionPose
from physix.world.obstacle import Obstacle
from robotix.experiment.scenario import Scenario
from robotix.structure.kind.mind.action.group.group import Group
from robotix.kind.uav.quad_copter.act.action.go_to import GoTo
from sociomind.experiment.kind.oldest.experience.world.hollow_nested_cubes_narrowed_on_a_side import HollowNestedCubesNarrowedOnASide
from sociomind.experiment.kind.oldest.experience.plan.next_to import NextTo as NextToPlan
from sociomind.experiment.kind.oldest.experience.goal.synced_turning_arround_corridor import SyncedTurningAroundCorridor
from sociomind.experiment.kind.oldest.scenrios import Scenrios


class NextTo(Scenario):
    def __init__(self):
        self._world = HollowNestedCubesNarrowedOnASide([Obstacle()])
        self._plan = NextToPlan(Group([GoTo(QuaternionPose(Vector([1, 2, 3]), Vector([1, 2, 3, 4])))]))  # pose points from normal scenario points
        self._mission = SyncedTurningAroundCorridor()

        self._robots = Scenrios.get_robots()

        super().__init__(self._robots, self._mission, self._world, self._plan, "next_to")

    def learn(self) -> None:
        print("I am in NextTo scenario Learning")