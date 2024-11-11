# Utiliser l'image Python de base Alpine (plus légère)
FROM python:3.8-alpine

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


