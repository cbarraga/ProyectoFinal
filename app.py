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


@app.route('/RecuperarPassword', methods=['POST', 'GET'])
def RecuperarPassword():
    if request.method == 'GET':
        return render_template('RecuperarPassword.html')
    else:
        # validar el formulario
        if not True:
            # validación exitosa
            pass
        else:
            # validación incorrecta
            return render_template('RecuperarPassword.html')


@app.route('/NuevaPassword', methods=['POST', 'GET'])
def NuevaPassword():
    if request.method == 'GET':
        return render_template('NuevaPassword.html')
    else:
        # validar el formulario
        if not True:
            # validación exitosa
            pass
        else:
            # validación incorrecta
            return render_template('NuevaPassword.html')


if __name__ == '__main__':
    app.run(debug=True, port=8001)
