# Utiliser l'image Node.js officielle
FROM node:16

# Créer et définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY . .

# Installer les dépendances
RUN npm install

# Exposer le port
EXPOSE 80

# Lancer l'application
CMD ["node", "app.js"]

