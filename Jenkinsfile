pipeline {
    agent any
	
    parameters {
		
	string(Name: 'HTTP_PORT', defaultValue:'80', description: 'First Port')
		
		
    }
		
    stages {
	   
	    
	# Fetch the code from Git Repo    
	stage("Pull Code From Repo") {
	  git 'https://github.com/AtrashAyoub/Kaltura'
	}
	   
        stage("Build Docker") {
            steps {
		sh 'docker build -t kaltura .'
                
            }
        }
	
	stage("Run the Application") {
		steps{	
			sh "docker run -itd -p ${params.HTTP_PORT}:8080 <imagename> "
		}
		
		post {
			success {
			  slackSend ...
			}
			failure {
				slackSend ...
			}
			
	}
       
        
    }
	}
