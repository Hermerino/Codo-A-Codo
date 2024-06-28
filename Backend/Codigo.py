from flask import Flask

app = Flask(__name__)   # Crea una instancia de la clase Flask 

@app.route('/')         # Crea una ruta para la raiz
def index():
    return 'Hello, World!' 

app.run()
