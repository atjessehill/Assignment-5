from flask import Flask, jsonify
import json

data = {"1": "Jesse", "2": "Jonathan", "3": "Luisa", "4": "Ana Maria", "5": "James"}

app = Flask(__name__)

def get_all_customers():
    return data

def get_customer_by_id(id):
    for key, value in data.items():
        if key == id:
            print(key)
            print(value)
            print(id)
            return value

    return "No User with that ID"

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route('/customers', methods=['GET'])
def return_customers():
    d = get_all_customers()
    return jsonify(d)

@app.route('/customers/<id>', methods=['GET'])
def return_one_customer(id):
    d = get_customer_by_id(id)
    return d

if __name__== "__main__":
    app.run()