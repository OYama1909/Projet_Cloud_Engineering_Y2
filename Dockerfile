# Utiliser une image de base officielle Python
FROM python:3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances et installer les dépendances
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers du projet dans le répertoire de travail
COPY . .

# Exposer le port que votre application utilise
EXPOSE 5000

# Commande pour lancer l'application
CMD ["flask", "run", "--host=0.0.0.0"]
