pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
        pollSCM '* * * * *'
    }
    environment {
        CI = true
        ARTIFACTORY_ACCESS_TOKEN = credentials('artifactory-access-token')
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd jenkins_test_app
                pip install pytest
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd jenkins_test_app
                python3 -m pytest .
                '''
            }
        }
        stage('Deliver') {
            agent {
                docker {
                  image 'releases-docker.jfrog.io/jfrog/jfrog-cli-v2:2.2.0'
                  reuseNode true
                }
            }
              steps {
                sh 'jfrog rt upload --url http://192.168.54.61:8081/artifactory/ --access-token ${ARTIFACTORY_ACCESS_TOKEN} jenkins_test_app/main.py jenkins_test_app/'
            }
        }
    }
}

