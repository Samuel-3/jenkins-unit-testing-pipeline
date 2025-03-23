pipeline {
    stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
    }

    agent { docker { image 'python:3.13.2-alpine3.21' } }
    
    stages {
        stage('build') {
            steps {
                sh 'py --version'
            }
        }
    }
}

