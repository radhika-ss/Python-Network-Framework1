pipeline {

    agent any

    stages {

        stage('Checkout Code') {

            steps {

                git 'https://github.com/radhika-ss/Python-Network-Framework1.git'
            }
        }

        stage('Install Dependencies') {

            steps {

                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Pytest Tests') {

            steps {

                bat 'python -m pytest -v'
            }
        }

        stage('Archive Logs') {

            steps {

                archiveArtifacts artifacts: 'framework.log', fingerprint: true
            }
        }
    }

    post {

        always {

            echo 'Pipeline execution completed'
        }

        success {

            echo 'All tests passed successfully'
        }

        failure {

            echo 'Some tests failed'
        }
    }
}
