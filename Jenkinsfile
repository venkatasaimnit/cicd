pipeline {
  agent any 
  stages {
    stage("clone repository") {
      /* cloning repository to our workspace */
      steps {
        checkout scm
      }
    }
    stage('build image') {
      steps {
        sh 'sudo usermod -a -G docker jenkins' 
        sh 'sudo docker build -t firstproject .'
      }
    }
    stage('Run image') {
      steps {
        sh 'sudo docker run -d -p 5000:5000 -v $(which docker):/usr/bin/docker firstproject'
      }
    }
    stage('testing') {
      steps {
        echo 'testing'
      }
    }
  }
}
