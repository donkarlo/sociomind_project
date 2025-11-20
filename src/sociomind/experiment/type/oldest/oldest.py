from robotix.mind.memory.composite.decorator.segregatored import Segregatored
from robotix.mind.memory.composite.factory.from_name_dictionary import FromNameDictionary as CompositeMemoryDic
from robotix.mind.memory.composite.segregation.segregator.kind.ros_bag_yaml_message_segragator import \
    RosBagYamlMessageSegragator
from robotix.mind.memory.trace.group.kind.ros_multi_modal_yaml_messages import RosMultiModalYamlMessages

from multirobotix.group import Group as RobotGroup
from multirobotix.experiment.experiment import Experiment
from robotix.mind.memory.composite.composite import Composite as CompositeMemory
from robotix.mind.memory.trace.group.decorator.storaged import Storaged as StoragedTraceGroup
from robotix.mind.memory.trace.group.group import Group as TraceGroup
from robotix.mind.memory.trace.kind.kinds import Kinds as PotentialFilledTraceKinds
from utilix.data.storage.factory.uniformated_multi_valued_yaml_file import UniformatedMultiValuedYamlFile
from utilix.data.storage.kind.file.file import File
from utilix.data.kind.dic.dic import Dic
from utilix.os.file_system.path.path import Path


class Oldest(Experiment):
    """
    """

    def __init__(self):
        print("Oldest experiment is initializing ...")

        path_sep = Path.get_os_path_separator()
        shared_path = "/home/donkarlo/Dropbox/phd/data/experiements/oldest/robots/"
        shared_mind_path = "mind/"
        memory_tree_dic = Dic(
            {
                "memory": {
                    "long_term": {
                        "explicit": {
                            "auto_biographic": {},
                            "episodic": {},
                            "semantic": {}
                        }
                    },
                    "short_term": {}
                }
            }
        )
        shared_path_to_expisode = memory_tree_dic.get_shortest_path("memory", "episodic", path_sep)+path_sep

        # [0, -1] is to get rid of the the trailing slash experience/
        shared_all_mod_file_name = "all_modalities.yaml"

        robot_props = [Dic({"name": "uav1"})]
        # robot_props.append(Dic({"name": "uav2"}))

        #episode here is the experience name
        episode_props = [Dic({"name": "normal"})]
        # experience_props.append(Dic({"name": "follow"}))
        # experience_props.append(Dic({"name": "next_to"}))

        modality_props = [Dic({"name": PotentialFilledTraceKinds.gaussianed_quaternion_kinematic.name}),
                          Dic({"name": PotentialFilledTraceKinds.lidar_scan_ranges.name})]



        for robot_prop in robot_props:
            robot_name = robot_prop["name"]
            compit_mem_tree = CompositeMemoryDic(memory_tree_dic)
            # we have ros files for each experience independently so we send None here
            robot_episode_compit_mem_root = compit_mem_tree.get_root_composite()

            robot_shared_mind_path = shared_path + robot_name + path_sep + shared_mind_path
            robot_shared_episode_path = robot_shared_mind_path + shared_path_to_expisode

            #Go through the episode of each robot
            # EPSODE IS HERE NORMA OR FOLLOW OR NEXT TO EXPERIENCES
            for episode_prop in episode_props:
                episode_name = episode_prop["name"]
                robot_episode_dir_path = robot_shared_episode_path+ path_sep + episode_name + path_sep
                robot_episode_all_mod_file_path = robot_episode_dir_path + path_sep + shared_all_mod_file_name

                robot_episode_trace_group = StoragedTraceGroup(TraceGroup.init_from_traces_and_kind_and_name(None, RosMultiModalYamlMessages(), shared_all_mod_file_name), UniformatedMultiValuedYamlFile(robot_episode_all_mod_file_path, False))

                #building mixed modelity which should be segregated to be able to segregate each episode
                compit_mem_episode = CompositeMemory(robot_episode_trace_group, episode_name)
                robot_episode_compit_mem = Segregatored(compit_mem_episode, RosBagYamlMessageSegragator(compit_mem_episode, slice(1, 1000)))


                robot_episode_compit_mem_root.get_child_by_name("episodic").add_child(robot_episode_compit_mem)
                robot_episode_compit_mem.create_segregated_componnets_as_children()

                robot_episode_compit_mem_root.draw()
                print(robot_episode_compit_mem_root.get_tree())

                #Go through the modality of each experience
            #     for modality_prop in modality_props:
            #         mod_name = modality_prop["name"]
            #         robot_episode_mod_path = Path(robot_episode_dir_path + mod_name)
            #
            #         robot_episode_mod_storage = UniTraceKinded(MultiValued(File(robot_episode_mod_path, False),"---"),YamlFormat)
            #
            #         modality_trace_group = StoragedTraceGroup(TraceGroup(None, mod_name), robot_episode_mod_storage)
            #
            #         robot_modality_memory_node = CompositeMemory(modality_trace_group, mod_name)
            #         robot_episode_compit_mem.add_child(robot_modality_memory_node)
            #
            # robot_exp_compit_memory_root.draw_tree()
            # robot_exp_compit_memory_root.draw()
            # robot_exp_compit_memory_root.create_directory_structure(Path(robot_shared_mind_path), "pkl")



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