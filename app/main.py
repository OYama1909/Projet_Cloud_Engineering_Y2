from flask import Flask, request, jsonify
import msgpack
import base64
from services/decode_store import decode_and_store


app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_data():
    # Vérifier si les données reçues sont au format MsgPack
    if request.content_type == 'application/json':
        data = request.data
        # Décoder les données MsgPack
        try:
            decode_and_store(data)
        except msgpack.ExtraData as e:
            return jsonify({"status": "error", "message": "Extra data received."}), 400
    else:
       return jsonify({"status": "error", "message": "Invalid content type. Please send MsgPack data."}), 415

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
