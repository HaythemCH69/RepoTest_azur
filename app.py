from flask import Flask

# Créez une instance de l'application Flask
app = Flask(__name__)

# Définissez une route de base
@app.route('/')
def accueil():
    return 'Bienvenue sur mon site web !'

# Exécutez l'application Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)