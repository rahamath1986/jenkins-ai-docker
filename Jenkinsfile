pipeline {
  agent none

  environment {
    SLACK_WEBHOOK_URL = credentials('SLACK_WEBHOOK_URL')
  }

  stages {

    stage('Checkout') {
      agent any
      steps {
        checkout scm
      }
    }

    stage('Fastlane Android Build') {
      agent {
        docker {
          image 'freeletics/fastlane:2.227.2'
          args '--platform linux/amd64'
        }
      }
      steps {
        sh '''
          cd $WORKSPACE/android

          chmod +x gradlew

          # Run Fastlane and capture REAL logs
          fastlane android ci_build > build.log 2>&1 || true
        '''
      }
    }

    stage('AI Failure Analysis & Archive') {
      agent {
        docker {
          image 'python:3.11'
          args '--network ai-net'
        }
      }
      steps {
        sh '''
          pip install requests
          python ai-agent/agent.py < $WORKSPACE/android/build.log
        '''

        archiveArtifacts artifacts: 'android/build.log', fingerprint: true
      }
    }
  }
}