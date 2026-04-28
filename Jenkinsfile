pipeline {
  agent any

  environment {
    DOCKER_NETWORK = "ai-net"
  }

  stages {
    stage('AI Agent Test') {
      steps {
        sh '''
          echo "Build failed due to dependency issue" > build.log

          docker run --rm \
            --network ${DOCKER_NETWORK} \
            -v "$PWD:/app" \
            -w /app \
            python:3.11 \
            python ai-agent/agent.py < build.log
        '''
      }
    }
  }
}