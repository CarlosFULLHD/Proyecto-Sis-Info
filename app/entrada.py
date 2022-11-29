from flask import Blueprint, request, render_template, redirect, url_for, flash
from db import mysql
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

from datetime import datetime
entrada = Blueprint('entrada', __name__, template_folder='app/templates')


@entrada.route('/')
def Index():
    print("ODIOAKI")
    #return render_template('pruebaLogin/Login.html')
    #return render_template('Registro/Registro.html')
    return render_template('combi.html')
    #return render_template('PaginaPrincipal/Principal.html')

@entrada.route('/')
def Registro_Frame():
    
    return render_template('Registro/Registro.html')


@entrada.route('/')
def Login_Frame():
    return render_template('pruebaLogin/Login.html')

@entrada.route('/')
def Quitar_Frame():
    return render_template('quitar.html')





#para ir a menu de Combi
@entrada.route('/templates/combi.html')
def Combi():
    return render_template('combi.html')

#para ir a menu de Salchipapus
@entrada.route('/templates/salchipapus.html')
def Salchipapus():
    return render_template('salchipapus.html')

#para ir a menu de maito
@entrada.route('/templates/maito.html')
def maito():
    return render_template('maito.html')

#para ir a menu de pocho
@entrada.route('/templates/pocho.html')
def pocho():
    return render_template('pocho.html')

#para ir a "Inicio"
@entrada.route('/templates/index.html')
def irInicio():
    return render_template('index.html')

#para ir a  Registro
#############################
@entrada.route('/templates/Registro/Registro.html', methods=['GET', 'POST'])
def Registro():
    return render_template('/Registro/Registro.html')


#para volver a ATRAS desde Registro
#############################
@entrada.route('/templates/pruebaLogin/Login.html', methods=['GET', 'POST'])
def VolverAtras():
    return render_template('/pruebaLogin/Login.html')







#agregar productos

@entrada.route('/templates/carrito.html')
def Agregar_CombiBBQ():
    Agregar_carrito("CombiBBQ",33)
    return render_template('combi.html')
    
@entrada.route('/templates/carrito.html')
def Agregar_CombiBBQ():
    Agregar_carrito("CombiBBQ",33)
    return render_template('combi.html')




@entrada.route('/Paginaweb/index.html', methods=['GET', 'POST'])
def Iniciar_Sesion():
    if request.method == 'POST':
        print("Conexion")
        usuario = request.form['user']
        contra = request.form['pass']
        cur = mysql.connection.cursor()        
        cur.execute('Select count(nombreUsuario) from datosUsuario where nombreUsuario = %s and estado=1 group by nombreUsuario ', [usuario])
        data = cur.fetchone()
        cur.close()
        if not data:
            print("Este usuario no existe")
            return redirect(url_for('entrada.Login_Frame'))
        else:
            cur = mysql.connection.cursor()
            cur.execute('SELECT datosusuario.contrasenia  FROM datosusuario  WHERE datosusuario.nombreUsuario = %s ', [usuario])
            data = cur.fetchone()
            if contra==data[0]:
                print("accesso")
                cur.execute('SELECT tipocuenta.idTipoCuenta  FROM datosusuario INNER JOIN usuario ON datosusuario.usuario_idUsuario = usuario.idUsuario INNER JOIN tipocuenta ON usuario.tipoCuenta_idTipoCuenta = tipocuenta.idTipoCuenta  WHERE datosusuario.nombreUsuario = %s ', [usuario])
                data = cur.fetchone()
                cur.close()
                if data[0]==1:
                    return render_template('index.html', entrada=data)
                elif data[0]==3:
                    return render_template('admin.html', entrada=data)
            else:
                try:
                    return redirect(url_for('entrada.Login_Frame'))
                except Exception as e:
                    flash(e.args[1])
                    return redirect(url_for('entrada.Login_Frame'))
 
def ultimoreg(tabla):
    cadena="Select * from "+tabla
    cur = mysql.connection.cursor()        
    cur.execute(cadena)
    data = cur.fetchall()
    cur.close()
    if not data:
        return(0)
    else:
        for  row in data:
            i=0
            for columna in row:
                if i==0:
                    aux=columna
                i=i+1
        return(aux)         



def Agregar_carrito(prod,precio):
        print("carrito")
        id=ultimoreg("carrito")+1
        print (id)
        cur = mysql.connection.cursor()        
        cur.execute('SELECT sum(carrito.cantidad)  FROM carrito  WHERE carrito.Producto = %s group by carrito.cantidad>0', [prod])
        data = cur.fetchone()
        cur.close()
        
        if not data:
            cur = mysql.connection.cursor()        
            cur.execute('INSERT INTO carrito (Id_carrito, Producto, Cantidad, Precio) VALUES (%s, %s, %s, %s); ', (id,prod,1,precio))
            flash('Register Successfully')
            mysql.connection.commit()
            cur.close()
        else:
            aux=data[0]
            cur = mysql.connection.cursor()        
            cur.execute(' update carrito set carrito.cantidad= %s where carrito.producto= %s ', ((aux+1,prod)))
            flash('Carrito Updated Successfully')
            mysql.connection.commit()
            cur.close()


        


@entrada.route('/Registro/Registro.html', methods=['GET', 'POST'])
def Registro_Usuario():
    if request.method == 'POST':
        print("Registro")
        id=ultimoreg("usuario")+1
        print (id)
        usuario = request.form['user']
        contra = request.form['pass1']
        contra2 = request.form['pass2']
        mail = request.form['email']
        now = datetime.now()
        fecha=now.date()
        
        cur = mysql.connection.cursor()        
        cur.execute('Select count(nombreUsuario) from datosUsuario where nombreUsuario = %s and estado = 1 group by nombreUsuario ', [usuario])
        data = cur.fetchone()
        cur.close()
        if not data:
            if contra==contra2:
                cur = mysql.connection.cursor()        
                cur.execute('INSERT INTO usuario (idUsuario, tipoCuenta_idTipoCuenta, persona_idPersona, empresa_idEmpresa) VALUES (%s, %s, NULL, NULL); ', (id,1))
                flash('Register Successfully')
                mysql.connection.commit()
                cur.close()

                cur = mysql.connection.cursor()        
                cur.execute('INSERT INTO datosusuario (idDatosUsuario, nombreUsuario, contrasenia, fechaCreacion, estado, usuario_idUsuario) VALUES (%s, %s, %s, %s,1, %s);', (id,usuario,contra,fecha,id))
                flash('Register Successfully')
                mysql.connection.commit()
                cur.close()
                return render_template('index.html')
            else:
              print("Contraseñas no coinciden") 
              return redirect(url_for('entrada.Registro_Frame'))
        else:
            print("Este Usuario ya existe")
            return redirect(url_for('entrada.Registro_Frame'))







@entrada.route('/Paginaweb/quitar.html', methods=['GET', 'POST'])
def Quitar_Admin():
    if request.method == 'POST':
        print("quitar admin")
        
        usuario = request.form['user']
        
     
        print(usuario)
        cur = mysql.connection.cursor()        
        cur.execute('SELECT  datosusuario.nombreUsuario  FROM datosusuario INNER JOIN usuario ON datosusuario.usuario_idUsuario = usuario.idUsuario  WHERE usuario.tipoCuenta_idTipoCuenta = 3  AND datosusuario.nombreUsuario = %s ', [usuario])
        data = cur.fetchone()
        cur.close()
        if not data:
            print("Este usuario administrador no existe")
            return redirect(url_for('entrada.Quitar_Frame'))
        else:
            if data[0]==usuario:
                cur = mysql.connection.cursor()        
                cur.execute(' update datosusuario set datosusuario.estado=0 where datosusuario.nombreUsuario= %s ', [usuario])
                flash('Admin Updated Successfully')
                mysql.connection.commit()
                cur.close()
                
                print("Usuario Eliminado")
                return render_template('PaginaPrincipal/Principal.html', entrada=data)
                #return redirect(url_for('entrada.Quitar_Frame'))


    