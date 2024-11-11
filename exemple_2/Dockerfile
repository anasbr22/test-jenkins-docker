# Utiliser une image de base avec Python
FROM python:3.8-slim

# Copier le code de l'application dans le conteneur
COPY . /app

# Spécifier le répertoire de travail
WORKDIR /app

# Exposer le port 5000 pour l'application
EXPOSE 5000

# Commande pour exécuter l'application
CMD ["python", "app.py"]
