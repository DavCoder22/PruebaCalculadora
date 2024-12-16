from flask import Flask, request, render_template

app = Flask(__name__)

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    resultado = None
    if request.method == 'POST':
        a = float(request.form['a'])
        b = float(request.form['b'])
        operacion = request.form['operacion']

        if operacion == 'sumar':
            resultado = sumar(a, b)
        elif operacion == 'restar':
            resultado = restar(a, b)
        elif operacion == 'multiplicar':
            resultado = multiplicar(a, b)
        elif operacion == 'dividir':
            resultado = dividir(a, b)

    return render_template('calculadora.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
