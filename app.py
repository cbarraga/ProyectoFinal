from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registrar', methods=['POST', 'GET'])
def registar():
    if request.method == 'GET':
        return render_template('registro.html')
    else:
        # validar el formulario
        if not True:
            # validación exitosa
            pass
        else:
            # validación incorrecta
            return render_template('registro.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # validar el formulario
        if not True:
            # validación exitosa
            pass
        else:
            # validación incorrecta
            return render_template('login.html')


@app.route('/recuperarPassword', methods=['POST', 'GET'])
def recuperarPassword():
    if request.method == 'GET':
        return render_template('recuperarPassword.html')
    else:
        # validar el formulario
        if not True:
            # validación exitosa
            pass
        else:
            # validación incorrecta
            return render_template('recuperarPassword.html')


@app.route('/nuevaPassword', methods=['POST', 'GET'])
def nuevaPassword():
    if request.method == 'GET':
        return render_template('nuevaPassword.html')
    else:
        # validar el formulario
        if not True:
            # validación exitosa
            pass
        else:
            # validación incorrecta
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
