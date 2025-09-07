pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/rijukrroy/pytest-api-automation-framework.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    mkdir -p reports allure-results
                    venv/bin/python -m pytest --maxfail=1 --disable-warnings -q \
                        --alluredir=allure-results \
                        --junitxml=allure-results/junit-results.xml
                '''
            }
        }

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'reports/test_log.log', allowEmptyArchive: true
                junit 'allure-results/junit-results.xml'
            }
        }

        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}
