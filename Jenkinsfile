pipeline {
     agent any
     
     environment {
          dh_pass = credentials('DOCKER_PASS')
     }
     
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
                  sh 'docker login -u gradjitta -p $dh_pass'
               }
         }
         stage('Push Docker Image') {
              steps {
                      sh "docker tag streamlit-app gradjitta/streamlit-app:prod"
                      sh 'docker push gradjitta/streamlit-app:prod'
                  }
              }
         }
 }
