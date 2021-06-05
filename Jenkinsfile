pipeline {
    agent any

	environment {
          git_repo = "https://github.com/AtrashAyoub/Kaltura"
	      docker_image = "ayoubatrash/kaltura"	
          docker_secret = "dockerhubSecret"		
	}
	
    parameters {
	string(name: 'HTTP_PORT', defaultValue:'80', description: 'HTTP Port')
	string(name: 'HTTPS_PORT', defaultValue:'443', description: 'HTTPS Port')
    }
		
    stages {
        
        stage("Build Docker") {
            steps {
		withCredentials([usernamePassword(credentialsId: docker_secret, usernameVariable: 'USERNAME',
                         passwordVariable: 'PASSWORD')]) {
                    sh "docker login -u $USERNAME -p $PASSWORD"
                 }
  
	        sh "docker build -t  ${docker_image} . && docker push ${docker_image}:latest"
	   
            }
        }
	
	stage("Run the Application") {
		steps{	
			sh "docker run -itd -p ${params.HTTP_PORT}:80 -p ${params.HTTPS_PORT}:80 "
		}
		
		post {
			success {
			  slackSend channel: "notificationapp", message: "Build Finished Successfully !"
			}
			failure {
			  slackSend channel: "notificationapp", message: "Build Failed !"
			}
			
	}
       
        
    }
	}
}
