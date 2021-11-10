
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('Index.html')

@app.route('/Login')
def login():
    return render_template('Login.html')

@app.route('/PaginaPrincipal',methods=['post'])
def menu():
    nombre=request.form['Usuarios']
    p=request.form['contra']
    datos=['Pedro','Hugo','Jessi']
    contras=['123','456','789']
    cont=0
    for u in datos:
        if u==nombre and p == contras[cont]:
            return render_template('PaginaPrincipal.html',Usuarios=u)
        cont=cont+1
    return render_template('Login.html',mensaje='Usuarios no registrado')

@app.route('/VMV')
def VMV():
    return render_template('VMV.html')

@app.route('/AVISOPTC')
def aviso():
    return render_template('AVISOPTC.html')

@app.route('/Contactos')
def Cont():
    return render_template('Contactos.html')

@app.route('/RedesSociales')
def Redes():
    return render_template('RedesSociales.html')

@app.route('/productos/<U>')
def products(U):
    return render_template('MenuProductos.html',Usuarios=U)

@app.route('/AgregarProducto/<U>')
def agregarproducts(U):
    return render_template('AgregarProducto.html',Usuarios=U)

@app.route('/GuardarProducto/<U>' ,methods=['post'])
def guardarproducts(U):
   NumProducto= request.form['ClaveP']
   NombreProducto = request.form['NombreP']
   Descripcion = request.form['descP']
   producto = [NumProducto,
               NombreProducto,
               Descripcion]
   return render_template('productoGuardado.html',Usuarios=U,producto=producto)

if __name__ == '__main__':
    app.run(debug=True)
