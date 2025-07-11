import pytest
from datetime import datetime
from src.task_manager.task import Task, Priority, Status


class TestTaskCreation:
    """Tests de création de tâches"""

    def test_create_task_minimal_sets_defaults(self):
        """Test création tâche avec paramètres minimaux"""
        task = Task("Faire les courses")
        assert task.title == "Faire les courses"
        assert task.description == ""
        assert task.priority == Priority.MEDIUM
        assert task.status == Status.TODO
        assert isinstance(task.created_at, datetime)
        assert task.completed_at is None
        assert task.project_id is None
        assert isinstance(task.id, str)

    def test_create_task_complete_sets_all_fields(self):
        """Test création tâche avec tous les paramètres"""
        task = Task("Ranger bureau", description="Organiser les papiers", priority=Priority.HIGH)
        assert task.title == "Ranger bureau"
        assert task.description == "Organiser les papiers"
        assert task.priority == Priority.HIGH
        assert task.status == Status.TODO

    def test_create_task_empty_title_raises_error(self):
        """Test titre vide lève une erreur"""
        with pytest.raises(ValueError):
            Task("")

    def test_create_task_invalid_priority_raises_error(self):
        """Test priorité invalide lève une erreur"""
        with pytest.raises(ValueError):
            Task("Tâche invalide", priority="HAUTE")

class TestTaskOperations:
    """Tests des opérations sur les tâches"""

    def setup_method(self):
        """Fixture : tâche de test"""
        self.task = Task("Préparer le rapport", description="Analyse hebdo", priority=Priority.URGENT)

    def test_mark_completed_changes_status_and_sets_date(self):
        """Test marquage comme terminée"""
        self.task.mark_completed()
        assert self.task.status == Status.DONE
        assert isinstance(self.task.completed_at, datetime)

    def test_update_priority_valid_updates_priority(self):
        """Test mise à jour priorité valide"""
        self.task.update_priority(Priority.LOW)
        assert self.task.priority == Priority.LOW

    def test_update_priority_invalid_raises_error(self):
        """Test mise à jour priorité invalide"""
        with pytest.raises(ValueError):
            self.task.update_priority("BASSE")

    def test_assign_to_project_sets_project_id(self):
        """Test assignation à un projet"""
        self.task.assign_to_project("project-123")
        assert self.task.project_id == "project-123"


class TestTaskSerialization:
    """Tests de sérialisation JSON"""

    def setup_method(self):
        self.task = Task("Tâche complète", description="Tout est là", priority=Priority.HIGH)
        self.task.assign_to_project("proj-42")
        self.task.mark_completed()

    def test_to_dict_contains_all_fields_and_valid_types(self):
        """Test conversion en dictionnaire"""
        d = self.task.to_dict()
        assert d["id"] == self.task.id
        assert d["title"] == self.task.title
        assert d["priority"] == "HIGH"
        assert d["status"] == "DONE"
        assert isinstance(d["created_at"], str)
        assert isinstance(d["completed_at"], str)
        assert d["project_id"] == "proj-42"

    def test_from_dict_recreates_equivalent_task(self):
        """Test recréation depuis dictionnaire"""
        d = self.task.to_dict()
        new_task = Task.from_dict(d)
        assert new_task.id == self.task.id
        assert new_task.title == self.task.title
        assert new_task.priority == self.task.priority
        assert new_task.status == self.task.status
        assert new_task.created_at == self.task.created_at
        assert new_task.completed_at == self.task.completed_at
        assert new_task.project_id == self.task.project_id