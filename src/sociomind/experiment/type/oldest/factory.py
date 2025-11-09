from multirobotix.group import Group as RobotGroup
from multirobotix.composite.composite import Composite as CompositeRobotGroup
from multirobotix.kind.leader_follower.leader_followers import LeaderFollowers
from robotix.mind.memory.composite.composite import Composite as CompositeMemory
from robotix.mind.memory.trace.kind.kinds import Kinds as FilledTraceKinds
from robotix.type.human.human import Human
from robotix.type.uav.quad_copter.model.tarot_t650_oldest import TarotT650Oldest
from utilix.data.storage.factory.uniformated_multi_valued_yaml_file import UniformatedMultiValuedYamlFile
from utilix.data.type.dic.dic import Dic
from robotix.mind.memory.trace.group.group import Group as TraceGroup


class Factory(object):
    """
    """
    def __init__(self):


        shared_path = "/home/donkarlo/Dropbox/projs/research/data/self-aware-drones/ctumrs/two-drones/"
        self._robot_experience_names = ["normal", "follow", "next_to"]
        all_modalities_file_name = "${uav_name}_odometry_odom_gps_rplidar_scan.yaml"

        self._experiences = [Dic({"name": "normal"}), Dic({"name", "follow"}), Dic({"name", "next_to"})]

        modalities = [Dic({"name": FilledTraceKinds.ditributed_quaternion_kinematic.name}), Dic({"name": FilledTraceKinds.lidar_scan_ranges.name})]


        robots = [Dic({"name":"uav1"}),Dic({"name":"uav2"})]

        for robot in robots:
            robot_composite_memory = CompositeMemory("base")
            for robot_experience in self._experiences:
                robot_exprience_file_path = shared_path+ robot_experience["name"]+"/"+all_modalities_file_name.replace("${uav_name}",robot["name"])

                trace_group = TraceGroup(UniformatedMultiValuedYamlFile(robot_exprience_file_path))
                robot_composite_memory.add_child(trace_group)
                for modality in modalities:
                    pass

        human_group = RobotGroup(Human())

        robot_group = LeaderFollowers(TarotT650Oldest(""), [TarotT650Oldest("")])

        composite_robot_group = CompositeRobotGroup()
        composite_robot_group.add_child(robot_group)
        composite_robot_group.add_child(human_group)




