from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Création de l'instance de l'application Flask
app = Flask(__name__)

# Configuration de l'URI de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db/service_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de l'objet SQLAlchemy avec l'application Flask
db = SQLAlchemy(app)

# Définition d'un modèle pour SQLAlchemy
class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    # Ajoutez d'autres champs nécessaires

# Assurez-vous que cette partie ne s'exécute que si ce script est le point d'entrée principal
if __name__ == '__main__':
    # Création des tables dans la base de données
    with app.app_context():
        db.create_all()
    # Vous pouvez ajouter d'autres commandes pour démarrer votre application ici
