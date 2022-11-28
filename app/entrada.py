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
    return render_template('quitar.html')
    #return render_template('PaginaPrincipal/Principal.html')

@entrada.route('/')
def Registro_Frame():
    return render_template('Registro/Registro.html')


@entrada.route('/')
def Login_Frame():
    return render_template('pruebaLogin/Login.html')




#salkdejals






@entrada.route('/Paginaweb/index.html', methods=['GET', 'POST'])
def Iniciar_Sesion():
    if request.method == 'POST':
        print("Conexion")
        usuario = request.form['user']
        contra = request.form['pass']
        cur = mysql.connection.cursor()        
        cur.execute('Select count(nombreUsuario) from datosUsuario where nombreUsuario = %s group by nombreUsuario ', [usuario])
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
                return render_template('PaginaPrincipal/Principal.html', entrada=data)
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
    for  row in data:
        i=0
        for columna in row:
            if i==0:
                aux=columna
            i=i+1
    return(aux)         



@entrada.route('/Registro/Registro.html', methods=['GET', 'POST'])
def Registro_Usuario():
    if request.method == 'POST':
        print("Registro")
        id=ultimoreg("usuario")+1
        usuario = request.form['user']
        contra = request.form['pass1']
        contra2 = request.form['pass2']
        mail = request.form['email']
        now = datetime.now()
        fecha=now.date()
        
        cur = mysql.connection.cursor()        
        cur.execute('Select count(nombreUsuario) from datosUsuario where nombreUsuario = %s group by nombreUsuario ', [usuario])
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
                return render_template('PaginaPrincipal/Principal.html')
            else:
              print("Contraseñas no coinciden") 
              return redirect(url_for('entrada.Registro_Frame'))
        else:
            print("Este Usuario ya existe")
            return redirect(url_for('entrada.Registro_Frame'))



        
        
       
 
    

@entrada.route('/edit/<id>', methods=['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM entrada WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-contact.html', contact=data[0])


@entrada.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE entrada
            SET fullname = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        """, (fullname, email, phone, id))
        flash('Contact Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('entrada.Index'))


@entrada.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM entrada WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('entrada.Index'))

    