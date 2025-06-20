import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.fake_catalog import FakeCatalog
from model_objects import Product

def test_fake_catalog_add_and_price():
    catalog = FakeCatalog()
    apple = Product("apple", "each")
    catalog.add_product(apple, 100)
    
    assert catalog.unit_price(apple) == 100