# File: random_hash_machine.py
import hashlib
import random
import string
import time
from flask import Flask, jsonify

app = Flask(__name__)

def generate_random_hash():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    hash_object = hashlib.sha256(random_string.encode())
    return hash_object.hexdigest()

@app.route("/endpoint1")
def endpoint1():
    time.sleep(1)  # Simulate 1 second delay
    return jsonify({"hash": generate_random_hash()})

@app.route("/endpoint2")
def endpoint2():
    while True:
        response = app.test_client().get("/endpoint1")
        data = response.get_json()
        return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

