# Utiliser une image de base avec Python
FROM python:3.8-slim

# Configurer DNS pour assurer la connexion Internet
RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf && \
    echo "nameserver 8.8.4.4" >> /etc/resolv.conf

# Mettre à jour pip et installer Flask
RUN pip install --upgrade pip && pip install flask


# Copier le code de l'application dans le conteneur
COPY . /app

# Spécifier le répertoire de travail pour le sous-dossier 'exemple_2'
WORKDIR /app

# Commande par défaut pour exécuter l'application avec le chemin complet
CMD ["pwd"]
CMD ["ls"]

# Exposer le port 
EXPOSE 5000

CMD ["python","test-jenkins-docker/exemple_2/app.py"]


