pipeline {
  agent any

  parameters {
    credentials(
      name: 'SAUCE_DEMO_CRED',
      credentialType: 'UsernamePassword',
      description: 'Sauce Demo login/password'
    )
    choice(name: 'ENV', choices: ['test'], description: '')
    choice(name: 'BROWSER', choices: ['chrome','firefox'], description: '')
    booleanParam(name: 'HEADLESS', defaultValue: true, description: '')
    string(name: 'SLOW', defaultValue: '200', description: '')
  }

  environment {
    TEST_URL = 'https://www.saucedemo.com/'
    ENV     = "${params.ENV}"
    BROWSER = "${params.BROWSER}"
    H       = "${params.HEADLESS}"
    SLOW    = "${params.SLOW}"
  }

  stages {
    stage('Checkout') { steps { checkout scm } }

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
