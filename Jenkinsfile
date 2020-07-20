pipeline {
     agent any
     
     environment {
          dh_pass = credentials('DOCKER_PASS')
          IMAGE_TAG = "latest"
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
                  sh 'docker build . -t streamlit-app:$IMAGE_TAG'
              }
         }
         stage('Docker login') {
              steps {
                  sh 'docker login -u gradjitta -p $dh_pass'
               }
         }
         stage('Push Docker Image') {
              steps {
                      sh "docker tag streamlit-app:$IMAGE_TAG gradjitta/streamlit-app:$IMAGE_TAG"
                      sh 'docker push gradjitta/streamlit-app:$IMAGE_TAG'
               }
         }
         stage('Configuring k8s') {
              steps {
                   dir ('./') {
                      withAWS(credentials: 'aws-static', region: 'eu-west-1') {
                           sh "aws eks --region eu-west-1 update-kubeconfig --name CapstoneEKS-yG6S3kgKWfas"
                           sh "kubectl apply -f aws-cf/aws-auth-cm.yaml"
                      }
                   }
              }
          }
          stage('Deploying app to k8 cluster') {
              steps {
                   dir ('./') {
                      withAWS(credentials: 'aws-static', region: 'eu-west-1') {
                           sh "kubectl apply -f aws-cf/streamlit-deploy.yaml"
                      }
                   }
              }
          }
          stage('Rollout update app to k8 cluster') {
              steps {
                   dir ('./') {
                      withAWS(credentials: 'aws-static', region: 'eu-west-1') {
                           sh "kubectl set image deployments/streamlit-app streamlit-app=gradjitta/streamlit-app:$IMAGE_TAG"
                      }
                   }
              }
          }
          stage("Remove dangling images") {
              steps{
                    sh "docker system prune -f"
              }
        }
     }
 }
