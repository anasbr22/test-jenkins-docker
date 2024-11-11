# Utiliser une image de base contenant Python
FROM python:3.8-alpine

# Copier le code de l'application dans le conteneur
COPY . /app

# Spécifier le répertoire de travail pour le sous-dossier 'exemple_2'
WORKDIR /app

# Commande par défaut pour exécuter l'application avec le chemin complet
CMD ["pwd"]
CMD ["ls"]

# Exposer le port 
EXPOSE 5000

#Docker, par défaut, n'est pas conçu pour exécuter des applications graphiques sur un serveur
# CMD ["python","test-jenkins-docker/exemple_2/app.py"]


RUN echo "import http.server\nimport socketserver\n\nclass MyHandler(http.server.BaseHTTPRequestHandler):\n    def do_GET(self):\n        self.send_response(200)\n        self.send_header('Content-type', 'text/html')\n        self.end_headers()\n        self.wfile.write(b'<html><body><h1>L\\'application marche bien</h1></body></html>')\n\nPORT = 5000\nwith socketserver.TCPServer(('', PORT), MyHandler) as httpd:\n    print('Serving at port', PORT)\n    httpd.serve_forever()" > app.py
