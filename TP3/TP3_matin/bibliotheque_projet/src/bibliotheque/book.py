class Book:
    """Représente un livre dans la bibliothèque"""

    def __init__(self, title, author, isbn):
        # Initialisation des attributs
        self.title = title
        self.author = author
        self.isbn = isbn
        self._borrowed = False  
        
        # Validez que title et author sont non vides
        if not title or not author:
            raise ValueError("Le titre et l'auteur ne doivent pas être vides.")
        
        # Validez que isbn a exactement 13 caractères
        if len(isbn) != 13:
            raise ValueError("L'ISBN doit contenir exactement 13 caractères.")

    def is_available(self):
        """Retourne True si le livre n'est pas emprunté"""
        return not self._borrowed

    def borrow(self):
        """Marque le livre comme emprunté. Retourne True si succès, False si déjà emprunté."""
        if self._borrowed:
            return False
        self._borrowed = True
        return True

    def return_book(self):
        """Marque le livre comme disponible. Retourne True si succès, False si pas emprunté."""
        if not self._borrowed:
            return False
        self._borrowed = False
        return True