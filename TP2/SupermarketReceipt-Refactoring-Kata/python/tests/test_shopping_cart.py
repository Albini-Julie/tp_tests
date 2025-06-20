import unittest
from unittest.mock import Mock
from shopping_cart import ShoppingCart
from model_objects import Product, Offer, SpecialOfferType
from tests.fake_catalog import FakeCatalog

class TestShoppingCart(unittest.TestCase):

    def test_add_item_and_quantity(self):
        cart = ShoppingCart()
        apple = Product("Apple", 1.0)

        cart.add_item(apple)
        cart.add_item_quantity(apple, 2)

        self.assertEqual(cart.product_quantities[apple], 3)
        self.assertEqual(len(cart.items), 2)

    def test_handle_three_for_two_offer(self):
        apple = Product("Apple", 1.0)
        cart = ShoppingCart()
        cart.add_item_quantity(apple, 3)

        offer = Offer(SpecialOfferType.THREE_FOR_TWO, apple, 0)
        offers = {apple: offer}

        catalog = FakeCatalog()
        catalog.add_product(apple, 1.0)

        receipt = Mock()
        receipt.add_discount = Mock()

        cart.handle_offers(receipt, offers, catalog)

        receipt.add_discount.assert_called_once()

    def test_handle_two_for_amount_offer(self):
        apple = Product("Apple", 1.0)
        cart = ShoppingCart()
        cart.add_item_quantity(apple, 3)

        offer = Offer(SpecialOfferType.TWO_FOR_AMOUNT, apple, 1)
        offers = {apple: offer}

        catalog = FakeCatalog()
        catalog.add_product(apple, 1.0)

        receipt = Mock()
        receipt.add_discount = Mock()

        cart.handle_offers(receipt, offers, catalog)

        receipt.add_discount.assert_called_once()
        discount_arg = receipt.add_discount.call_args[0][0]
        self.assertEqual(discount_arg.product, apple)
        self.assertIn("2 for 1", discount_arg.description)
        self.assertLess(discount_arg.discount_amount, 0)

    def test_handle_five_for_amount_offer(self):
        apple = Product("Apple", 1.0)
        cart = ShoppingCart()
        cart.add_item_quantity(apple, 6)

        offer = Offer(SpecialOfferType.FIVE_FOR_AMOUNT, apple, 3)
        offers = {apple: offer}

        catalog = FakeCatalog()
        catalog.add_product(apple, 1.0)

        receipt = Mock()
        receipt.add_discount = Mock()

        cart.handle_offers(receipt, offers, catalog)

        receipt.add_discount.assert_called_once()
        discount_arg = receipt.add_discount.call_args[0][0]  
        self.assertEqual(discount_arg.product, apple)
        self.assertIn("5 for 3", discount_arg.description)
        self.assertLess(discount_arg.discount_amount, 0)


    def test_handle_ten_percent_discount(self):
        milk = Product("Milk", 2.0)
        cart = ShoppingCart()
        cart.add_item_quantity(milk, 2)

        offer = Offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, milk, 10)
        offers = {milk: offer}

        catalog = FakeCatalog()
        catalog.add_product(milk, 2.0)

        receipt = Mock()
        receipt.add_discount = Mock()

        cart.handle_offers(receipt, offers, catalog)

        receipt.add_discount.assert_called_once()

    def test_handle_offers_with_no_offer(self):
        cart = ShoppingCart()
        banana = Product("Banana", 0.5)
        cart.add_item_quantity(banana, 2)

        catalog = FakeCatalog()
        catalog.add_product(banana, 0.5)

        receipt = Mock()
        receipt.add_discount = Mock()

        cart.handle_offers(receipt, {}, catalog)

        receipt.add_discount.assert_not_called()

    

if __name__ == '__main__':  # pragma: no cover
    unittest.main()