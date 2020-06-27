pipeline {
   agent any

   stages {
      stage('Hello') {
         steps {
            echo 'in the git'
            bat 'hostname'
            deleteDir()
         }
      }
   }
}
