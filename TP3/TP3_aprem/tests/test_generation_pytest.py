import pytest
from approvaltests import verify
from src.generation import generation

# ------------------ TESTS VALIDES ------------------

def test_generation_email_valide():
    """Test generation d'email valide avec toutes les informations"""
    message = generation("Julie", "Albini", "Montbeliard", "julie.albini@ynov.com")
    assert message == (
        "Bonjour Julie Albini de Montbeliard, votre inscription a bien ete prise en compte a l'addresse mail suivante : julie.albini@ynov.com"
    )

# ------------------ ERREURS AVANT LE @ ------------------

def test_generation_email_pas_prenom():
    with pytest.raises(ValueError, match="prenom"):
        generation("", "Albini", "Montbeliard", "julie.albini@ynov.com")

def test_generation_email_pas_nom():
    with pytest.raises(ValueError, match="nom"):
        generation("Julie", "", "Montbeliard", "julie.albini@ynov.com")

def test_generation_email_pas_ville():
    with pytest.raises(ValueError, match="ville"):
        generation("Julie", "Albini", "", "julie.albini@ynov.com")

def test_generation_email_pas_email():
    with pytest.raises(ValueError, match="email"):
        generation("Julie", "Albini", "Montbeliard", "")

def test_generation_email_sans_arobase():
    with pytest.raises(ValueError, match="email valide contenant un @"):
        generation("Julie", "Albini", "Montbeliard", "julie.albinynov.com")

def test_generation_email_deux_points_consecutifs():
    with pytest.raises(ValueError, match="deux \. consecutifs"):
        generation("Julie", "Albini", "Montbeliard", "julie..albini@ynov.com")

def test_generation_email_commence_par_point():
    with pytest.raises(ValueError, match="ne peut pas commencer pas un point"):
        generation("Julie", "Albini", "Montbeliard", ".julie.albini@ynov.com")

def test_generation_email_termine_par_point():
    with pytest.raises(ValueError, match="ne peut pas se terminer pas un point"):
        generation("Julie", "Albini", "Montbeliard", "julie.albini.@ynov.com")

def test_generation_email_plus_de_64_avant_arobase():
    email = "julie.albini" + "x" * 55 + "@ynov.com"  # 65+ caractères avant le @
    with pytest.raises(ValueError, match="plus de 64 caractères"):
        generation("Julie", "Albini", "Montbeliard", email)

# ------------------ ERREURS APRÈS LE @ ------------------

def test_generation_email_sans_point_domaine():
    with pytest.raises(ValueError, match="nom de domaine valide contenant un \."):
        generation("Julie", "Albini", "Montbeliard", "julie.albini@ynovcom")

def test_generation_email_deux_points_domaine():
    with pytest.raises(ValueError, match="domaine valide ne contenant pas deux \."):
        generation("Julie", "Albini", "Montbeliard", "julie.albini@ynov..com")

def test_generation_email_point_debut_domaine():
    with pytest.raises(ValueError, match="nom de domaine ne peut pas commencer pas un point"):
        generation("Julie", "Albini", "Montbeliard", "julie.albini@.ynov.com")

def test_generation_email_point_fin_domaine():
    with pytest.raises(ValueError, match="nom de domaine ne peut pas se terminer pas un point"):
        generation("Julie", "Albini", "Montbeliard", "julie.albini@ynov.com.")

def test_generation_email_plus_de_64_domaine():
    domaine = "ynov.com" + "x" * 60  # 67 caractères après le @
    email = f"julie.albini@{domaine}"
    with pytest.raises(ValueError, match="domaine ne peut pas faire plus de 64 caractères"):
        generation("Julie", "Albini", "Montbeliard", email)


# APPROVAL    
def test_generation_email_valide_approval():
    message = generation("Julie", "Albini", "Montbeliard", "julie.albini@ynov.com")
    verify(message)