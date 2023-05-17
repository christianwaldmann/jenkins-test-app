pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                pip install pytest
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                pytest .
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                python3 main.py
                '''
            }
        }
    }
}

