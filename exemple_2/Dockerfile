# Utiliser l'image Python de base Alpine 
FROM python:3.8-alpine

# Copier le code de l'application dans le conteneur
COPY exemple_2 /app

# Spécifier le répertoire de travail
WORKDIR /app

# Exposer le port 
EXPOSE 5000

# Commande par défaut pour exécuter l'application
CMD ["python", "app.py"]
