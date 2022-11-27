from flask import Blueprint, request, render_template, redirect, url_for, flash
from db import mysql
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
contacts = Blueprint('contacts', __name__, template_folder='app/templates')


@contacts.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM datosusuario')
    data = cur.fetchall()
    cur.close()
    return render_template('pruebaLogin/Login.html', contacts=data)

def is_empty(a):
    return a == set()




@contacts.route('/Paginaweb/index.html', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        print("Conexion")
        usuario = request.form['user']
        contra = request.form['pass']
        cur = mysql.connection.cursor()        
        cur.execute('Select count(nombreUsuario) from datosUsuario where nombreUsuario = %s group by nombreUsuario ', [usuario])
        data = cur.fetchone()
        cur.close()
        print(data)
        if not data:
            print("Este usuario no existe")
        else:
            cur = mysql.connection.cursor()
            cur.execute('SELECT datosusuario.contrasenia  FROM datosusuario  WHERE datosusuario.nombreUsuario = %s ', [usuario])
            data = cur.fetchone()
            if contra==data[0]:
                print("accesso")
                return render_template('PaginaPrincipal/Principal.html', contacts=data)
                try:
                     return redirect(url_for('/PaginaPrincipal/PaginaPrincipal.html'))
                except Exception as e:
                    flash(e.args[1])
                    return redirect(url_for('contacts.Index'))
            else:
                print("Contrasenia incorrecta")

        
  


            
        try:
            return redirect(url_for('contacts.Index'))
        except Exception as e:
            flash(e.args[1])
            return redirect(url_for('contacts.Index'))


@contacts.route('/edit/<id>', methods=['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-contact.html', contact=data[0])


@contacts.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET fullname = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        """, (fullname, email, phone, id))
        flash('Contact Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('contacts.Index'))


@contacts.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('contacts.Index'))
