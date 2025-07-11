import pytest
from unittest.mock import mock_open, patch
import json

from src.task_manager.manager import TaskManager
from src.task_manager.task import Priority, Status


class TestTaskManagerBasics:
    """Tests basiques du gestionnaire"""

    def setup_method(self):
        """Fixture : gestionnaire de test"""
        self.manager = TaskManager("test_tasks.json")

    def test_add_task_returns_id_and_stores_task(self):
        """Test ajout tâche retourne un ID"""
        task_id = self.manager.add_task("Tâche simple", "Description", Priority.LOW)
        assert task_id is not None
        task = self.manager.get_task(task_id)
        assert task is not None
        assert task.title == "Tâche simple"
        assert task.priority == Priority.LOW

    def test_get_task_existing(self):
        """Test récupération tâche existante"""
        task_id = self.manager.add_task("Lire un livre")
        task = self.manager.get_task(task_id)
        assert task.title == "Lire un livre"
        assert task.status == Status.TODO

    def test_get_task_nonexistent_returns_none(self):
        """Test récupération tâche inexistante"""
        assert self.manager.get_task("non-existent-id") is None


class TestTaskManagerFiltering:
    """Tests de filtrage des tâches"""

    def setup_method(self):
        """Fixture : gestionnaire avec plusieurs tâches"""
        self.manager = TaskManager("test_tasks.json")
        # Créer 4 tâches avec différents statuts/priorités
        self.id1 = self.manager.add_task("Tâche A", priority=Priority.HIGH)
        self.id2 = self.manager.add_task("Tâche B", priority=Priority.MEDIUM)
        self.id3 = self.manager.add_task("Tâche C", priority=Priority.HIGH)
        self.id4 = self.manager.add_task("Tâche D", priority=Priority.LOW)

        self.manager.get_task(self.id1).mark_completed()
        self.manager.get_task(self.id3).status = Status.IN_PROGRESS

    def test_get_tasks_by_status(self):
        """Test filtrage par statut"""
        todos = self.manager.get_tasks_by_status(Status.TODO)
        assert len(todos) == 2
        assert all(task.status == Status.TODO for task in todos)

    def test_get_tasks_by_priority(self):
        """Test filtrage par priorité"""
        high_priority = self.manager.get_tasks_by_priority(Priority.HIGH)
        assert len(high_priority) == 2
        titles = [task.title for task in high_priority]
        assert "Tâche A" in titles and "Tâche C" in titles


class TestTaskManagerPersistence:
    """Tests de sauvegarde/chargement avec mocks"""

    def setup_method(self):
        self.manager = TaskManager("test_tasks.json")
        self.manager.add_task("À sauvegarder", priority=Priority.HIGH)

    @patch('builtins.open', new_callable=mock_open)
    @patch('json.dump')
    def test_save_to_file_success(self, mock_json_dump, mock_file):
        """Test sauvegarde réussie"""
        self.manager.save_to_file()
        mock_file.assert_called_once_with("test_tasks.json", "w", encoding="utf-8")
        assert mock_json_dump.called

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data='[{"id": "t1", "title": "Mock Task", "description": "", "priority": "MEDIUM", "status": "TODO", "created_at": "2025-07-11T10:00:00", "completed_at": null, "project_id": null}]')
    def test_load_from_file_success(self, mock_file, mock_exists):
        """Test chargement réussi"""
        manager = TaskManager("test_tasks.json")
        manager.load_from_file()
        
        assert len(manager.tasks) == 1
        assert manager.tasks[0].title == "Mock Task"

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_load_from_nonexistent_file(self, mock_file):
        """Test chargement fichier inexistant"""
        manager = TaskManager("test_tasks.json")
        manager.load_from_file()
        assert len(manager.tasks) == 0

## Pour atteindre la couverture

def test_add_task_invalid_title_raises():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add_task("") 
    with pytest.raises(ValueError):
        manager.add_task(None)  


@patch('builtins.open', new_callable=mock_open)
def test_save_to_file_ioerror(mock_file):
    manager = TaskManager()
    manager.add_task("Titre valide")
    mock_file.side_effect = IOError("Erreur écriture")
    with patch('json.dump') as mock_json_dump:
        manager.save_to_file()



@patch('builtins.open', new_callable=mock_open, read_data='not a json')
def test_load_from_file_jsondecodeerror(mock_file):
    manager = TaskManager()
    with patch('json.load', side_effect=json.JSONDecodeError("msg", "doc", 0)):
        manager.load_from_file()

    assert manager.tasks == []


def test_get_tasks_by_status_empty():
    manager = TaskManager()
    assert manager.get_tasks_by_status(Status.TODO) == []


def test_get_tasks_by_priority_empty():
    manager = TaskManager()
    assert manager.get_tasks_by_priority(Priority.HIGH) == []


def test_get_statistics_empty_and_nonempty():
    manager = TaskManager()
    stats = manager.get_statistics()
    assert stats['total_tasks'] == 0
    assert stats['completed_tasks'] == 0
    for p in Priority:
        assert stats['tasks_by_priority'][p.name] == 0
    for s in Status:
        assert stats['tasks_by_status'][s.name] == 0

    tid = manager.add_task("Tâche 1", priority=Priority.HIGH)
    task = manager.get_task(tid)
    task.mark_completed()
    tid2 = manager.add_task("Tâche 2", priority=Priority.LOW)
    stats = manager.get_statistics()
    assert stats['total_tasks'] == 2
    assert stats['completed_tasks'] == 1
    assert stats['tasks_by_priority'][Priority.HIGH.name] == 1
    assert stats['tasks_by_priority'][Priority.LOW.name] == 1

def test_add_task_invalid_title_raises():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add_task("")  
    with pytest.raises(ValueError):
        manager.add_task(None)  


def test_delete_task_nonexistent_returns_false():
    manager = TaskManager()
    result = manager.delete_task("id-inexistant")
    assert result is False