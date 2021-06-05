pipeline {
    agent any
		
    stages {
	
        stage("Build") {

            steps {
                echo "Building the application..."
		sh 'docker build -t kaltura .'
                
            }
        }
		
       
        
    }
	}
