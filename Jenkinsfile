pipeline {
  agent any

  parameters {
    choice(
      name: 'ENV',
      choices: ['test'],
      description: 'Choose the target environment'
    )
    choice(
      name: 'BROWSER',
      choices: ['chrome', 'firefox'],
      description: 'Choose browser: chrome or firefox'
    )
    credentials(
      name: 'SAUCE_CREDENTIALS',
      credentialType: 'UsernamePassword',
      description: 'Sauce Demo credentials'
    )
  }

  environment {
    TEST_URL = 'https://www.saucedemo.com/'
    ENV            = "${params.ENV}"
    BROWSER        = "${params.BROWSER}"
    TEST_AUTH_LOGIN    = "${SAUCE_CREDENTIALS_USR}"
    TEST_AUTH_PASSWORD = "${SAUCE_CREDENTIALS_PSW}"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Prepare .env') {
      steps {
        sh '''
          cat > .env <<EOF
          TEST_URL=${TEST_URL}
          ENV=${ENV}
          TEST_AUTH_LOGIN=${TEST_AUTH_LOGIN}
          TEST_AUTH_PASSWORD=${TEST_AUTH_PASSWORD}
          EOF
        '''
        sh 'cat .env'
      }
    }

    stage('Setup Python & Playwright') {
      steps {
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
          python3 -m playwright install --with-deps
        '''
      }
    }

    stage('Run Tests') {
      steps {
        sh '''
          . venv/bin/activate
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
