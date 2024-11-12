# Utiliser une image de base Node.js allégée (Alpine)
FROM node:16-alpine

# Créer et définir le répertoire de travail
WORKDIR /app

# Copier uniquement les fichiers nécessaires pour l'application Node.js
COPY package*.json ./

# Installer les dépendances de Node.js
RUN npm install

# Copier le reste des fichiers du projet dans le conteneur
COPY . .

# Exposer le port de l'application
EXPOSE 5000

# Lancer le serveur Node.js
CMD ["node", "public/app.js"]
