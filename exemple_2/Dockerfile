# Utiliser une image de base avec Python
FROM python:3.8-slim



# Copier le code de l'application dans le conteneur
COPY . /app

# Spécifier le répertoire de travail pour le sous-dossier 'exemple_2'
WORKDIR /app

# Exposer le port 5000 pour Flask
EXPOSE 5000

# Commande par défaut pour exécuter l'application Flask
CMD ["python", "test-jenkins-docker/exemple_2/app.py"]
