import base64
import json

def decode_data(encoded_data):
    base64_bytes = encoded_data.encode('utf-8')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('utf-8')
    return json.loads(message)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.data
    decoded_data = decode_data(data)
    print(decoded_data)  # Afficher les données pour le débogage
    # Ici, vous pourriez appeler une fonction pour stocker les données dans la base de données.
    return jsonify({"message": "Data received successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
