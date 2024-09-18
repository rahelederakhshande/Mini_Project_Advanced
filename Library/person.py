from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age, id_):
        self.name = name
        self.age = age
        self.id_ = id_

    @abstractmethod
    def introduce(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}(Name: {self.name}, Age: {self.age}, ID: {self.id_})"