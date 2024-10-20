
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "hospital-management-system"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/sonu-iyer/Hospital-Management-System1.git', branch: 'main', credentialsId: 'sonu-iyer'
    
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh "docker run --rm ${DOCKER_IMAGE} python -m unittest discover"
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'sonalika27', usernameVariable: 'sonalika27', passwordVariable: '7815976825AS')]) {
                        sh "docker login -u sonalika27 -p 7815976825AS"
                        sh "docker tag ${DOCKER_IMAGE} sonalika27/${DOCKER_IMAGE}"
                        sh "docker push sonalika27/${DOCKER_IMAGE}"
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Stop and remove existing container
                    sh 'docker stop hospital-management-system || true && docker rm hospital-management-system || true'

                    // Run the Docker container
                    sh "docker run -d --name hospital-management-system -p 80:81 ${DOCKER_IMAGE}"
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}

