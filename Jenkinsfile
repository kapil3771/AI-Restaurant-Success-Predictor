pipeline {
    agent any

    stages {
        stage('Checkout Source Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/kapil3771/AI-Restaurant-Success-Predictor.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t restaurant-predictor:ci .'
            }
        }

        stage('Run Container Test') {
            steps {
                sh '''
                docker run -d -p 8501:8501 restaurant-predictor:ci
                sleep 10
                docker ps
                docker stop $(docker ps -q --filter ancestor=restaurant-predictor:ci)
                '''
            }
        }
    }
}