from functools import cache
from robotix.mind.memory.level.level import Level
from robotix.mind.memory.level.level_stack import LevelStack
from robotix.mrs.type.homogeneous.collection_generator import CollectionGenerator as RobotCollectionGenerator
from robotix.plan.mission.mission import Mission
from sociomind.experiment.scenario.mission.synced_turning_arround_corridor import SyncedTurningAroundCorridor
from robotix.plan.plan import Plan
from typing import Tuple
from robotix.type.uav.quad_copter.model.tarot_t650_oldest import TarotT650Oldest
from robotix.mrs.mrs import Mrs as BaseMrs
from utilix.data.storage.factory.uniformated_multi_valued_yaml_file import UniformatedMultiValuedYamlFile
from utilix.data.storage.factory.single_yaml_file import SingleYamlFile
from utilix.data.storage.type.file.file import File
from utilix.os.path import Path
from robotix.mind.memory.episode.experience import Experience
from robotix.mind.memory.episode.experience_set import ExperienceSet
from physix.kinematics.position import Position
from robotix.act.goal.position_tolerance_criterion import PositionToleranceCriterion
from robotix.act.CollectionGenerator import CollectionGenerator as ActionCollectionGenerator
from robotix.act.goal.goal import Goal





class Mrs(BaseMrs):
    @staticmethod
    @cache
    def get_robots() -> Tuple[TarotT650Oldest, TarotT650Oldest]:
        """
        Create the two UAVs only once and reuse them forever.
        """
        scenario_configs_dict = Mrs.get_scnario_configs()


        # uav1 or leader experience
        uav1_name = "uav1"
        uav1_mission = Mrs.get_mission(uav1_name)
        uav1_normal_plan = Mrs.get_scnario_plan(uav1_name, "normal")
        uav1_normal_memeory_level_stack = Mrs.get_normal_experience_memory_level_stack(uav1_name, "normal")
        uav1_normal_experience = Experience(uav1_mission, uav1_normal_plan, uav1_normal_memeory_level_stack, "normal")
        uav1_experience_set = ExperienceSet([uav1_normal_experience])
        uav1 = TarotT650Oldest(uav1_experience_set, uav1_name)

        # uav2 or leader experience
        uav2_name = "uav1"
        uav2_mission = Mrs.get_mission(uav2_name)
        uav2_normal_plan = Mrs.get_scnario_plan(uav2_name, "normal")
        uav2_normal_memeory_level_stack = Mrs.get_normal_experience_memory_level_stack(uav2_name, "normal")
        uav2_normal_experience = Experience(uav2_mission, uav2_normal_plan, uav2_normal_memeory_level_stack, "normal")
        uav2_experience_set = ExperienceSet([uav2_normal_experience])

        uav2 = TarotT650Oldest(uav2_experience_set, uav2_name)

        return (uav1, uav2)

    @staticmethod
    @cache
    def get_scnario_configs()->dict:
        scenarios_configs = SingleYamlFile("../../configs/scenarios.yaml")
        scenario_configs_dict = scenarios_configs.get_ram_dict()
        return scenario_configs_dict

    @staticmethod
    @cache
    def get_mission(robot_name:str)->Mission:
        scenario_configs_dict = Mrs.get_scnario_configs()
        goal_states = scenario_configs_dict["mission"]["goals"]["robots"][robot_name]["states"]

        mission = SyncedTurningAroundCorridor(goal_states)

        return mission

    @staticmethod
    @cache
    def get_scnario_plan(robot_name: str, scanario_name:str)->Plan:
        scenario_configs_dict = Mrs.get_scnario_configs()
        uav_plan = scenario_configs_dict["members"][scanario_name]["robots"][robot_name]["plan"]
        uav_plan_states_file = uav_plan["actions"]["goals"]["states"]["file"]
        vec_sep = uav_plan_states_file["vector_sep"]
        component_sep = uav_plan_states_file["vector_components_sep"]
        uav_status_plan_file_path = uav_plan_states_file["path"]
        action_name = uav_plan["actions"]["name"]

        
        if action_name == "goto":
            from robotix.type.uav.quad_copter.act.action.go_to import GoTo
            sample_goal_state = Position(0,0,0)
            ptc_val = uav_plan["actions"]["goals"]["acceptance_criterion"]["tolerance"]
            sample_goal_acceptance = PositionToleranceCriterion(ptc_val)
            sample_goal = Goal(sample_goal_state, sample_goal_acceptance)
            sample_action = GoTo(sample_goal)
            action_collection = ActionCollectionGenerator.clone_from_vecs_file_path(sample_action, uav_status_plan_file_path, vec_sep, component_sep)
        return Plan(action_collection)

    @staticmethod
    @cache
    def get_normal_experience_memory_level_stack(robot_name:str, scenario_name:str)->LevelStack:
        scnario_configs = Mrs.get_scnario_configs()

        rosbag_shared_dir = scnario_configs["ros"]["bag"]["dir"]
        normal_scenario_ros_bag = scnario_configs["members"][scenario_name]["ros"]["bag"]
        normal_scenario_sor_bag_dir = normal_scenario_ros_bag["dir"]
        rosbag_shared_file_name = normal_scenario_ros_bag["robots"][robot_name]["file"]["name"]

        noramal_file_storage_path = rosbag_shared_dir+ normal_scenario_sor_bag_dir + rosbag_shared_file_name
        file = UniformatedMultiValuedYamlFile(noramal_file_storage_path)

        level_0 = Level(file)
        level_stack = LevelStack([level_0])


        return level_stack




