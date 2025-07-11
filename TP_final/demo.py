#!/usr/bin/env python3
"""
Démonstration du module TaskManager
"""

from src.task_manager.manager import TaskManager
from src.task_manager.task import Priority, Status
from src.task_manager.services import EmailService

def main():
    print("=== Démonstration TaskManager ===\n")

    # Crée un gestionnaire de tâches
    manager = TaskManager()

    # Ajoute plusieurs tâches avec différentes priorités
    id1 = manager.add_task("Faire les courses", "Acheter fruits et légumes", Priority.HIGH)
    id2 = manager.add_task("Préparer présentation", "Slides pour réunion lundi", Priority.MEDIUM)
    id3 = manager.add_task("Appeler client", "Discuter des délais", Priority.LOW)

    # Marque certaines tâches comme terminées (par exemple la 1ère)
    task1 = manager.get_task(id1)
    if task1:
        task1.status = Status.COMPLETED

    # Affiche les statistiques
    stats = manager.get_statistics()
    print("Statistiques :")
    for key, value in stats.items():
        print(f"  {key} : {value}")

    # Sauvegarde dans un fichier
    manager.save_to_file("demo_tasks.json")
    print("\nTâches sauvegardées dans demo_tasks.json")

    # Recharge depuis le fichier
    manager.load_from_file("demo_tasks.json")

    # Vérifie la recharge
    print(f"\nNombre de tâches rechargées : {len(manager.tasks)}")

    print("\nDémo terminée avec succès !")

if __name__ == "__main__":
    main()