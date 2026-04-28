pipeline {
  agent none

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
          echo "Build failed due to dependency issue" > build.log
          python ai-agent/agent.py < build.log
        '''
      }
    }

  }
}