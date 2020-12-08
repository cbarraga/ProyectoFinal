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
        if True:
            # validación exitosa
            pass
        else:
            # validación incorrecta
            return render_template('registro.html')


if __name__ == '__main__':
    app.run(debug=True, port=8001)
