import redis

r = redis.Redis(host="queue",port=6379)

def main():
    pubsub = r.pubsub()
    pubsub.subscribe("jobs")

    print("testing!")

    for job in pubsub.listen():
        """
        - sends jobs to network
        - decides if the network is overloaded
        - creates new network nodes
        - effectively does load balancing
        """
        print(job)

main()
