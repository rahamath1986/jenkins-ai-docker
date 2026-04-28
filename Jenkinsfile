pipeline {
  agent none

  environment {
    SLACK_WEBHOOK_URL = credentials('SLACK_WEBHOOK_URL')
  }

  stages {
    stage('AI Agent Test') {
      agent {
        docker {
          image 'python:3.11'
          args '--network ai-net -v $PWD:/app'
        }
      }
      steps {
        sh '''
          pip install requests
          echo "Build failed due to dependency conflict" > build.log
          python ai-agent/agent.py < build.log
        '''
      }
    }
  }
}