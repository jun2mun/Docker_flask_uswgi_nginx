 node {
     def app

     stage('Clone repository') {
         /* Let's make sure we have the repository cloned to our workspace */

         checkout scm
     }
     dir("flask"){
        /* This builds the actual image; synonymous to
         * docker build on the command line */
      stage('Build image'){
         sh 'docker build -t jun2mun/flask:pipeline .'
      }
     }
     dir("nginx"){
        /* This builds the actual image; synonymous to
         * docker build on the command line */
      stage('Build image'){
         sh 'ls'
         sh 'docker build -t jun2mun/nginx:pipline .'
      }
     }

     stage('Test image') {
         sh 'docker run ---name web -d -p 5000:5000 jun2mun/flask:pipeline
     }

     stage('Push image') {
         /* Finally, we'll push the image with two tags:
         * First, the incremental build number from Jenkins
         * Second, the 'latest' tag.
         * Pushing multiple tags is cheap, as all the layers are reused. */
         docker.withRegistry('https://registry.hub.docker.com', 'docker-hub') {
             sh 'docker push jun2mun/flask:pipleine
             sh 'docker push jun2mun/nginx:pipeline
         }
     }
 }
