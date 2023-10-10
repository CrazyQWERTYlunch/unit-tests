import pytest

from Homework2.Car import Car
from Homework2.Motorcycle import Motorcycle


@pytest.fixture(scope="session")
def proto_car():
    """Фикустура для создания автомобиля"""
    return Car("Asda", "Grafa", 2015)


@pytest.fixture(scope="session")
def proto_motorcycle():
    """Фикстура для создания мотоцикла"""
    return Motorcycle("Grapa", "Trava", 2017)
