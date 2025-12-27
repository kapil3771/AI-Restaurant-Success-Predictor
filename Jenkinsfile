pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t restaurant-predictor:ci .'
            }
        }

        stage('Run Container Test') {
            steps {
                sh '''
                docker run -d -p 8501:8501 --name test_app restaurant-predictor:ci
                sleep 10
                docker ps | grep test_app
                docker rm -f test_app
                '''
            }
        }
    }
}