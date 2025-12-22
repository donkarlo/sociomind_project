from multirobotix.composite.composite import Composite
from multirobotix.group import Group
from robotix.type.human.human import Human
from robotix.type.uav.quad_copter.model.tarot_t650_oldest import TarotT650Oldest
from utilix.data.kind.dic.dic import Dic


class Robots(Composite):
    human_group = Group(Human("Mohamad"))
    robot_group = Group(TarotT650Oldest(""))

    uavs:Dic = Dic({"uav1":{}, "uav2":{}})

