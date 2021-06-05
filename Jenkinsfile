pipeline {
    agent any
		
    stages {
	
        stage("Build") {

            steps {
                echo "Building the application..."
		bat 'docker build -t kaltura .'
                
            }
        }
		
       
        
    }
	}
