 node {
     def app

     stage('Clone repository') {
         /* Let's make sure we have the repository cloned to our workspace */

         checkout scm
     }

     dir("flask"){
         sh 'pwd'
     }
     stage('Build image') {
         /* This builds the actual image; synonymous to
         * docker build on the command line */
         
        sh 'docker build -t jun2mun/Docker_flask_uswgi_nginx/flask'
        sh 'docker build -t jun2mun/Docker_flask_uswgi_nginx/nginx'
         
     }

     stage('Test image') {
         app.inside {
             sh 'echo "Tests passed"'
         }
     }

     stage('Push image') {
         /* Finally, we'll push the image with two tags:
         * First, the incremental build number from Jenkins
         * Second, the 'latest' tag.
         * Pushing multiple tags is cheap, as all the layers are reused. */
         docker.withRegistry('https://registry.hub.docker.com', 'docker-hub') {
             app.push("${env.BUILD_NUMBER}")
             app.push("latest")
         }
     }
 }
