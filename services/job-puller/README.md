# JOB PULLER

This:

- subscribes to RabbitMQ,
- pulls jobs off it,
- sends jobs to network
- decides if the network is overloaded
- creates new network nodes
- effectively does load balancing
