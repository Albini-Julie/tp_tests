from fonctions import additionner, est_pair, valider_email, calculer_moyenne, convertir_temperature, diviser, mot de passe

def test_additionner_cas_positif():
    """Test addition avec nombres positifs"""
    resultat = additionner(2, 3)
    assert resultat == 5
def test_additionner_cas_negatif():
    """Test addition avec nombres négatifs"""
    resultat = additionner(-2, -3)
    assert resultat == -5

def test_est_pair_nombre_pair():
    """Test avec un nombre pair"""
    assert est_pair(4) == True
def test_est_pair_nombre_impair():
    """Test avec un nombre impair"""
    assert est_pair(3) == False
def test_est_pair_zero():
    """Test avec zéro"""
    assert est_pair(0) == True

def test_valider_email_valide():
    """Test avec un email valide"""
    assert valider_email("test@example.com") == True
def test_valider_email_sans_arobase():
    """Test avec un email sans @"""
    assert valider_email("testexample.com") == False
def test_valider_email_sans_point():
    """Test avec un email sans point"""
    assert valider_email("test@example") == False
def test_calculer_moyenne_liste_normale():
    """Test avec une liste de notes normales"""
    assert calculer_moyenne([10,15,20]) == 15
def test_calculer_moyenne_liste_vide():
    """Test avec une liste vide"""
    assert calculer_moyenne([]) == 0
def test_calculer_moyenne_une_note():
    """Test avec une seule note"""
    assert calculer_moyenne([18]) == 18
def test_convertir_temperature_zero():
    """Test conversion 0°C = 32°F"""
    assert convertir_temperature(0) == 32
def test_convertir_temperature_eau_bouillante():
    """Test conversion 100°C = 212°F"""
    assert convertir_temperature(100) == 212
def test_diviser_reussi():
    """Test 12 / 6 doit retourner 2"""
    assert diviser(12, 6) == 2
def test_diviser_zero():
    """Test 12 / 6 doit retourner 2"""
    with pytest.raises(ZeroDivisionError):
        diviser(10, 0)
def test_motdepasse_ok():
    """test avec 'Coucoutoi2'"""
    assert mot_de_passe("Coucoutoi2")
def test_motdepasse_sanschiffre():
    """test avec 'Coucoutoi'"""
    assert mot_de_passe("Coucoutoi")
def test_motdepasse_moins8():
    """test avec 'Coucouto'"""
    assert mot_de_passe("Coucouto")