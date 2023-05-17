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
                pytest .
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                cd jenkins_test_app
                python3 main.py
                '''
            }
        }
    }
}

