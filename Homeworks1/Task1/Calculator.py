import math


class Calculator:

    @staticmethod
    def calculation(first_operand: int | float, second_operand: int | float, operator: str) -> float:
        result: float

        match operator:
            case '+':
                result = first_operand + second_operand
            case '-':
                result = first_operand - second_operand
            case '*':
                result = first_operand * second_operand
            case '/':
                if second_operand != 0:
                    result = first_operand / second_operand
                else:
                    raise ZeroDivisionError("Деление на ноль не поддерживается")
            case _:
                raise ValueError("Неправильный оператор" + operator)

        return result

    @staticmethod
    def square_root_extraction(num: int | float) -> float:

        if num < 0:
            raise ValueError("Cannot calculate square root of a negative number")

        return math.sqrt(num)

    @staticmethod
    def calculating_discount(purchase_amount: float, discount_amount: int) -> float:
        if type(discount_amount) != int:
            raise ValueError("Скидка указывается целым числом")

        if not 0 < discount_amount <= 100:
            raise ValueError("Размер скидки варьируется от 1 до 100%")

        if purchase_amount < 0:
            raise ValueError("Цена не может быть отрицательной")

        return purchase_amount * (1 - (discount_amount / 100))

