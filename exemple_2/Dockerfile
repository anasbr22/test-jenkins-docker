# Utiliser une image de base contenant Python
FROM python:3.11

# Installer les dépendances nécessaires pour Tkinter et X11
RUN apt-get update && apt-get install -y \
    python3-tk \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Installer les dépendances Python
RUN pip install  tkinter

# Copier le code de l'application dans le conteneur
COPY . /app

# Spécifier le répertoire de travail pour le sous-dossier 'exemple_2'
WORKDIR /app

# Commande par défaut pour exécuter l'application avec le chemin complet
CMD ["pwd"]
CMD ["ls"]

# Exposer le port (si nécessaire pour l'application)
EXPOSE 5000

CMD ["python","test-jenkins-docker/exemple_2/app.py"]


