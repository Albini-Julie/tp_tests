import unittest
from unittest.mock import Mock
from model_objects import Product, SpecialOfferType
from tests.fake_catalog import FakeCatalog
from teller import Teller
from shopping_cart import ShoppingCart

class TestTeller(unittest.TestCase):

    def test_add_special_offer_and_checkout(self):
        catalog = FakeCatalog()
        apple = Product("Apple", 1.0)
        catalog.add_product(apple, 1.0)

        cart = ShoppingCart()
        cart.add_item_quantity(apple, 3)

        teller = Teller(catalog)
        # Ajouter une offre spéciale (ex : 3 pour 2)
        teller.add_special_offer(SpecialOfferType.THREE_FOR_TWO, apple, 0)

        receipt = teller.checks_out_articles_from(cart)

        # On vérifie que le ticket contient bien l'article
        self.assertEqual(len(receipt.items), 1)
        self.assertEqual(receipt.items[0].product, apple)
        self.assertEqual(receipt.items[0].quantity, 3)

        # On vérifie qu'au moins une réduction a été appliquée
        self.assertTrue(len(receipt.discounts) > 0)

    def test_checkout_without_offers(self):
        catalog = FakeCatalog()
        banana = Product("Banana", 0.5)
        catalog.add_product(banana, 0.5)

        cart = ShoppingCart()
        cart.add_item_quantity(banana, 2)

        teller = Teller(catalog)

        receipt = teller.checks_out_articles_from(cart)

        self.assertEqual(len(receipt.items), 1)
        self.assertEqual(len(receipt.discounts), 0)
        self.assertEqual(receipt.items[0].product, banana)
        self.assertEqual(receipt.items[0].quantity, 2)

if __name__ == "__main__":
    unittest.main()