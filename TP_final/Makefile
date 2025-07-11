.PHONY: install test test-unit test-integration coverage clean lint all

# Installer les dépendances
install:
	pip install -r requirements.txt

# Lancer tous les tests
test:
	pytest

# Lancer uniquement les tests unitaires
test-unit:
	pytest -k "unit"

# Lancer uniquement les tests d'intégration
test-integration:
	pytest -k "integration"

# Générer le rapport de couverture HTML
coverage:
	pytest --cov=src --cov-report=html

# Nettoyer les fichiers temporaires
clean:
	rm -rf __pycache__ .pytest_cache .coverage htmlcov

# Vérification syntaxique (linting)
lint:
	python -m py_compile $(shell find src tests -name "*.py")

# Tout exécuter
all: clean install lint test coverage