import unittest
from model_objects import Product
from receipt import Receipt, ReceiptItem

class TestReceipt(unittest.TestCase):

    def setUp(self):
        self.receipt = Receipt()
        self.apple = Product("Apple", 1.0)

    def test_add_product_and_items_property(self):
        self.receipt.add_product(self.apple, 2, 1.0, 2.0)
        items = self.receipt.items
        self.assertEqual(len(items), 1)
        item = items[0]
        self.assertEqual(item.product, self.apple)
        self.assertEqual(item.quantity, 2)
        self.assertEqual(item.price, 1.0)
        self.assertEqual(item.total_price, 2.0)

    def test_add_discount_and_discounts_property(self):
        class DummyDiscount:
            def __init__(self):
                self.discount_amount = -0.5

        discount = DummyDiscount()
        self.receipt.add_discount(discount)
        discounts = self.receipt.discounts
        self.assertEqual(len(discounts), 1)
        self.assertIs(discounts[0], discount)

    def test_total_price_calculation(self):
        self.receipt.add_product(self.apple, 3, 1.0, 3.0)
        class DummyDiscount:
            def __init__(self):
                self.discount_amount = -1.0
        discount = DummyDiscount()
        self.receipt.add_discount(discount)

        total = self.receipt.total_price()
        self.assertEqual(total, 3.0 - 1.0)

    def test_items_and_discounts_are_copies(self):
        self.receipt.add_product(self.apple, 1, 1.0, 1.0)
        self.receipt.add_discount(type('D', (), {'discount_amount': -0.1})())

        items_copy = self.receipt.items
        discounts_copy = self.receipt.discounts

        items_copy.append('fake')
        discounts_copy.append('fake')

        self.assertEqual(len(self.receipt.items), 1)
        self.assertEqual(len(self.receipt.discounts), 1)

if __name__ == '__main__':
    unittest.main()