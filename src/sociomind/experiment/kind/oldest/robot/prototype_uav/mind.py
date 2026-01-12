from robotix.mind.cognition.process.kind.thinking.decision_making.decision_making import DecisionMaking
from robotix.structure.kind.mind.learning.learning import Learning
from robotix.mind.memory.long_term.explicit.auto_biographic.episodic.experience.collection.collection import Collection as ExperienceCollection
from robotix.structure.kind.mind.process.kind.memory.kind.long_term.modality.group.group import \
    Group as ModalityCollection
from robotix.structure.kind.mind.process.kind.memory.composite.trace.kind.core.kinds import Group
from robotix.structure.kind.mind.process.kind.memory.memorizing.memorizing import Memorizing
from robotix.structure.mind.process.kind.memory.kind.working.working import Working
from robotix.structure.kind.mind.process.kind.memory.remembering.remembering import Remembering
from robotix.mind.cognition.process.kind.thinking.reasoning.reasoning import Reasoning


class Mind():
    """
    Mind of a single robot
    """
    def __init__(self):
        self._memory:Working = self._build_memory()
        self._learning:Learning = self._build_learning()
        self._reasoning:Reasoning = self._build_reasoning()
        self._decision_making:DecisionMaking = self._build_decision_making()

    def _build_memory(self):
        self._experiences = ExperienceCollection()
        self._memorizing = Memorizing()
        self._remembering = Remembering()

    def _build_memory_experiences(self):
        self._experiences = ExperienceCollection()
        self._build_experience_modalities()

    def _build_experience_modalities(self)-> ModalityCollection:
        """
        All experiences have the same modality architecture ie all have lidar and gps
        :return:
        """
        experience_modality_kinds = [Group.gaussianed_quaternion_kinematic, Group.lidar_scan_ranges]
        self._experiences_file_paths = experience_file_path

        for kind in experience_modality_kinds:
            pass


    def _build_experience_modality_stacks(self):
        pass

    def _build_modality_stack_layer(self):
        pass

