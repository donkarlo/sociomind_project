from robotix.mind.memory.composite.decorator.segregatored import Segregatored
from robotix.mind.memory.composite.factory.stack import Stack as CompositeMemoryStack
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
from utilix.os.file_system.path.path import Path


class Oldest(Experiment):
    """
    """

    def __init__(self):
        print("Oldest experiment is initializing ...")

        path_sep = Path.get_os_path_separator()
        shared_path = "/home/donkarlo/Dropbox/phd/data/experiements/oldest/robots/"
        shared_mind_path = "mind/"
        shared_path_to_exps = "memory/long_term/explicit/episodic/experience/"
        # [0, -1] is to get rid of the the trailing slash experience/
        shared_path_parts_to_exps = shared_path_to_exps.split(path_sep)[0:-1]
        shared_all_mod_file_name = "all_modalities.yaml"

        robot_props = [Dic({"name": "uav1"})]
        # robot_props.append(Dic({"name": "uav2"}))

        exp_props = [Dic({"name": "normal"})]
        # experience_props.append(Dic({"name": "follow"}))
        # experience_props.append(Dic({"name": "next_to"}))

        modality_props = [Dic({"name": FilledTraceKinds.ditributed_quaternion_kinematic.name}),
                          Dic({"name": FilledTraceKinds.lidar_scan_ranges.name})]



        for robot_prop in robot_props:
            compit_mem_stack = CompositeMemoryStack(shared_path_parts_to_exps)
            # we have ros files for each experience independently so we send None here
            robot_name = robot_prop["name"]
            robot_exp_compit_memory_root = compit_mem_stack.get_root_composite()
            robot_shared_mind_path = shared_path + robot_name + path_sep + shared_mind_path
            robot_shared_exps_path = robot_shared_mind_path + shared_path_to_exps

            #Go through the experience of each robot
            for robot_exp_prop in exp_props:
                exp_name = robot_exp_prop["name"]
                robot_exp_dir_path = robot_shared_exps_path+ path_sep + exp_name + path_sep
                robot_exp_all_mod_file_path = robot_exp_dir_path + path_sep + shared_all_mod_file_name

                robot_exp_trace_group = StoragedTraceGroup(TraceGroup(None, shared_all_mod_file_name), UniformatedMultiValuedYamlFile(robot_exp_all_mod_file_path, False))

                robot_exp_composite_memory_node = Segregatored(CompositeMemory(robot_exp_trace_group, exp_name))

                compit_mem_stack.get_deepest_composite().add_child(robot_exp_composite_memory_node)

                #Go through the modality of each experience
                for modality_prop in modality_props:
                    mod_name = modality_prop["name"]
                    robot_exp_mod_path = Path(robot_exp_dir_path + mod_name)
                    
                    robot_exp_mod_storage = UniFormated(MultiValued(File(robot_exp_mod_path, False),"---"),YamlFormat)

                    modality_trace_group = StoragedTraceGroup(TraceGroup(None, mod_name), robot_exp_mod_storage)

                    robot_modality_memory_node = CompositeMemory(modality_trace_group, mod_name)
                    robot_exp_composite_memory_node.add_child(robot_modality_memory_node)

            robot_exp_compit_memory_root.draw_tree()
            robot_exp_compit_memory_root.draw()
            robot_exp_compit_memory_root.create_directory_structure(Path(robot_shared_mind_path), "pkl")



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