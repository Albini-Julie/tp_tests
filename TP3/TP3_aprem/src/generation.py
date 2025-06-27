def generation(prenom, nom, ville, email):
    if not prenom:
        raise ValueError("Vous devez entrer un prénom")
    if not nom:
        raise ValueError("Vous devez entrer un nom")
    if not ville:
        raise ValueError("Vous devez entrer une ville")
    if not email:
        raise ValueError("Vous devez entrer un email")

    if "@" not in email:
        raise ValueError("Vous devez entrer un email valide contenant un @")

    local, sep, domaine = email.partition("@")

    if ".." in local:
        raise ValueError("Vous devez entrer un email valide ne contenant pas deux . consécutifs")
    if local.startswith("."):
        raise ValueError("L'email ne peut pas commencer pas un point")
    if local.endswith("."):
        raise ValueError("L'email ne peut pas se terminer pas un point")
    if len(local) > 64:
        raise ValueError("L'email ne peut pas faire plus de 64 caractères")

    if "." not in domaine:
        raise ValueError("Vous devez entrer un nom de domaine valide contenant un .")
    if ".." in domaine:
        raise ValueError("Vous devez entrer un nom de domaine valide ne contenant pas deux . consécutifs")
    if domaine.startswith("."):
        raise ValueError("Le nom de domaine ne peut pas commencer pas un point")
    if domaine.endswith("."):
        raise ValueError("Le nom de domaine ne peut pas se terminer pas un point")
    if len(domaine) > 64:
        raise ValueError("Le nom de domaine ne peut pas faire plus de 64 caractères")

    return (
        f"Bonjour {prenom} {nom} de {ville}, votre inscription a bien été prise en compte à l'addresse mail suivante : {email}"
    )