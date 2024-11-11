# Utiliser une image de base contenant Python
FROM python:3.8-alpine

# Copier le code de l'application dans le conteneur
COPY . /app

# Spécifier le répertoire de travail pour le sous-dossier 'exemple_2'
WORKDIR /app

# Commande par défaut pour exécuter l'application avec le chemin complet
CMD ["pwd"]
CMD ["ls"]

# Exposer le port 
EXPOSE 5000

#Docker, par défaut, n'est pas conçu pour exécuter des applications graphiques sur un serveur
# CMD ["python","test-jenkins-docker/exemple_2/app.py"]
