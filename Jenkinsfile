pipeline {
  agent any

  stages {
    stage('AI Agent Test') {
      steps {
        sh '''
          echo "Build failed due to dependency issue" > build.log
          cat build.log | python3 ai-agent/agent.py
        '''
      }
    }
  }
}