import re

def additionner(a, b):
    """Verification des types"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"les nombres doivent être de type integer ou float")
    """Additionne deux nombres"""
    return a + b

def est_pair(nombre):
    """Vérifie si un nombre est pair"""
    return nombre % 2 == 0

def valider_email(email):
    """Valide un email simple (doit contenir @ et .)"""
    if "@" not in email and "." not in email:
        raise ValueError("Vous devez entrer une adresse mail valide contenant un . et un @")
    if "@" not in email:
        raise ValueError("Vous devez entrer une adresse mail valide contenant un @")
    if "." not in email:
        raise ValueError("Vous devez entrer une adresse mail valide contenant un .")
    return True

def calculer_moyenne(notes):
    """Calcule la moyenne d'une liste de notes"""
    if not isinstance(notes, (list, tuple)):
        raise TypeError("Les notes doivent être contenues dans une liste ou un tuple")
    """Calcule la moyenne d'une liste de notes"""
    if len(notes) == 0:
        return 0
    return sum(notes) / len(notes)

def convertir_temperature(celsius):
    """Convertit des degrés Celsius en Fahrenheit"""
    return (celsius * 9/5) + 32

def diviser(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"les nombres doivent être de type integer ou float")
    """Divise deux nombres et retourne le résultat"""
    return a / b

def mot_de_passe(mdp):
    """Si mot de passe fait plus de 8 caractère"""
    if len(mdp) >= 8 and re.search(r'[0-9]', mdp) :
        return True
    return False
