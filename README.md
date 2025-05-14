# Projet Flask minimal

Ce projet est une base pour une application Flask avec :
- Un dossier `static/` pour les fichiers statiques (CSS, JS, images)
- Un dossier `templates/` pour les templates HTML
- Un fichier `app.py` qui lance un Hello World via un template
- Une fonction de connexion à une base SQLite

## Lancer le projet

1. Installez Flask si besoin :
   
   ```bash
   pip install flask
   ```

2. Lancez l'application :
   
   ```bash
   python app.py
   ```

3. Rendez-vous sur http://127.0.0.1:5000/

## Structure

- `app.py` : point d'entrée de l'application
- `templates/hello.html` : template HTML affichant "Hello World"
- `static/` : dossier pour les fichiers statiques
