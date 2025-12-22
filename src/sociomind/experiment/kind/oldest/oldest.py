from robotix.mind.memory.composite.decorator.segregatored.segregatored import Segregatored
from robotix.mind.memory.composite.factory.from_name_dictionary import FromNameDictionary as CompositeMemoryDic
from robotix.mind.memory.composite.segregation.segregator.kind.ros_bag_yaml_message_segragator import \
    RosBagYamlMessageSegragator
from robotix.mind.memory.schema import Schema
from robotix.mind.memory.trace.group.kind.ros_multi_modal_yaml_messages import RosMultiModalYamlMessages

from multirobotix.group import Group as RobotGroup
from multirobotix.experiment.experiment import Experiment
from robotix.mind.memory.composite.composite import Composite as CompositeMemory
from robotix.mind.memory.trace.group.decorator.storaged import Storaged as StoragedTraceGroup
from robotix.mind.memory.trace.group.group import Group as TraceGroup
from robotix.mind.memory.trace.kind.core.kinds import Kinds as PotentialFilledTraceKinds
from utilix.data.storage.factory.uniformated_multi_valued_yaml_file import UniformatedMultiValuedYamlFile
from utilix.data.kind.dic.dic import Dic
from utilix.os.file_system.path.path import Path


class Oldest(Experiment):
    """
    """

    def __init__(self):
        print("Oldest experiment is initializing ...")

        # slices to load
        slc = slice(1, 300000)

        path_sep = Path.get_os_path_separator()
        shared_path = "/home/donkarlo/Dropbox/phd/data/experiements/oldest/robots/"
        shared_mind_path = "mind/"
        memory_tree_dic = Schema().get_schema_dic()
        shared_path_to_expisode = memory_tree_dic.get_shortest_path("memory", "episodic", path_sep)+path_sep

        # each file is named all_modalities.yaml
        all_mixed_memory_traces_for_single_episode = "all_modalities.yaml"

        robots_props = [Dic({"name": "uav1"})]
        # robots_props.append(Dic({"name": "uav2"}))

        #episode here is the experience name
        episode_props = [Dic({"name": "normal"})]
        # experience_props.append(Dic({"name": "follow"}))
        # experience_props.append(Dic({"name": "next_to"}))

        modality_props = [Dic({"name": PotentialFilledTraceKinds.gaussianed_quaternion_kinematic.name}),
                          Dic({"name": PotentialFilledTraceKinds.lidar_scan_ranges.name})]


        # building the robots and loading their mind
        for robot_prop in robots_props:
            robot_name = robot_prop["name"]

            # Building memory
            composit_memmory_tree = CompositeMemoryDic(memory_tree_dic)

            ## we have ros files for each experience independently so we send None here
            robot_episode_composit_mem_root = composit_memmory_tree.get_root_composite()

            robot_shared_mind_path = shared_path + robot_name + path_sep + shared_mind_path
            robot_shared_episode_path = robot_shared_mind_path + shared_path_to_expisode

            #Go through the episode of each robot
            for episode_prop in episode_props:
                episode_name = episode_prop["name"]
                robot_episode_dir_path = robot_shared_episode_path+ path_sep + episode_name + path_sep
                robot_episode_all_mod_file_path = robot_episode_dir_path + path_sep + all_mixed_memory_traces_for_single_episode



                uniformatted_multi_valued_yaml_file = UniformatedMultiValuedYamlFile(robot_episode_all_mod_file_path,
                                                                                     slc,False)

                robot_episode_trace_group = StoragedTraceGroup(TraceGroup.init_from_traces_and_kind_and_name(None, RosMultiModalYamlMessages(), all_mixed_memory_traces_for_single_episode), uniformatted_multi_valued_yaml_file)

                #Todo:  is segregation possible? the robot should ask itself and decide base on relatned nodes
                #TODO: the robot should understand if it needs segregation according to anomally level or not?
                #TODO: is resegregation necessary?
                #building mixed modality which should be segregated to be able to segregate each episode
                composite_memory_episode = CompositeMemory(robot_episode_trace_group, episode_name)
                robot_segregatble_episode_composit_memory = Segregatored(composite_memory_episode, RosBagYamlMessageSegragator(composite_memory_episode, slc))

                # add normal episode for example and then follow and next_to
                robot_episode_composit_mem_root.get_child_by_name("episodic").add_child(robot_segregatble_episode_composit_memory)

                # if normal is added, now segregate it
                robot_segregatble_episode_composit_memory.create_segregated_componnets_as_children()

                robot_episode_composit_mem_root.draw()
                print(robot_episode_composit_mem_root.get_tree())
                # Klass.init_from_object(robot_segregatble_episode_composit_memory).draw_inherited_classes()



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