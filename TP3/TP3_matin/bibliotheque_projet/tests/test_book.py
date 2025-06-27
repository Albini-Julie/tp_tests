import pytest
from src.bibliotheque.book import Book

# ---------- FIXTURES ----------
@pytest.fixture
def valid_isbn():
    return "1234567890123"

@pytest.fixture
def valid_book(valid_isbn):
    return Book("Le Petit Prince", "Antoine de Saint-Exupéry", valid_isbn)

@pytest.fixture
def borrowed_book(valid_book):
    valid_book.borrow()
    return valid_book

# ---------- TESTS DE CRÉATION ----------
class TestBookCreation:

    def test_create_valid_book(self, valid_book):
        """Test création livre valide"""
        assert valid_book.title == "Le Petit Prince"
        assert valid_book.author == "Antoine de Saint-Exupéry"
        assert valid_book.isbn == "1234567890123"
        assert valid_book.is_available() is True

    def test_create_book_empty_title_raises_error(self, valid_isbn):
        """Test titre vide lève une erreur"""
        with pytest.raises(ValueError, match="titre.*auteur.*vides"):
            Book("", "Auteur", valid_isbn)

    def test_create_book_invalid_isbn_raises_error(self):
        """Test ISBN invalide lève une erreur"""
        with pytest.raises(ValueError, match="ISBN.*13 caractères"):
            Book("Titre", "Auteur", "123")
        with pytest.raises(ValueError, match="ISBN.*13 caractères"):
            Book("Titre", "Auteur", "12345678901234")

# ---------- TESTS D'EMPRUNT ----------
class TestBookBorrowing:

    def test_new_book_is_available(self, valid_book):
        """Test livre neuf disponible"""
        assert valid_book.is_available() is True

    def test_borrow_available_book_success(self, valid_book):
        """Test emprunt livre disponible"""
        success = valid_book.borrow()
        assert success is True
        assert valid_book.is_available() is False

    def test_borrow_already_borrowed_book_fails(self, borrowed_book):
        """Test emprunt livre déjà emprunté"""
        second_attempt = borrowed_book.borrow()
        assert second_attempt is False

    def test_return_book_not_borrowed_fails(self, valid_book):
        """Test retour livre non emprunté"""
        assert valid_book.return_book() is False

    def test_return_borrowed_book_success(self, borrowed_book):
        """Test retour livre emprunté"""
        result = borrowed_book.return_book()
        assert result is True
        assert borrowed_book.is_available() is True