# Utiliser une image Python comme base
FROM python:3.9

# Créer un répertoire pour l'application
WORKDIR /app

# Copier les fichiers de l'application
ADD requirements.txt .
ADD bot.py .

# Installer les dépendances
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

# Commande pour lancer l'application (bot ou admin)
# On peut spécifier si on lance le bot ou l'admin dans le docker-compose
CMD ["python", "bot.py"]
