from flask import Flask, request, jsonify
import msgpack
import base64
import psycopg2
from psycopg2.extras import execute_values
import json
from app.services.anomaly_detector_fonction import anomaly_detector

app = Flask(__name__)


@app.route('/receive', methods=['POST'])
def receive_data():
    # Vérifier si les données reçues sont au format MsgPack
    if request.content_type == 'application/json':
        data = request.data
        # Décoder les données MsgPack
        try:
            # Configurations de la base de données 
            DATABASE = "root"
            USER = "root"
            PASSWORD = "root"
            HOST = "127.0.0.1"
            PORT = "5432"

            # Premièrement, décoder depuis Base64
            base64_decoded_bytes = base64.b64decode(data)

            # Ensuite, décompresser les données MessagePack
            decoded_data = msgpack.unpackb(base64_decoded_bytes)

            # Convertir les données JSON en texte
            data_text = json.dumps(decoded_data)

            # Insérer les données textuelles dans la base de données PostgreSQL
            conn = psycopg2.connect(dbname=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
            cur = conn.cursor()

            # Insérer les données dans les tables appropriées
            sensor_id = data_text["sensor_id"]
            sensor_version = data_text["sensor_version"]
            plant_id = data_text["plant_id"]
            timestamp = data_text["time"]
            measures = data_text["measures"]

            temperature_value = float(measures["temperature"].replace("°C", ""))
            humidity_value = float(measures["humidite"].replace("%", ""))

            if anomaly_detector(measures["temperature"]) == "anomaly":
                temperature_value = anomaly_detector(temperature_value, "yes")

                # Insérer les données de température
                cur.execute("INSERT INTO anomaly (value_temp, value_humidity, plant_id, sensor_id) VALUES (%s, %s, %s, %s);", (temperature_value, humidity_value, plant_id, sensor_id))

                # Valider la transaction
                conn.commit()

                # Fermer la connexion
                cur.close()
                conn.close()

            else:
                # Insérer les données de température
                cur.execute("INSERT INTO temperature (value, plant_id, sensor_id) VALUES (%s, %s, %s);", (temperature_value, plant_id, sensor_id))

                # Insérer les données d'humidité
                cur.execute("INSERT INTO humidity (value, plant_id, sensor_id) VALUES (%s, %s, %s);", (humidity_value, plant_id, sensor_id))

                # Insérer les données de l'ID de la plante (si nécessaire)
                cur.execute("INSERT INTO id_plant (id) VALUES (%s);", (plant_id,))

                # Insérer les données des capteurs
                cur.execute("INSERT INTO id_sensors (id, type, timestamp) VALUES (%s, %s, %s);", (sensor_id, sensor_version, timestamp))

                # Valider la transaction
                conn.commit()

                # Fermer la connexion
                cur.close()
                conn.close()
        except msgpack.ExtraData as e:
            return jsonify({"status": "error", "message": "Extra data received."}), 400
    else:
       return jsonify({"status": "error", "message": "Invalid content type. Please send MsgPack data."}), 415

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
