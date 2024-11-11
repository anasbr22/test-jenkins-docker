pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/anasbr22/test-jenkins-docker'
        APP_DIR = 'test-jenkins-docker/exemple_2'  
        CONTAINER_NAME = 'tkinter-python-app-container'
        IMAGE_NAME = 'image-tkinter-python-app'
        PORT = '5000'
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    echo "Cleaning workspace..."
                    sh "rm -rf *"  // Supprime tout dans le répertoire de travail Jenkins
                    echo "Cloning repository..."
                    sh "git clone ${REPO_URL}"  // Cloner le dépôt
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Assurez-vous d'être dans le répertoire 'exemple_2'
                dir("${APP_DIR}") {
                    // Exécuter les tests unitaires
                    sh "python3 -m unittest test_app.py"
                }
            }
        }

        stage('Stop Existing Container') {
            steps {
                // Arrêter et supprimer un conteneur existant
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
            }
        }

        stage('Remove Old Docker Image') {
            steps {
                script {
                    // Suppression de l'image si elle existe déjà
                    sh 'docker rmi -f image-tkinter-python-app || true'  
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    
                    sh "docker build -f jenkins-docker-test/exemple_2/Dockerfile -t ${IMAGE_NAME} ."

                }
            }
        }

        stage('Run Docker Container') {
            steps {
                // Exécuter un conteneur avec l'image Docker construite
                sh "docker run -d --name ${CONTAINER_NAME} -p ${PORT}:${PORT} ${IMAGE_NAME}"
            }
        }
    }

    post {
        always {
            // Actions à réaliser à la fin du pipeline (en succès ou échec)
            echo 'Pipeline terminé.'
        }
        failure {
            // Actions spécifiques en cas d'échec
            echo 'Échec de la pipeline.'
        }
        success {
            // Actions spécifiques en cas de succès
            echo 'Pipeline exécuté avec succès.'
        }
    }
}
