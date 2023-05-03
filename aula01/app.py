from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template('pagina_inicial.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/experiencia')
def experiencia():
    return render_template('experiencia.html')

@app.route('/formacao')
def formacao():
    return render_template('formacao.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)