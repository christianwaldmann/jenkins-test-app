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
              steps {
                sh 'curl -v -X PUT -u admin:${ARTIFACTORY_ACCESS_TOKEN} --upload-file jenkins_test_app/main.py http://localhost:8081/artifactory/system-monitoring/main.py'
            }
        }
    }
}

