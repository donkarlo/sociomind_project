from robotix.mind.decision_making.decision_making import DecisionMaking
from robotix.mind.learning.learning import Learning
from robotix.mind.memory.long_term.explicit.auto_biographic.episodic.experience.collection.collection import Collection as ExperienceCollection
from robotix.mind.memory.long_term.modality.group.group import \
    Group as ModalityCollection
from robotix.mind.memory.trace.kind.kinds import Kinds
from robotix.mind.memory.memorizing.memorizing import Memorizing
from robotix.mind.memory.memory import Memory
from robotix.mind.memory.remembering.remembering import Remembering
from robotix.mind.reasoning.reasoning import Reasoning


class Mind():
    """
    Mind of a single robot
    """
    def __init__(self):
        self._memory:Memory = self._build_memory()
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
        experience_modality_kinds = [Kinds.ditributed_quaternion_kinematic, Kinds.lidar_scan_ranges]
        self._experiences_file_paths = experience_file_path

        for kind in experience_modality_kinds:
            self._


    def _build_experience_modality_stacks(self):
        pass

    def _build_modality_stack_layer(self):
        pass

