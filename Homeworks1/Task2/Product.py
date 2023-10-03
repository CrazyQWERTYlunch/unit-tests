class Product:

    def __init__(self, base_cost: int, base_title: str):
        self.set_cost(base_cost)
        self.set_title(base_title)

    def get_cost(self):
        return self.__cost

    def set_cost(self, new_cost):
        self.__cost = new_cost

    def get_title(self):
        return self.__title

    def set_title(self, new_title):
        self.__title = new_title

    @classmethod
    def __verify_cost(cls, other):
        if not isinstance(other, Product):
            raise TypeError("Операнд должен иметь тип Product")
        return other.__cost


    def __eq__(self, other):
        sc = self.__verify_cost(other)
        return self.__cost == sc

    def __repr__(self):
        return f"{self.__title} : {self.__cost}"

    def __str__(self):
        return f"{self.__title} : {self.__cost}"

    def __lt__(self, other):
        sc = self.__verify_cost(other)
        return self.__cost < sc

