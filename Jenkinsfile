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
	   
	    
	//Fetch the code from Git Repo    
	// stage("Pull Code From Repo") {
	// 	git git_repo
	// }
	   
        stage("Build Docker") {
            steps {
		withCredentials([usernamePassword(credentialsId: docker_secret, usernameVariable: 'USERNAME',
                         passwordVariable: 'PASSWORD')]) {
                    sh "docker login -u $USERNAME -p $PASSWORD && docker push ${docker_image} "
                 }
  
	        sh "docker build -t  ${docker_image}:latest . && docker push ${docker_image}"
            }
        }
	
	stage("Run the Application") {
		steps{	
			sh "docker run -itd -p ${params.HTTP_PORT}:80 -p ${params.HTTPS_PORT}:80 "
		}
		
		post {
			success {
			  slackSend (channel: "notificationapp", color: colorCode, message: "Success !")
			}
			failure {
			  slackSend (channel: "notificationapp", color: colorCode, message: "Failed !")
			}
			
	}
       
        
    }
	}
}
