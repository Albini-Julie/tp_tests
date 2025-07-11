import re
import csv
from datetime import datetime
from typing import List
from .task import Task
from src.task_manager.task import Status


class EmailService:
    """Service d'envoi d'emails (à mocker dans les tests)"""

    def __init__(self, smtp_server="smtp.gmail.com", port=587):
        self.smtp_server = smtp_server
        self.port = port

    def _is_valid_email(self, email: str) -> bool:
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def send_task_reminder(self, email: str, task_title: str, due_date: datetime):
        if not self._is_valid_email(email):
            raise ValueError("Adresse email invalide.")

        print(f"[SIMULATION] Envoi d'un rappel à {email} pour la tâche '{task_title}' (à faire avant {due_date}).")
        return True

    def send_completion_notification(self, email: str, task_title: str):
        if not self._is_valid_email(email):
            raise ValueError("Adresse email invalide.")

        print(f"[SIMULATION] Notification de complétion envoyée à {email} pour la tâche '{task_title}'.")
        return True


class ReportService:
    """Service de génération de rapports"""

    def generate_daily_report(self, tasks: List[Task], date=None):
        date = date or datetime.now().date()
        date_str = date.isoformat()

        completed_today = [
            t for t in tasks
            if t.completed_at and t.completed_at.date() == date
        ]

        return {
            "date": datetime.now().date().isoformat(),
            "tasks": [t.to_dict() for t in tasks],
            "total_tasks": len(tasks),
            "total_completed": len([t for t in tasks if t.status == Status.COMPLETED])
        }

    def export_tasks_csv(self, tasks: List[Task], filename: str):
        try:
            with open(filename, mode="w", encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=[
                        "id", "title", "description", "priority", "status",
                        "created_at", "completed_at", "project_id"
                    ]
                )
                writer.writeheader()
                for task in tasks:
                    writer.writerow(task.to_dict())
        except IOError as e:
            print(f"Erreur lors de l'export CSV : {e}")