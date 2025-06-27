class User:
    """Représente un utilisateur de la bibliothèque"""

    def __init__(self, name, email):

        self.name = name
        self.email = email
        self.borrowed_books = []
        # Validation du nom (non vide)
        if not name:
            raise ValueError("Le nom ne doit pas être vide.")
        
        # Validation de l'email (doit contenir '@')
        if '@' not in email:
            raise ValueError("L'email doit contenir '@'.")

    def can_borrow(self, max_books=3):
        """Retourne True si l'utilisateur peut emprunter un livre de plus"""
        return len(self.borrowed_books) < max_books

    def add_borrowed_book(self, book):
        """Ajoute un livre à la liste des emprunts si autorisé"""
        if not self.can_borrow():
            raise ValueError("Limite d'emprunts atteinte.")
        self.borrowed_books.append(book)

    def remove_borrowed_book(self, book):
        """Retire un livre de la liste des emprunts"""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)