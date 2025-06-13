import unittest
from fonctions import additionner, est_pair, valider_email, calculer_moyenne, convertir_temperature, diviser, mot_de_passe
class TestFonctions(unittest.TestCase):

    def test_additionner_cas_positif(self):
        """Test addition avec nombres positifs"""
        resultat = additionner(2, 3)
        self.assertEqual(resultat, 5)

    def test_additionner_cas_negatif(self):
        """Test addition avec nombres négatifs"""
        resultat = additionner(-2, -3)
        self.assertEqual(resultat, -5)

    def test_est_pair_nombre_pair(self):
        """Test avec un nombre pair"""
        self.assertTrue(est_pair(4))

    def test_est_pair_nombre_impair(self):
        """Test avec un nombre impair"""
        self.assertFalse(est_pair(3))

    def test_est_pair_zero(self):
        """Test avec zéro"""
        self.assertTrue(est_pair(0))

    def test_valider_email_valide(self):
        """Test avec un email valide"""
        self.assertTrue(valider_email("test@example.com"))

    def test_valider_email_sans_arobase(self):
        """Test avec un email sans @"""
        self.assertFalse(valider_email("testexample.com"))
    
    def test_valider_email_sans_point(self):
        """Test avec un email sans point"""
        self.assertFalse(valider_email("test@example"))
    
    def test_calculer_moyenne_liste_normale(self):
        """Test avec une liste de notes normales"""
        self.assertEqual(calculer_moyenne([10,15,20]), 15)
    
    def test_calculer_moyenne_liste_vide(self):
        """Test avec une liste vide"""
        self.assertFalse(calculer_moyenne([]), 0)
    
    def test_calculer_moyenne_une_note(self):
        self.assertEqual(calculer_moyenne([18]), 18)

    def test_convertir_temperature_zero(self):
        """Test conversion 0°C = 32°F"""
        self.assertEqual(convertir_temperature(0), 32)
    
    def test_convertir_temperature_eau_bouillante(self):
        """Test conversion 100°C = 212°F"""
        self.assertTrue(convertir_temperature(100), 212)

    def test_diviser_reussi(self):
        """Test 12 / 6 doit retourner 2"""
        self.assertEqual(diviser(12, 6), 2)

    def test_diviser_parzero(self):
        """Division par zéro doit lever une erreur"""
        with self.assertRaises(ZeroDivisionError):
            diviser(12, 0)


 # À COMPLÉTER : Ajoutez vos tests ici
# Permet d'exécuter les tests
if __name__ == '__main__':
 unittest.main()