import base64
import psycopg2
from psycopg2.extras import execute_values
import msgpack
from flask import Flask, request, jsonify
import json  

# Configurations de la base de données (à remplacer par vos valeurs)
DATABASE = "nom_de_votre_base_de_donnees"
USER = "votre_user"
PASSWORD = "votre_mot_de_passe"
HOST = "localhost"  # ou l'adresse du service dans docker-compose
PORT = "5432"


def decode_and_store(encoded_data, table_name):
    # Premièrement, décoder depuis Base64
    base64_decoded_bytes = base64.b64decode(encoded_data)

    # Ensuite, décompresser les données MessagePack
    decoded_data = msgpack.unpackb(base64_decoded_bytes)
    
    # Convertir les données JSON en texte
    data_text = json.dumps(decoded_data)
    
    # Insérer les données textuelles dans la base de données PostgreSQL
    conn = psycopg2.connect(dbname=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    cur = conn.cursor()
    
    # La requête SQL dépendra de la structure de votre table et des données
    insert_query = f"INSERT INTO {table_name} (column_name) VALUES %s;"
    
    # Exécuter la requête d'insertion avec les données sous forme de texte
    execute_values(cur, insert_query, [(data_text,)])
    
    # Valider la transaction
    conn.commit()
    
    # Fermer la connexion
    cur.close()
    conn.close()
    
    print("Données insérées avec succès.")

# Exemple d'utilisation
encoded_text = "VotreTexteEncodéEnBase64"
table_name = "nom_de_votre_table"
decode_and_store(encoded_text, table_name)
