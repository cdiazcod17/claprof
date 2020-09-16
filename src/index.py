from flask import Flask, render_template, request
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

@app.route('/add_user', methods=['POST'])
def add_User():
    if request.method == 'POST':
        usuario = request.form['usuario']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        password = request.form['password']
        email = request.form['email']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        ciudad = request.form['ciudad']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuarios (Nombre, Apellido, Email, Usuario,Telefono,Password,Direccion,id_Ciudad) VALUES(%s, %s, %s,%s,%s,%s,%s,%s)',(nombres,apellidos,email,usuario,telefono,password,direccion,ciudad))
        mysql.connection.commit()
        return "received"

#comprobar si estamos en el archivo principal
if __name__ == '__main__':
    app.run(debug=True)#debug sirve para que al actualizar el codigo se reinicie el servidor