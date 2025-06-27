import pytest
from src.bibliotheque.user import User
from src.bibliotheque.book import Book

# ---------- FIXTURES ----------
@pytest.fixture
def valid_user():
    return User("Bob", "bob@example.com")

@pytest.fixture
def valid_book():
    return Book("Titre", "Auteur", "1234567890123")

# ---------- TESTS ----------

def test_user_init_invalid_email():
    with pytest.raises(ValueError):
        User("Bob", "bobatexample.com") 

def test_user_init_empty_name():
    with pytest.raises(ValueError):
        User("", "bob@example.com")

def test_can_borrow_true_and_false(valid_user, valid_book):
    valid_user.borrowed_books = []
    assert valid_user.can_borrow() is True

    valid_user.borrowed_books = [valid_book] * 3
    assert valid_user.can_borrow() is False

def test_add_and_remove_borrowed_book(valid_user, valid_book):
    valid_user.borrowed_books = []
    
    valid_user.add_borrowed_book(valid_book)
    assert valid_book in valid_user.borrowed_books

    valid_user.remove_borrowed_book(valid_book)
    assert valid_book not in valid_user.borrowed_books