from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/ver")
def saludar():
    return "<h1>Hola mundo</h1>"

@app.route("/hora")
def hora():
    # Obtiene la hora actual
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>La hora actual es: {ahora}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
