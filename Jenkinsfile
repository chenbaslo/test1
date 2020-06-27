pipeline {
   agent any

   stages {
      stage('Hello') {
         steps {
            echo 'in the git'
            bat 'hostname'
            dir('app'){
               bat 'C:\Users\Chen\AppData\Local\Programs\Python\Python38\python.exe app3.py'
            }
            
         }
      }
   }
}
