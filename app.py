from flask import Flask, render_template, url_for
import sqlite3

app = Flask(__name__)

# Conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Ruta principal
@app.route('/')
def index():
    conn = get_db_connection()
    vehiculos = conn.execute('SELECT * FROM vehiculos').fetchall()
    servicios = conn.execute('SELECT * FROM servicios').fetchall()
    conn.close()
    return render_template('index.html', vehiculos=vehiculos, servicios=servicios)

if __name__ == '__main__':
    app.run(debug=True)