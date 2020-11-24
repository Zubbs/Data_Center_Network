import json
import redis
from flask import Flask, request


app = Flask(__name__)
r = redis.Redis(host="queue",port=6379)


@app.route("/add_job", methods=['POST'])
def add_job():
    data = request.json
    r.publish("jobs", json.dumps(data))
    return data, 200
