import base64
import psycopg2
from psycopg2.extras import execute_values
import msgpack
from flask import Flask, request, jsonify
import json
from anomaly_detector import anomaly_detector

# Configurations de la base de données 
DATABASE = "root"
USER = "root"
PASSWORD = "root"
HOST = "127.0.0.1"
PORT = "5432"


def decode_and_store(encoded_data):
    # Premièrement, décoder depuis Base64
    base64_decoded_bytes = base64.b64decode(encoded_data)

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


# Exemple d'utilisation
# encoded_text = "halzZW5zb3JfaWSmMTI2NTMxrnNlbnNvcl92ZXJzaW9upUZSLXY4qHBsYW50X2lkzgAAAAOkdGltZbQyMDI0LTA0LTExVDA3OjI0OjUzWqhtZWFzdXJlc4KrdGVtcGVyYXR1cmWlMTTCsEOoaHVtaWRpdGWjMTgl"
# decode_and_store(encoded_text, table_name)
