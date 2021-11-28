
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,BLOB,ForeignKey,Float,Date
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/chiptune'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Producto(db.Model):
    __tablename__='productos'
    idProducto=Column(Integer,primary_key=True)
    Nombre=Column(String)
    Caracteristicas=Column(String)
    Precio=Column(Float)

    def consultaIndividual(self, id):
        return Producto.query.get(id)

    def consultaGeneral(self):
        return self.query.all()

    def agregar(self):
        db.session.add(self)
        db.session.commit()

    def editar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        p = self.consultaIndividual(id)
        db.session.delete(p)
        db.session.commit()

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
    for U in datos:
        if U==nombre and p == contras[cont]:
            return render_template('PaginaPrincipal.html',Usuarios=U)
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

@app.route('/EliminarProducto/<U>')
def eliminarproducts(U):
    prod = Producto()
    prods = prod.consultaGeneral()
    return render_template('Eliminar.html',Usuarios=U,producto=prods)

@app.route('/ModificarProducto/<U>')
def modificarproducts(U):
    prod = Producto()
    prods = prod.consultaGeneral()
    return render_template('ModificarProd.html',Usuarios=U,producto=prods)

@app.route('/ConsultarProducto/<U>')
def consultarproducts(U):
    prod=Producto()
    prods=prod.consultaGeneral()
    return render_template('ConsultarProducto.html',Usuarios=U,producto=prods)

@app.route('/actualizarProducto/<U>/<id>')
def actualizarProd(U,id):
    prod = Producto()
    prod = prod.consultaIndividual(id)
    return render_template('Modificar.html',Usuarios=U,producto=prod)

@app.route('/ModificarP/<U>',methods=['post'])
def modificarProd(U):
    NumProducto = request.form['claveP']
    NombreProducto = request.form['nombreP']
    Caracteristicas = request.form['CaraP']
    precioP = request.form['precioP']

    prod = Producto()
    prod.idProducto = NumProducto
    prod.Nombre = NombreProducto
    prod.Caracteristicas = Caracteristicas
    prod.Precio = precioP
    prod.editar()
    prods = prod.consultaGeneral()
    return render_template('ConsultarProducto.html', Usuarios=U, producto=prods)

@app.route('/eliminarProducto/<U>/<id>')
def eliminarProd(U,id):
    prod = Producto()
    prod.eliminar(id)
    prods = prod.consultaGeneral()
    return render_template('ConsultarProducto.html',Usuarios=U,productos=prods)

@app.route('/GuardarProducto/<U>' ,methods=['post'])
def guardarproducts(U):
   NumProducto= request.form['claveP']
   NombreProducto = request.form['NombreP']
   Caracteristicas = request.form['CaraP']
   precioP = request.form['precioP']
   producto = [NumProducto,
               NombreProducto,
               Caracteristicas,
               precioP]

   prod = Producto()
   prod.idProducto = NumProducto
   prod.Nombre = NombreProducto
   prod.Caracteristicas = Caracteristicas
   prod.Precio = precioP
   prod.agregar()
   return render_template('productoGuardado.html',Usuarios=U,producto=producto)

if __name__ == '__main__':
    app.run(debug=True)
