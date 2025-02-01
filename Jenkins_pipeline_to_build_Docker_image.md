```
Prerequisites

Docker Installed on Jenkins Agent
Jenkins Credentials:
Docker Hub Username & Password stored as Jenkins credentials (docker-hub-credentials).
GitHub Repository with a valid Dockerfile.
Jenkinsfile in the GitHub repo (or create a Pipeline job in Jenkins).
Jenkinsfile (Declarative Pipeline)

pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "your-dockerhub-username/your-image-name"
        DOCKER_TAG = "latest"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/your-username/your-repository.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    }
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    sh "docker rmi ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }
    }

    post {
        success {
            echo "Docker Image successfully pushed to Docker Hub!"
        }
        failure {
            echo "Build failed. Check logs for details."
        }
    }
}
Explanation of Stages

Stage	Description
Clone Repository	Clones the GitHub repository containing the Dockerfile.
Build Docker Image	Builds a Docker image from the Dockerfile.
Login to Docker Hub	Uses Jenkins credentials to authenticate with Docker Hub.
Push Docker Image	Pushes the image to Docker Hub.
Cleanup	Removes the locally built image to save space.
Setting Up Jenkins Pipeline Job

Go to Jenkins Dashboard → New Item
Select "Pipeline", give it a name, and click OK.
In the Pipeline section, select Pipeline script from SCM.
Choose Git, and enter your GitHub repository URL.
Under Script Path, enter Jenkinsfile.
Click Save and Build Now.
Verifying the Image

After the pipeline runs successfully, check your Docker Hub repository:

docker pull your-dockerhub-username/your-image-name:latest
```