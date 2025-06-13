import unittest
from fonctions import remise
class TestFonctions(unittest.TestCase):

    def test_remise_ok(self):
        """Test positif est 20 et 50%"""
        self.assertEqual(remise(20, 50), 10)
    
    def test_remise_ok_0(self):
        """Test positif est 20 et 0%"""
        self.assertEqual(remise(20, 0), 20)
    
    def test_remise_ok_100(self):
        """Test positif est 20 et 100%"""
        self.assertEqual(remise(20, 100), 0)
    
    def test_remise_prix_string(self):
        """Test négatif car prix string et 50%"""
        with self.assertRaises(TypeError) as context:
            remise('coucou', 50)
        self.assertEqual(str(context.exception), "Le prix n'est pas un nombre")
    
    def test_remise_pourcentage_string(self):
        """Test négatif car 20 et coucou"""
        with self.assertRaises(TypeError) as context:
            remise(20, 'coucou')
        self.assertEqual(str(context.exception), "Le pourcentage n'est pas un nombre")
    
    def test_remise_prix_negatif(self):
        """Test négatif car prix négatif : -20 et 50%"""
        with self.assertRaises(ValueError) as context:
            remise(-20, 50)
        self.assertEqual(str(context.exception), "Le prix doit être positif")
    
    def test_remise_pourcentage_negatif(self):
        """Test négatif car pourcentage négatif 20 et -50%"""
        with self.assertRaises(ValueError) as context:
            remise(20, -50)
        self.assertEqual(str(context.exception), "Le pourcentage doit être compris entre 0 et 100")
    
    def test_remise_pourcentage_plus_de_100(self):
        """Test négatif car pourcentage négatif 20 et 101"""
        with self.assertRaises(ValueError) as context:
            remise(20, 101)
        self.assertEqual(str(context.exception), "Le pourcentage doit être compris entre 0 et 100")


if __name__ == '__main__':
 unittest.main()