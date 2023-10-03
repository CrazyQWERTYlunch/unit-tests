from Calculator import Calculator
import pytest


# проверка базового функционала
@pytest.mark.parametrize("first_operand, second_operand, operator, result", [(8, 2, '+', 10),
                                                                             (8, 2, '-', 6),
                                                                             (8, 2, '*', 16),
                                                                             (8, 2, '/', 4)])
def test_basic_func(first_operand, second_operand, operator, result):
    # Проверка базового функционала с целыми числами
    if result != Calculator.calculation(first_operand, second_operand, operator):
        raise AssertionError("Ошибка метода")


@pytest.mark.parametrize("first_operand, second_operand, operator, result", [(8, 2, '+', 10),
                                                                             (8, 2, '-', 6),
                                                                             (8, 2, '*', 16),
                                                                             (8, 2, '/', 4)])
def test_positive_base_func(first_operand, second_operand, operator, result):
    # Проверка базового функционала с использованием утверждений
    assert Calculator.calculation(first_operand, second_operand, operator) == result


@pytest.mark.parametrize("expected_exception,first_operand, second_operand, operator", [(ValueError, 1, 2, "c"),
                                                                                        (TypeError, 10, '20', '+'),
                                                                                        (TypeError, 10, 20, 2),
                                                                                        (ZeroDivisionError, 3, 0, '/')])
def test_calculate_with_error(expected_exception, first_operand, second_operand, operator):
    # Проверка ожидаемого исключения
    try:
        Calculator.calculation(first_operand, second_operand, operator)
    except expected_exception:
        print("Ошибка в методе")


@pytest.mark.parametrize("expected_exception, first_operand, second_operand, operator", [(ValueError, 1, 2, "c"),
                                                                                        (TypeError, 10, '20', '+'),
                                                                                        (TypeError, 10, 20, 2),
                                                                                        (ZeroDivisionError, 3, 0, '/')])
def test_positive_calculate_with_error(expected_exception, first_operand, second_operand, operator):
    # Проверка ожидаемого исключения через утверждения
    with pytest.raises(expected_exception):
        Calculator.calculation(first_operand, second_operand, operator)


@pytest.mark.parametrize("expected_exception, num", [(ValueError, -1),
                                                     (TypeError, 'a')])
def test_parameter_square_root_extraction(expected_exception, num):
    with pytest.raises(expected_exception):
        Calculator.square_root_extraction(num)



@pytest.mark.parametrize("expected_exception, purchase_amount, discount_amount", [(ValueError, 1200, 23.2),
                                                                                  (ValueError, 1300, 120),
                                                                                  (ValueError, -123, 100),
                                                                                  (ValueError, 1200, -1),
                                                                                  (TypeError, 'a', 10)])
# (TypeError, 1200, 'a') не пройдёт проверку поскольку завалит тест по первому критерию
def test_calculating_discount(expected_exception, purchase_amount, discount_amount):
    with pytest.raises(expected_exception):
        Calculator.calculating_discount(purchase_amount, discount_amount)