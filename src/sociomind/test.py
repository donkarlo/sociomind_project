from utilix.oop.klass.structure.kind.based_on_inheritence import BasedOnInheritence


class Mamal:
    def __init__(self, kind:str, name: str, age: int) -> None:
        self._name = name
        self._age = age
        self._kind = kind

class Person(Mamal):
    def __init__(self, name:str, age:int):
        super().__init__("human",name, age)

class Mohammad(Person):
    def __init__(self, name:str):
        super().__init__("Mohammad", 42)

print(Person)