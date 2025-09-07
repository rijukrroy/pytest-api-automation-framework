pipeline {
    agent any

    tools {
        // Make sure Jenkins has Python installed or installed via system package
        // Otherwise, we'll use venv as below
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/rijukrroy/pytest-api-automation-framework.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv venv
                    venv/bin/pip install --upgrade pip
                    venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    venv/bin/python -m pytest --maxfail=1 --disable-warnings -q --alluredir=allure-results
                '''
            }
        }

        stage('Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }

    post {
        always {
            // Publish test results if JUnit XML is generated
            junit 'allure-results/*.xml'
        }
    }
}
