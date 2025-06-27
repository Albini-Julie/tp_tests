import pytest
from src.bibliotheque.library import Library
from src.bibliotheque.book import Book
from src.bibliotheque.user import User

# ---------- FIXTURES ----------
@pytest.fixture
def books():
    return [
        Book("Livre A", "Auteur 1", "0000000000001"),
        Book("Livre B", "Auteur 2", "0000000000002"),
        Book("Livre C", "Auteur 3", "0000000000003"),
        Book("Livre D", "Auteur 4", "0000000000004"),
    ]

@pytest.fixture
def users():
    return [
        User("Alice", "alice@example.com"),
        User("Bob", "bob@example.com"),
    ]

@pytest.fixture
def library(books):
    lib = Library("Bibliothèque Centrale")
    for book in books:
        lib.add_book(book)
    return lib

# ---------- TESTS ----------
def test_borrow_flow_success(library, users, books):
    """Test flux complet d'emprunt réussi"""
    user1 = users[0]
    book1 = books[0]

    success = library.borrow_book(user1, book1.isbn)

    assert success is True
    assert book1.is_available() is False
    assert book1 in user1.borrowed_books

def test_user_cannot_borrow_more_than_limit(library, users, books):
    """Test limite d'emprunts par utilisateur"""
    user2 = users[1]

    library.borrow_book(user2, books[0].isbn)
    library.borrow_book(user2, books[1].isbn)
    library.borrow_book(user2, books[2].isbn)

    result = library.borrow_book(user2, books[3].isbn)
    assert result is False
    assert books[3].is_available() is True