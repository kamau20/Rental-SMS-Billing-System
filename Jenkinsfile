pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        VENV = "venv"
        BUILD_DIR = "built"
        REPO_URL = "https://github.com/kamau20/Rental-SMS-System.git"
        BRANCH = "main"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: "${BRANCH}",
                    credentialsId: 'jenkins-github-creds',
                    url: "${REPO_URL}"
            }
        }

        stage('Setup Python Virtualenv') {
            steps {
                sh '''
                    python3 -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Migrations') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    python manage.py migrate
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    python manage.py test
                '''
            }
        }

        stage('Collect Static Files') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    python manage.py collectstatic --noinput
                '''
            }
        }

        stage('Package Build Artifacts') {
            steps {
                sh '''
                    mkdir -p ${BUILD_DIR}
                    tar -czf ${BUILD_DIR}/rental-sms-build.tar.gz .
                '''
            }
        }
    }

    post {
        success {
            echo "Build successful 🎉"
            archiveArtifacts artifacts: 'built/*.tar.gz', fingerprint: true
        }
        failure {
            echo "Build failed ❌"
        }
    }
}