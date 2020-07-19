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
          stage('Lint Dockerfile') {
               steps {
                  sh 'cat Dockerfile'
                  sh 'docker run --rm -i hadolint/hadolint < Dockerfile'
               }
          }
          stage('Lint Python Code') {
               steps {
                  sh 'pylint --disable=R,C,W1203,W1202,E0401,W0401,W0613,W0621,W0611,E0602  **/**.py'
               }
          }
         stage('Build Docker Image') {
              steps {
                  sh 'docker build . -t streamlit-app:roll'
              }
         }
         stage('Docker login') {
              steps {
                  sh 'docker login -u gradjitta -p $dh_pass'
               }
         }
         stage('Push Docker Image') {
              steps {
                      sh "docker tag streamlit-app:roll gradjitta/streamlit-app:roll"
                      sh 'docker push gradjitta/streamlit-app:roll'
               }
         }
         stage('Deploying k8s') {
              steps {
                   dir ('./') {
                      withAWS(credentials: 'aws-static', region: 'eu-west-1') {
                           sh "aws eks --region eu-west-1 update-kubeconfig --name CapstoneEKS-yG6S3kgKWfas"
                      }
                   }
              }
          }
     }
 }
