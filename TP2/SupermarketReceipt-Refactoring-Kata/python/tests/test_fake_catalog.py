import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from tests.fake_catalog import FakeCatalog
from model_objects import Product

def test_add_product_and_unit_price():
    catalog = FakeCatalog()
    apple = Product("apple", "each")
    banana = Product("banana", "each")
    
    # Ajout des produits
    catalog.add_product(apple, 100)
    catalog.add_product(banana, 200)
    
    # Vérification des prix
    assert catalog.unit_price(apple) == 100
    assert catalog.unit_price(banana) == 200

def test_unit_price_for_unknown_product_raises():
    catalog = FakeCatalog()
    orange = Product("orange", "each")
    
    # Pas ajouté dans le catalogue, doit lever une erreur
    with pytest.raises(KeyError):
        catalog.unit_price(orange)