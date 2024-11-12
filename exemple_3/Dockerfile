# Utiliser une image de base Node.js allégée (Alpine)
FROM node:16-alpine

# Créer et définir le répertoire de travail
WORKDIR /app

# Copier uniquement les fichiers nécessaires (package.json et package-lock.json d'abord)
COPY package*.json ./

# Installer les dépendances (optimisé en séparant les étapes pour profiter du cache Docker)
RUN npm install

# Copier le reste des fichiers du projet dans le conteneur
COPY . .

# Exposer le port de l'application
EXPOSE 80

# Lancer l'application
CMD ["node", "app.js"]
