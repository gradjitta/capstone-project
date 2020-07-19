pipeline {
     agent any
     stages {
         stage('Build') {
              steps {
                  sh 'echo Building...'
              }
         }
         stage('Build Docker Image') {
              steps {
                  sh 'docker build . -t streamlit-app'
              }
         }
         stage('Docker login') {
              steps {
                  sh 'docker login --u=gradjitta -p="$DOCKER_PASS"'
               }
         }
         stage('Push Docker Image') {
              steps {
                      sh "docker tag streamlit-app gradjitta/streamlit-app"
                      sh 'docker push gradjitta/streamlit-app'
                  }
              }
         }
 }
