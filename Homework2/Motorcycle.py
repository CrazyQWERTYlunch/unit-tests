from Vehicle import Vehicle


class Motorcycle(Vehicle):
    __company: str
    __model: str
    __year_release: int
    __num_wheels: int
    __speed: int

    def __init__(self, company: str, model: str, year: int):
        self.__company = company
        self.__model = model
        self.__year_release = year
        self.__num_wheels = 2
        self.__speed = 0

    def test_drive(self):
        self.__speed = 75

    def park(self):
        self.__speed = 0

    def get_company(self):
        return self.__company

    def get_model(self):
        return self.__model

    def get_year_release(self):
        return self.__year_release

    def get_num_wheels(self):
        return self.__num_wheels

    def get_speed(self):
        return self.__speed

    def __str__(self):
        return f"This motorcycle  is a {self.__year_release}"
