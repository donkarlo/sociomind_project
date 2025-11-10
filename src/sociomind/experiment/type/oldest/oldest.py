from utilix.data.storage.type.file.format.kind.yaml.yaml import Yaml as YamlFormat
from multirobotix.group import Group as RobotGroup
from multirobotix.experiment.experiment import Experiment
from robotix.mind.memory.composite.composite import Composite as CompositeMemory
from robotix.mind.memory.trace.group.decorator.storaged import Storaged as StoragedTraceGroup
from robotix.mind.memory.trace.group.group import Group as TraceGroup
from robotix.mind.memory.trace.kind.kinds import Kinds as FilledTraceKinds
from utilix.data.storage.decorator.multi_valued.multi_valued import MultiValued
from utilix.data.storage.decorator.multi_valued.uniformated import UniFormated
from utilix.data.storage.factory.uniformated_multi_valued_yaml_file import UniformatedMultiValuedYamlFile
from utilix.data.storage.type.file.file import File
from utilix.data.type.dic.dic import Dic
from utilix.os.path.path import Path


class Oldest(Experiment):
    """
    """

    def __init__(self):
        print("Oldest experiment is initializing ...")

        shared_path = "/home/donkarlo/Dropbox/phd/data/experiements/oldest/${uav_name}/mind/memory/experiences/"
        shared_all_modalities_file_name = "all_modalities.yaml"

        robot_props = [Dic({"name": "uav1"})]
        # robot_props.append(Dic({"name": "uav2"}))

        experience_props = [Dic({"name": "normal"})]
        # experience_props.append(Dic({"name": "follow"}))
        # experience_props.append(Dic({"name": "next_to"}))

        modality_props = [Dic({"name": FilledTraceKinds.ditributed_quaternion_kinematic.name}),
                          Dic({"name": FilledTraceKinds.lidar_scan_ranges.name})]



        for robot_prop in robot_props:
            # we have ros files for each experience independently so we send None here
            robot_experience_composite_memory_root = CompositeMemory(None, robot_prop["name"])
            robot_name_replaced_path = shared_path.replace("${uav_name}", robot_prop["name"])

            #Go through the experience of each robot
            for robot_experience_prop in experience_props:
                robot_experience_dir_path = robot_name_replaced_path+ Path.get_os_path_separator() + robot_experience_prop["name"]
                robot_experience_file_path = robot_experience_dir_path + Path.get_os_path_separator() + shared_all_modalities_file_name

                robot_experience_trace_group = StoragedTraceGroup(TraceGroup(None), UniformatedMultiValuedYamlFile(robot_experience_file_path))

                robot_experience_composite_memory_node = CompositeMemory(robot_experience_trace_group, robot_experience_prop["name"])

                robot_experience_composite_memory_root.add_child(robot_experience_composite_memory_node)

                #Go through the modality of each experience
                for modality_prop in modality_props:
                    robot_exp_mod_path = robot_experience_dir_path + Path.get_os_path_separator() + modality_prop["name"]
                    robot_exp_mod_storage = StoragedTraceGroup(TraceGroup(None), UniFormated(MultiValued(File(Path(robot_exp_mod_path)),"---"),YamlFormat))
                    modality_trace_group = StoragedTraceGroup(TraceGroup(None), robot_exp_mod_storage)
                    robot_modality_memory_node = CompositeMemory(modality_trace_group, modality_prop["name"])
                    robot_experience_composite_memory_node.add_child(robot_modality_memory_node)

        robot_experience_composite_memory_root.draw_tree()



        # now that we have the mind aqnd memory tree lets build the the Robot Group
        # human_group = RobotGroup(Human())
        # robot_group = LeaderFollowers(TarotT650Oldest(""), [TarotT650Oldest("")])
        # self._composite_robot_group = CompositeRobotGroup()
        # self._composite_robot_group.add_child(robot_group)
        # self._composite_robot_group.add_child(human_group)

        # building scenarios
        # learning_scenarios = [NormalScenario()]
        # test_scenarios = [FollowScenario(), NextToScenario()]
        # super().__init__(learning_scenarios, test_scenarios)

    def get_robot_group(self) -> RobotGroup:
        return self._composite_robot_group

if __name__ == "__main__":
    experiment = Oldest()