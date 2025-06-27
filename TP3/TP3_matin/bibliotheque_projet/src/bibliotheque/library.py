from .book import Book
from .user import User

class Library:
    """Gestionnaire de bibliothèque"""

    def __init__(self, name):
        # Initialisation du nom et d'une collection vide
        self.name = name
        self.collections = [] 

    def add_book(self, book):
        """Ajoute un livre à la collection"""
        if isinstance(book, Book):
            self.collections.append(book)
        else:
            raise TypeError("Seuls les objets de type Book peuvent être ajoutés.")

    def find_book_by_isbn(self, isbn):
        """Retourne un livre correspondant à l'ISBN, ou None si non trouvé"""
        for book in self.collections:
            if book.isbn == isbn:
                return book
        return None

    def borrow_book(self, user, isbn):
        """
        Gère l'emprunt :
        1. Trouve le livre
        2. Vérifie que l'utilisateur peut emprunter
        3. Vérifie que le livre est disponible
        4. Marque comme emprunté et ajoute à l'utilisateur
        """
        book = self.find_book_by_isbn(isbn)
        if not book:
            return False

        if not user.can_borrow():
            return False

        if not book.is_available():
            return False

        if book.borrow():
            user.add_borrowed_book(book)
            return True
        return False