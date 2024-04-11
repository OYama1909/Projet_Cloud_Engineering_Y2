from flask import Flask, request, jsonify
import msgpack
import base64


app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_data():
    # Vérifier si les données reçues sont au format MsgPack
    if request.content_type == 'application/json':
        data = request.data
        # Décoder les données MsgPack
        try:
            # First, decode from Base64
            base64_decoded_bytes = base64.b64decode(data)
            # Then, unpack the MessagePack data
            decoded_data = msgpack.unpackb(base64_decoded_bytes)
            # Afficher les données décodées
            print(decoded_data)
            return jsonify({"status": "success", "message": "Data received and decoded successfully."}), 200
        except msgpack.ExtraData as e:
            return jsonify({"status": "error", "message": "Extra data received."}), 400
    else:
       return jsonify({"status": "error", "message": "Invalid content type. Please send MsgPack data."}), 415

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
