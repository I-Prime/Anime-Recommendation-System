pipeline {
    agent any

    
    stages{

        stage("Cloning from Github...."){
            steps{
                script{
                    echo 'Cloning from Github...'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github_anime', url: 'https://github.com/I-Prime/Anime-Recommendation-System.git']])
                }
            }
        }
    }
}