# DATA CENTER
This setup assumes you have Docker running on your machine. 
Please download Docker for your platform if you don't.
You can download it here https://www.docker.com/get-started

With this packaged conatiner we have designed three services:

- A simple job generator expecting a job sent as a POST request.
- A job queue that the generator feeds jobs too
- A Job puller that pops jobs off the queue.

All these services are separate containers interconnected as one main system.


Steps:
 
To get up and running, open terminal and type:

$ docker-compose up --build 

This will instatiate the docker container and startup the job queue and the generator. 
This container stays running till it is terminated.


After setup, you can add a sample job to the generator by typing in another terminal instance:

$ curl -d '{
    "name": "pie",
    "action": "kpansh"
  }' \
  -H 'Content-Type: application/json' \
  http://localhost:5000/add_job

That will send a simple POST request to the job generator, you will see this reflect in terminal where the container is running.


"# Data_Center_Network" 
