import json
import os
from typing import List, Optional
from .task import Task, Priority, Status


class TaskManager:
    """Gestionnaire principal des tâches"""

    def __init__(self, storage_file="tasks.json"):
        self.tasks: List[Task] = []
        self.storage_file = storage_file

    def add_task(self, title, description="", priority=Priority.MEDIUM):
        task = Task(title, description, priority)
        self.tasks.append(task)
        return task.id

    def get_task(self, task_id) -> Optional[Task]:
        return next((t for t in self.tasks if t.id == task_id), None)

    def get_tasks_by_status(self, status: Status) -> List[Task]:
        return [t for t in self.tasks if t.status == status]

    def get_tasks_by_priority(self, priority: Priority) -> List[Task]:
        return [t for t in self.tasks if t.priority == priority]

    def delete_task(self, task_id) -> bool:
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def save_to_file(self, filename=None):
        file_to_use = filename or self.storage_file
        try:
            with open(file_to_use, "w", encoding="utf-8") as f:
                json.dump([t.to_dict() for t in self.tasks], f, indent=2)
        except IOError as e:
            print(f"Erreur lors de l'enregistrement : {e}")

    def load_from_file(self, filename=None):
        file_to_use = filename or self.storage_file
        if not os.path.exists(file_to_use):
            return

        try:
            with open(file_to_use, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(t) for t in data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Erreur de chargement : {e}")
            self.tasks = []

    def get_statistics(self):
        stats = {
            "total_tasks": len(self.tasks),
            "completed_tasks": len([t for t in self.tasks if t.status == Status.DONE]),
            "tasks_by_priority": {},
            "tasks_by_status": {},
        }

        for p in Priority:
            stats["tasks_by_priority"][p.name] = len(self.get_tasks_by_priority(p))

        for s in Status:
            stats["tasks_by_status"][s.name] = len(self.get_tasks_by_status(s))

        return stats