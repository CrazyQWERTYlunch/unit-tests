from abc import ABC, abstractmethod

class Vehicle(ABC):
    __company: str
    __model: str
    __year_release: int
    __num_wheels: int
    __speed: int

    @abstractmethod
    def test_drive(self):
        raise NotImplementedError("В дочернем классе должен быть переопределён метод test_drive()")

    @abstractmethod
    def park(self):
        raise NotImplementedError("В дочернем классе должен быть переопределён метод park()")