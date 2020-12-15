import os
from flask import Flask, render_template, request, flash, session
from formulario import formBlog, formLogin, formRegistro
import sqlite3
from markupsafe import escape
import hashlib
import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar')
def registrar():
    return render_template("registro.html")
@app.route("/registrar", methods=['POST'])
def registar_save():
    form = formRegistro()
    if request.method == "POST":
        nombres = request.form["nombre"]
        apellidos = request.form["apellido"]
        email = request.form["email"]
        contrasena = request.form["passw"]
        contrasena2= request.form["passver"]
        if (contrasena!=contrasena2):
            error = "Las contraseñas no coinciden."
            flash(error)
            return render_template("registro.html")
        encrip=hashlib.md5(contrasena.encode())
        consenc=encrip.hexdigest()
        tiempo=datetime.datetime.now
        with sqlite3.connect("ProyectoFinalDB.db") as con:
            try:
                cur = con.cursor()
                cur.execute("INSERT INTO Usuarios (Nombres, Apellidos, Correo, Contrasena) VALUES (?,?,?,?)",
                            (nombres, apellidos, email, consenc))
                con.commit()
                
                return 'Guardado Satisfactoriamente'
            except:
                con.rollback()
        error ="No se pudo guardar"
        return flash(error) 


@app.route('/login')
def login():
    form = formLogin()
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
    form = formLogin()
    usuario = request.form["email"]
    contrasena = request.form["password"]
    encrip=hashlib.md5(contrasena.encode())
    consenc=encrip.hexdigest()

    with sqlite3.connect("ProyectoFinalDB.db") as con:
        try:
            cur = con.cursor()
            cur.execute("SELECT * FROM usuario WHERE email = ? AND Contrasena = ? ", [usuario, consenc])
            if cur.fetchone():
                session["usuario"] = usuario #Creo la variable de sesion
                #return 'Usuario logeado'
                return render_template("Blogs.html", form=form)
        except:
            con.rollback()
    return 'Usuario no permitido'


@app.route('/recuperarPassword', methods=['POST'])
def recuperarPassword():
    return render_template('recuperarPassword.html')
    


@app.route('/nuevaPassword', methods=['POST'])
def nuevaPassword():
    return render_template('nuevaPassword.html')
    


@app.route('/Blogs')
def Blogs():
    return render_template('Blogs.html')


@app.route('/crearBlog', methods=['POST', 'GET'])
def crearBlog():
    if request.method == 'GET':
        return render_template('crearBlog.html')
    else:
        # validar el formulario
        if not True:
            # validación exitosa
            pass
        else:
            # validación incorrecta
            return render_template('crearBlog.html')


if __name__ == '__main__':
    app.run(debug=True, port=8001)
