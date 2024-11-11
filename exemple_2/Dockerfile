# Utiliser l'image Python de base Alpine (plus légère)
FROM python:3.8-alpine

# Copier le code de l'application dans le conteneur
COPY . /app

# Spécifier le répertoire de travail pour le sous-dossier 'exemple_2'
WORKDIR /app

# Afficher le contenu du répertoire 'exemple_2' dans le conteneur pour le débogage
RUN ls -l /app

# Exposer le port (si nécessaire pour l'application)
EXPOSE 5000

# Commande par défaut pour exécuter l'application avec le chemin complet
CMD ["echo", "HELLO MIASD 2024"]
