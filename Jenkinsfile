pipeline {
    agent any

    stages {

        stage('Checkout Source Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/kapil3771/AI-Restaurant-Success-Predictor.git'
            }
        }

        stage('Pull Docker Image') {
            steps {
                sh 'docker pull kapil9123/restaurant-predictor:1.0.0'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                kubectl rollout status deployment/restaurant-app
                kubectl get pods
                kubectl get services
                '''
            }
        }
    }
}