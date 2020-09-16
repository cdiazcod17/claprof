from flask import Flask, render_template
from flask_mysqldb import MySQL

#creo objeto para crear rutas
app = Flask(__name__)
#conexion a la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'claprofdb'
mysql = MySQL(app)

#crear rutaS
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register')
def register():
    return render_template('register.html')

#comprobar si estamos en el archivo principal
if __name__ == '__main__':
    app.run(debug=True)#debug sirve para que al actualizar el codigo se reinicie el servidor