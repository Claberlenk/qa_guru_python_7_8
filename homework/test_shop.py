"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)
@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(999)
        assert product.check_quantity(1000)
        assert not product.check_quantity(1001)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        total_qty = product.quantity
        assert total_qty - 500 == 500
        assert not total_qty - 1001 == 500
        assert not total_qty - 0 == 500





    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(product.quantity + 1)
            assert f"недостаточно товара в наличие {product.name}"


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product_in_cart(self, product, cart):
        cart.add_product(product, buy_count=2)
        cart.add_product(product, buy_count=3)
        assert cart.products[product] == 5

    def test_add_and_remove_product_from_cart(self, product, cart):
        cart.add_product(product, buy_count=2)
        assert product in cart.products
        assert cart.products[product] == 2

        cart.remove_product(product, 2)
        assert product not in cart.products

    def test_clear_cart(self,product, cart):
        cart.add_product(product, buy_count=1)
        assert len(cart.products) > 0

        cart.clear()
        assert len(cart.products) == 0

    def test_total_price(self, product, cart):
        cart.add_product(product, buy_count=1)
        assert cart.get_total_price() == 100

        cart.add_product(product, buy_count=3)
        assert cart.get_total_price() == 400

    def test_buy_product(self, product, cart):
        cart.add_product(product, buy_count=1)
        cart.buy()
        assert product.quantity == 999

    def test_buy_more_products(self, product, cart):
        cart.add_product(product, buy_count=1001)
        with pytest.raises(ValueError):
            cart.buy()













