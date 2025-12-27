pipeline {
    agent any

    stages {
        stage('Pull Docker Image') {
            steps {
                sh 'docker pull kapil9123/restaurant-predictor:1.0.0'
            }
        }

        stage('Run Container Smoke Test') {
            steps {
                sh '''
                docker run -d -p 8501:8501 --name test_app kapil9123/restaurant-predictor:1.0.0
                sleep 15
                docker ps | grep test_app
                docker rm -f test_app
                '''
            }
        }
    }
}