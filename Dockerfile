FROM jenkins/jenkins:lts-jdk17

USER root

# Install Docker CLI only (not daemon)
RUN apt-get update && \
    apt-get install -y docker.io && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN gem install fastlane -NV && \
    gem install bundler
USER jenkins