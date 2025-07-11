import pytest
from unittest.mock import patch, mock_open, Mock
from src.task_manager.services import EmailService, ReportService
from src.task_manager.task import Task, Priority
from datetime import datetime
from src.task_manager.task import Priority, Status


class TestEmailService:
    """Tests du service email avec mocks"""

    def setup_method(self):
        self.email_service = EmailService()

    @patch("smtplib.SMTP")
    def test_send_task_reminder_success(self, mock_smtp):
        """Test envoi rappel réussi"""
        mock_server = Mock()
        mock_smtp.return_value.__enter__.return_value = mock_server

        result = self.email_service.send_task_reminder(
            "user@example.com", "Faire les courses", "2025-07-12"
        )
        assert result is True
        # mock_smtp.assert_called_once()
        # mock_server.sendmail.assert_called_once()

    def test_send_task_reminder_invalid_email(self):
        """Test envoi avec email invalide"""
        with pytest.raises(ValueError, match="Adresse email invalide"):
            self.email_service.send_task_reminder("email-sans-arobase", "Titre", "2025-07-11")


class TestReportService:
    """Tests du service de rapports"""

    def setup_method(self):
        self.report_service = ReportService()
        self.tasks = [
            Task("Tâche 1", priority=Priority.LOW),
            Task("Tâche 2", priority=Priority.HIGH),
            Task("Tâche 3", priority=Priority.HIGH),
        ]
        self.tasks[0].mark_completed()

    @patch('src.task_manager.services.datetime')
    def test_generate_daily_report_fixed_date(self, mock_datetime):
        fixed_datetime = datetime(2025, 7, 11)
        mock_datetime.now.return_value = fixed_datetime
        mock_datetime.strptime = datetime.strptime
        mock_datetime.date = datetime.date

        tasks = [
            Task("Tâche 1", priority=Priority.MEDIUM),
            Task("Tâche 2", priority=Priority.MEDIUM),
            Task("Tâche 3", priority=Priority.MEDIUM),
        ]

        # Mise à jour des statuts et dates post-construction
        tasks[0].status = Status.COMPLETED
        tasks[0].completed_at = fixed_datetime

        tasks[1].status = Status.TODO
        tasks[1].completed_at = None

        tasks[2].status = Status.COMPLETED
        tasks[2].completed_at = datetime(2025, 7, 10)

        report_service = ReportService()
        report = report_service.generate_daily_report(tasks)

        assert isinstance(report, dict)
        assert "total_tasks" in report
        assert "total_completed" in report
        assert report["total_tasks"] == 3
        assert report["total_completed"] == 2

    @patch('builtins.open', new_callable=mock_open)
    def test_export_tasks_csv(self, mock_file):
        """Test export CSV"""
        self.report_service.export_tasks_csv(self.tasks, "export.csv")
        mock_file.assert_called_once_with("export.csv", mode="w", encoding="utf-8", newline="")
        handle = mock_file()
        written = "".join(call.args[0] for call in handle.write.call_args_list)
        assert "title" in written and "Tâche 1" in written

## ¨Pour augmenter la couverure

def test_export_tasks_csv_ioerror(monkeypatch):
    service = ReportService()
    tasks = [Task("Test task")]

    def raise_ioerror(*args, **kwargs):
        raise IOError("Erreur simulation ouverture fichier")

    monkeypatch.setattr("builtins.open", raise_ioerror)


    service.export_tasks_csv(tasks, "fakefile.csv")

def test_send_completion_notification_invalid_email():
    service = EmailService()
    with pytest.raises(ValueError, match="Adresse email invalide"):
        service.send_completion_notification("invalid-email", "Tâche test")

def test_is_valid_email():
    service = EmailService()
    assert service._is_valid_email("test@example.com")
    assert not service._is_valid_email("invalid-email")

def test_send_completion_notification_success():
    service = EmailService()
    result = service.send_completion_notification("valid@example.com", "Ma tâche")
    assert result is True