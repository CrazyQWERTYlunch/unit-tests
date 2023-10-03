from Shop import Shop
from Product import Product

import pytest


@pytest.mark.parametrize("length, bascket",
                         [(4, [Product(10, "asd"), Product(20, "aasd"), Product(50, "sasd"), Product(30, "dasd")]),
                          (0, [])])
def test_quantity_product(length, bascket):
    # Проверка количества продуктов
    sh = Shop()
    sh.set_products(bascket)
    assert len(sh.get_products()) == length


@pytest.mark.parametrize("bascket",
                         [[Product(10, "asd"), Product(20, "aasd"), Product(50, "sasd"), Product(30, "dasd")],
                          []])
def test_content_basket(bascket):
    # Проверка содержимого корзины
    sh = Shop()
    sh.set_products(bascket)
    assert bascket == sh.get_products()


@pytest.mark.parametrize("expected_exception, bascket", [(ValueError, [])])
# TypeError, ['a', 'b', 'c']] - можно сделать проверку но это повлечёт к созданию  кучи других доп. тестов
def test_get_most_with_error(expected_exception, bascket):
    sh = Shop()
    sh.set_products(bascket)
    with pytest.raises(expected_exception):
        sh.get_most_expensive_product()


@pytest.mark.parametrize("most_expensive, bascket",
                         [(Product(50, "sasd"),
                           [Product(10, "asd"), Product(20, "aasd"), Product(50, "sasd"), Product(30, "dasd")])])
def test_get_most_expensive_product(most_expensive, bascket):
    # Напишите тесты для проверки корректности работы метода getMostExpensiveProduct.
    sh = Shop()
    sh.set_products(bascket)
    assert most_expensive == sh.get_most_expensive_product()


@pytest.mark.parametrize("sort_res, bascket",
                         [([Product(10, "asd"), Product(20, "aasd"), Product(30, "dasd"), Product(50, "sasd")],
                           [Product(10, "asd"), Product(20, "aasd"), Product(50, "sasd"), Product(30, "dasd")]),
                          ([Product(1, "dasd"), Product(12, "sasd"), Product(13, "asd"), Product(400, "aasd")],
                          [Product(13, "asd"), Product(400, "aasd"), Product(1, "dasd"), Product(12, "sasd")]),
                          ([], [])])
def test_sort_products_by_price(sort_res, bascket):
    sh = Shop()
    sh.set_products(bascket)
    assert sort_res == sh.sort_products_by_price()