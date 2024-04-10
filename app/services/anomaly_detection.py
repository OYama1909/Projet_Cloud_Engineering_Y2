import base64
import psycopg2
from psycopg2.extras import execute_values

# Configurations de la base de données (à remplacer par vos valeurs)
DATABASE = "nom_de_votre_base_de_donnees"
USER = "votre_user"
PASSWORD = "votre_mot_de_passe"
HOST = "localhost"  # ou l'adresse du service dans docker-compose
PORT = "5432"

def decode_and_store(encoded_data, table_name):
    # Décoder les données en base64
    decoded_bytes = base64.b64decode(encoded_data)
    decoded_str = decoded_bytes.decode('utf-8')  # Supposer que le texte est en utf-8
    
    # Convertir la chaîne décodée en structure de données Python si nécessaire
    # Par exemple, si la chaîne décodée est du JSON
    # data = json.loads(decoded_str)
    
    # Dans cet exemple, on suppose que decoded_str est simplement un texte à stocker
    data_to_insert = decoded_str
    
    # Insérer les données dans la base de données PostgreSQL
    conn = psycopg2.connect(dbname=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    cur = conn.cursor()
    
    # La requête SQL dépendra de la structure de votre table et des données
    insert_query = f"INSERT INTO {table_name} (column_name) VALUES %s;"
    
    # Exécuter la requête d'insertion
    execute_values(cur, insert_query, [(data_to_insert,)])
    
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
