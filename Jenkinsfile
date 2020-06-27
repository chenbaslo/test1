pipeline {
   agent any

   stages {
      stage('Hello') {
         steps {
            echo 'in the git'
            bat 'hostname'
            dir('app'){
               bat 'python3 app3.py'
            }
            
         }
      }
   }
}
