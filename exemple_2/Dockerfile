# Utiliser l'image Python de base Alpine (plus légère)
FROM python:3.8-alpine

# Copier le code de l'application dans le conteneur
COPY . /app

# Spécifier le répertoire de travail 
WORKDIR /app/exemple_2

# Afficher le contenu du répertoire 'exemple_2' dans le conteneur
RUN ls -l

# Exposer le port (si nécessaire pour l'application)
EXPOSE 5000

# Commande par défaut pour exécuter l'application
CMD ["python", "app.py"]
