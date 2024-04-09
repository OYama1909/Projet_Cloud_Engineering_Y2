from flask import Flask, jsonify

app = Flask(__name__)

# Example data - in a real application, this would be dynamic
sensor_data = {
    'temperature': 20.5,  # Celsius
    'humidity': 50.0  # Percent
}

@app.route('/infos', methods=['GET'])
def get_infos():
    humidity = sensor_data['humidity']
    temperature = sensor_data['temperature']
    return jsonify({'humidity': humidity},{'temperature': temperature})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
