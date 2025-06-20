"""Calcul de remises"""
def remise(prix, pourcentage):
    """Verification des types"""
    if not isinstance(prix, (int, float)):
        raise TypeError(f"Le prix n'est pas un nombre")
    """Verification des types"""
    if not isinstance(pourcentage, (int, float)):
        raise TypeError(f"Le pourcentage n'est pas un nombre")
    """Prix supérieur à 0"""
    if (prix < 0):
        raise ValueError(f"Le prix doit être positif")
    """Pourcentage supérieur à 100"""
    if (pourcentage < 0 or pourcentage > 100):
        raise ValueError(f"Le pourcentage doit être compris entre 0 et 100")
    """Calcul du pourcentage deux nombres"""
    return prix - ((prix * pourcentage) / 100)
