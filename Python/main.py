from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('Index.html')

@app.route('/Login')
def login():
    return render_template('Login.html')

@app.route('/PaginaPrincipal')
def menu():
    return render_template('PaginaPrincipal.html')

@app.route('/VMV')
def VMV():
    return render_template('VMV.html')
@app.route('/Contactos')
def Cont():
    return render_template('Contactos.html')

if __name__ == '__main__':
    app.run(debug=True)
