from Homeworks.Homeworks1.Task2.Product import Product


class Shop:
    __products: list

    def get_products(self) -> list[Product]:
        return self.__products

    def set_products(self, products: list[Product]):
        products
        self.__products = products

    def sort_products_by_price(self) -> list[Product]:
        # Возвращает отсортированный по возрастанию список продуктов
        sorted_cost = sorted(self.__products, key=lambda x: x.get_cost())
        return sorted_cost

    def get_most_expensive_product(self) -> Product:
        # Возвращает самый дорогой продукт
        if not self.__products:
            raise ValueError("Продуктов нет")
        return max(self.__products)

#
# sh1 = Shop()
# sh1.set_products([Product(10, "asd"), Product(20, "aasd"), Product(50, "sasd"), Product(30, "dasd")])
# print(sh1.get_products())
# print(sh1.get_most_expensive_product())
# print(sh1.sort_products_by_price())
