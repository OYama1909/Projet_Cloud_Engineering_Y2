from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    # Ici, vous récupérerez les données réelles, par exemple depuis un capteur ou une base de données
    data = {"temperature": 22.5, "humidity": 45.2}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
def get_sensor_data():
    # Simuler la récupération de données depuis un capteur
    temperature = random.uniform(20.0, 25.0)
    humidity = random.uniform(40.0, 60.0)
    return {"temperature": temperature, "humidity": humidity}

@app.route('/data', methods=['GET'])
def get_data():
    data = get_sensor_data()
    return jsonify(data)
