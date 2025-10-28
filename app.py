from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Función para conectarse a la base de datos
def get_db_connection():
    conn = sqlite3.connect('vehiculos.db')
    conn.row_factory = sqlite3.Row
    return conn

# Página principal
@app.route('/')
def index():
    conn = get_db_connection()
    vehiculos = conn.execute('SELECT * FROM vehiculos').fetchall()
    conn.close()
    return render_template('index.html', vehiculos=vehiculos)

# Página para agregar un nuevo registro
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        patente = request.form['patente']
        marca = request.form['marca']
        modelo = request.form['modelo']
        servicio = request.form['servicio']
        fecha = request.form['fecha']
        costo = request.form['costo']

        conn = get_db_connection()
        conn.execute('INSERT INTO vehiculos (patente, marca, modelo, servicio, fecha, costo) VALUES (?, ?, ?, ?, ?, ?)',
                     (patente, marca, modelo, servicio, fecha, costo))
        conn.commit()
        conn.close()
        return redirect('/')

    return render_template('agregar.html')

if __name__ == '__main__':
    app.run(debug=True)
