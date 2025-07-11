### Phase 1 : Analyse et conception

Questions d'analyse :

1. Quelles sont les entités principales ? (Tâche, Projet, Gestionnaire)
   --> Il y a en tout 3 entitiés principales : task (la tâche individuelle), project (regroupe plusieurs tâches), et manager (qui gère les différentes opérations CRUD).
2. Quelles dépendances externes identifiez-vous ?
   --> J'identifie Github Actions pour le déploiement continu, pytest et pytest-mock pour les tests, pytest-cov et coverage pour la visualisation de la couverture.
3. Quels cas d'erreur faut-il prévoir ?
   --> Cas d'erreurs sur la création et la modification d'une tâche (ex: champs obligatoires manquants, priorité invalide,...) ;
   --> Cas d'erreurs sur la suppression d'une tâche (ex: tâche non trouvée, tâche déjà supprimée,...)
   --> Cas d'erreurs lors de l'organisation en projet (ex: projet inexistant, tâche déjà existante dans le projet,...)
   --> Cas d'erreurs lorsqu'une tâche est marquée comme terminée (ex: tâche inexistante,...)
   --> Cas d'erreurs lors de la sauvegarde (ex: fichier introuvable, fichier vide,...)
   --> Cas d'erreurs lors de la confection des statistiques (aucune tâche,...)
   --> Cas d'erreurs lors de l'envoi des notifications (ex: données incomplètes ou manquantes,...)
4. Comment organiser le code pour faciliter les tests ?
   --> Avoir d'un côté les fonctionnalités organisées dans un dossier spécifique, et d'un autre côté un dossier qui regroupe les fichiers de tests et qui reprend la structure du dossier de fonctionnalités pour avoir un parallèlisme.

Définissez les noms des fichiers et justifiez vos choix :
--> J'ai choisi d'appeler mes fichiers task.py, manager.py et services.py car ce sont des noms clairs, qui permettent en une seule lecture de comprendre leur rôle dans le projet. Au niveau des fichiers de tests, j'ai choisi de les appeler test_task.py, test_manager.py et test_services.py car ces noms sont clairs et permettent de faire rapidement le lien entre les fichiers sources dont nous avons parlé juste avant, et leurs fichiers de tests respectifs. L'architecture est ainsi structurées, lisible, et on comprend directement l'utilité et le rôle des fichiers sans avoir besoin d'aller chercher à l'intérieur ce qu'ils font.
