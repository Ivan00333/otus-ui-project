pipeline {
    agent {
        docker {
            image 'mcr.microsoft.com/playwright/python:v1.52.0-noble'
            args '-u root'
        }
    }

    parameters {
        credentials(
            name: 'SAUCE_DEMO_CRED',
            credentialType: 'UsernamePassword',
            description: 'Sauce Demo credentials'
        )
        choice(
            name: 'ENV',
            choices: ['test', 'staging', 'prod'],
            description: 'Target environment'
        )
        choice(
            name: 'BROWSER',
            choices: ['chrome', 'firefox'],
            description: 'Browser to test'
        )
        booleanParam(
            name: 'HEADLESS',
            defaultValue: true,
            description: 'Run in headless mode'
        )
        string(
            name: 'SLOW',
            defaultValue: '200',
            description: 'slow_mo for Playwright actions in ms'
        )
    }

    environment {
        TEST_URL = 'https://www.saucedemo.com/'
        ENV      = "${params.ENV}"
        BROWSER  = "${params.BROWSER}"
        H        = "${params.HEADLESS}"
        SLOW     = "${params.SLOW}"
    }

    stages {
        stage('Install Java') {
            steps {
                sh '''
                  apt-get update
                  apt-get install -y openjdk-11-jre-headless
                '''
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Prepare .env') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'sauce-demo-creds',
                    usernameVariable: 'TEST_AUTH_LOGIN',
                    passwordVariable: 'TEST_AUTH_PASSWORD'
                )]) {
                    sh '''
                      cat > .env <<EOF
                      TEST_URL=${TEST_URL}
                      ENV=${ENV}
                      TEST_AUTH_LOGIN=${TEST_AUTH_LOGIN}
                      TEST_AUTH_PASSWORD=${TEST_AUTH_PASSWORD}
                      EOF
                    '''
                    sh 'echo ".env content:" && cat .env'
                }
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                  pip install --upgrade pip
                  pip install -r requirements.txt
                  python3 -m playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                  pytest \
                    --browser=${BROWSER} \
                    --h=${H} \
                    --slow=${SLOW} \
                    --alluredir=reports/allure-results \
                    -q
                '''
            }
        }
    }

    post {
        always {
            allure([
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'reports/allure-results']]
            ])
            archiveArtifacts artifacts: 'reports/allure-results/**/*', fingerprint: true
        }
    }
}
