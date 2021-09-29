pipeline {
    agent any

    stages {
        stage('Build and Push Docker Image...') {
            steps {
                script {
                  // CUSTOM REGISTRY
                    docker.withRegistry('https://myregistry.images.io:30000') {

                        /* Build the container image */
                        def dockerImage = docker.build("main:${env.BUILD_ID}")

                        /* Push the container to the custom Registry */
                        dockerImage.push()

                    }
                    /* Remove docker image*/
                    sh "docker rmi -f main:${env.BUILD_ID}"
                }
            }
        }
    }
}

