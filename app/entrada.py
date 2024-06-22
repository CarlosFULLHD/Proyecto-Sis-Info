import pymysql
from flask import Blueprint, session, request, render_template, redirect, url_for, flash
from db import mysql
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

from datetime import datetime
entrada = Blueprint('entrada', __name__, template_folder='app/templates')


@entrada.route('/')
def Index():
    print("ODIOAKI")
    # return render_template('pruebaLogin/Login.html')
    # return render_template('Registro/Registro.html')
    return render_template('index.html')
    # return render_template('PaginaPrincipal/Principal.html')


@entrada.route('/')
def Registro_Frame():

    return render_template('Registro/Registro.html')


@entrada.route('/')
def Login_Frame():
    return render_template('pruebaLogin/Login.html')


@entrada.route('/')
def Quitar_Frame():
    return render_template('quitar.html')


@entrada.route('/templates/contactanos.html')
def Contactanos():
    return render_template('contactanos.html')


###############################
# para ir a CarritoTEMPORAL
# 33
@entrada.route('/templates/carrito.html')
def irCarrito():
    add_product_to_cart()
    return render_template('carrito.html')


# para ir a menu de Combi
@entrada.route('/templates/combi.html')
def Combi():
    return render_template('combi.html')

# para ir a menu de Salchipapus


@entrada.route('/templates/salchipapus.html')
def Salchipapus():
    return render_template('salchipapus.html')

# para ir a menu de maito


@entrada.route('/templates/maito.html')
def maito():
    return render_template('maito.html')

# para ir a menu de pocho


@entrada.route('/templates/pocho.html')
def pocho():
    return render_template('pocho.html')

# para ir a "Inicio"


@entrada.route('/templates/index.html')
def irInicio():
    return render_template('index.html')

# para ir a  Registro
#############################


@entrada.route('/templates/Registro/Registro.html', methods=['GET', 'POST'])
def Registro():
    return render_template('/Registro/Registro.html')


# para volver a ATRAS desde Registro
#############################
@entrada.route('/templates/pruebaLogin/Login.html', methods=['GET', 'POST'])
def VolverAtras():
    return render_template('/pruebaLogin/Login.html')

# para ir a "registroadmin" HREF


@entrada.route('/templates/registroadmin.html')
def regisAdmin():
    return render_template('registroadmin.html')

# para ir a "quitar"


@entrada.route('/templates/quitar.html')
def quitarAdmin():
    return render_template('quitar.html')


# para ir a "ATRAS" en quitar
@entrada.route('/templates/admin.html')
def atrasQuitar():
    return render_template('admin.html')

# para ir a "ATRAS" en RegistroAdmin with BUTTON


@entrada.route('/templates/admin.html', methods=['GET', 'POST'])
def atrasRegistro():
    return render_template('admin.html')

# para ir a Restaurante


@entrada.route('/templates/restaurantes.html')
def irRestaurantes():
    return render_template('restaurantes.html')


# agregar productos

@entrada.route('/templates/carrito_combi.html')
def Agregar_CombiClasicaQ():
    print("clasica")
    Agregar_carrito("Combi Clasica", 30, "hclasica.png")
    return render_template('combi.html')


@entrada.route('/templates/carrito_combibbq.html')
def Agregar_CombiBbq():
    print("bbq")
    Agregar_carrito("Combi BBQ", 33, "hbbq.png")
    return render_template('combi.html')


@entrada.route('/templates/carrito_combihongos.html')
def Agregar_CombiHongos():
    print("hongos")
    Agregar_carrito("Combi Hongos", 33, "hongos.png")
    return render_template('combi.html')


@entrada.route('/templates/carrito_combimexican.html')
def Agregar_CombiMexican():
    print("mexican")
    Agregar_carrito("Mexican Combi", 32, "hmexicana.png")
    return render_template('combi.html')


@entrada.route('/templates/carrito_combibuffalo.html')
def Agregar_CombiBuffalo():
    print("buffalo")
    Agregar_carrito("Combi Buffalo", 35, "hclasica.png")
    return render_template('combi.html')


@entrada.route('/templates/carrito_combi4quesos.html')
def Agregar_Combi4Quesos():
    print("4quesos")
    Agregar_carrito("Combi 4 Quesos", 35, "hclasica.png")
    return render_template('combi.html')


@entrada.route('/templates/carrito_maito.html')
def Agregar_ArrozChaufa():
    Agregar_carrito("Arroz Chaufa", 27, "arrozchaufa.png")
    return render_template('maito.html')


@entrada.route('/templates/carrito_maito_tallarin_salteado.html')
def Agregar_TallarinSalteado():
    Agregar_carrito("Tallarin Salteado", 27, "tallarinsalteado.png")
    return render_template('maito.html')


@entrada.route('/templates/carrito_maito_aereopuerto.html')
def Agregar_Aerepuerto():
    Agregar_carrito("Aerepuerto", 27, "tallarinsalteado.png")
    return render_template('maito.html')


@entrada.route('/templates/carrito_maito_kungpao.html')
def Agregar_KungPao():
    Agregar_carrito("Kung Pao", 35, "kungpao.png")
    return render_template('maito.html')


@entrada.route('/templates/carrito_maito_lomosalteado.html')
def Agregar_LomoSalteado():
    Agregar_carrito("Lomo Salteado", 35, "lomosalteado.png")
    return render_template('maito.html')


@entrada.route('/templates/carrito_maito_costillacerdo.html')
def Agregar_CostillaCerdo():
    Agregar_carrito("Costilla de Cerdo", 37, "costilladecerdo.png")
    return render_template('maito.html')


@entrada.route('/templates/carrito_pocho.html')
def Agregar_PipocasPollo():
    Agregar_carrito("Pipocas de Pollo", 23, "pipocasdepollo.png")
    return render_template('pocho.html')


@entrada.route('/templates/carrito_pocho_cuartopollo.html')
def Agregar_CuartoPollo():
    Agregar_carrito("Cuarto de pollo", 25, "cuartodepollo.png")
    return render_template('pocho.html')


@entrada.route('/templates/carrito_octavopollo.html')
def Agregar_OctavoPollo():
    Agregar_carrito("Octavo de pollo", 18, "octavodepollo.png")
    return render_template('pocho.html')


@entrada.route('/templates/carrito_salchipapus.html')
def Agregar_Salchipapu():
    Agregar_carrito("Salchipapu Tradicional", 18, "ssalchipapu.png")
    return render_template('salchipapus.html')


@entrada.route('/templates/carrito_salchipapu_argentina.html')
def Agregar_Salchipapu_Argentina():
    Agregar_carrito("Salchipapu Aregtina", 23, "sargentina.png")
    return render_template('salchipapus.html')


@entrada.route('/templates/carrito_salchipapu_mexicana.html')
def Agregar_Salchipapu_Mexicana():
    Agregar_carrito("Salchipapu Mexicana", 23, "smexicana.png")
    return render_template('salchipapus.html')


@entrada.route('/templates/carrito_salchipapu_peruana.html')
def Agregar_Salchipapu_Peruana():
    Agregar_carrito("Salchipapu Peruana", 23, "speruana.png")
    return render_template('salchipapus.html')


@entrada.route('/templates/carrito_salchipapu_cerdo.html')
def Agregar_Salchipapu_Cerdo():
    Agregar_carrito("Salchipapu Cerdo", 23, "scerdo.png")
    return render_template('salchipapus.html')


@entrada.route('/templates/carrito_salchipapu_4quesos.html')
def Agregar_Salchipapu_4Quesos():
    Agregar_carrito("Salchipapu 4 Quesos", 35, "s4quesos.png")
    return render_template('salchipapus.html')


def add_product_to_cart():
    cursor = None
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM carrito")
        data = cursor.fetchone()

        itemArray = {data[0]: {'name': data[1], 'code': data[0], 'quantity': data[2],
                               'price': data[3], 'total_price': (data[3]*data[2]), 'image': data[4]}}
        print(itemArray)
        session['cart_item'] = itemArray
        cantidad_total = data[2]
        precio_total = data[3]*data[2]
        aux1 = cantidad_total
        aux2 = precio_total
        cursor.close()
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM carrito")
        data = cursor.fetchall()

        cursor.close()
        for row in data:

            itemArray = {row[0]: {'name': row[1], 'code': row[0], 'quantity': row[2],
                                  'price': row[3], 'total_price': (row[3]*row[2]), 'image': row[4]}}

            session['cart_item'] = array_merge(session['cart_item'], itemArray)
            cantidad_total = cantidad_total+row[2]
            precio_total = precio_total+(row[3]*row[2])
            print(cantidad_total, "   ", precio_total)

        cantidad_total = cantidad_total-aux1
        precio_total = precio_total-aux2
        session['all_total_quantity'] = cantidad_total
        session['all_total_price'] = precio_total
        print(session['cart_item'])
        return redirect(url_for('.carrito_frame'))
    except Exception as e:
        print(e)


@entrada.route('/templates/carrito.html')
def carrito_frame():
    try:
        return render_template('carrito.html')
    except Exception as e:
        print(e)


@entrada.route('/empty')
def empty_cart():
    try:
        cur = mysql.connection.cursor()
        cur.execute('delete from carrito; ')
        flash('Register Successfully')
        mysql.connection.commit()
        cur.close()
        session.clear()
        return redirect(url_for('.carrito_frame'))
    except Exception as e:
        print(e)


@entrada.route('/delete/<string:code>')
def delete_product(code):
    try:
        all_total_price = 0
        all_total_quantity = 0
        session.modified = True

        for item in session['cart_item'].items():
            if item[0] == code:
                session['cart_item'].pop(item[0], None)
                if 'cart_item' in session:
                    for key, value in session['cart_item'].items():
                        individual_quantity = int(
                            session['cart_item'][key]['quantity'])
                        individual_price = float(
                            session['cart_item'][key]['total_price'])
                        all_total_quantity = all_total_quantity + individual_quantity
                        all_total_price = all_total_price + individual_price
                break

        if all_total_quantity == 0:
            session.clear()
        else:
            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price

        # return redirect('/')
        cur = mysql.connection.cursor()
        cur.execute('delete from carrito where Id_carrito=%s; ', code)
        flash('Register Successfully')
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('.carrito_frame'))
    except Exception as e:
        print(e)


def array_merge(first_array, second_array):
    if isinstance(first_array, list) and isinstance(second_array, list):
        return first_array + second_array
    elif isinstance(first_array, dict) and isinstance(second_array, dict):
        return dict(list(first_array.items()) + list(second_array.items()))
    elif isinstance(first_array, set) and isinstance(second_array, set):
        return first_array.union(second_array)
    return False


@entrada.route('/Paginaweb/index.html', methods=['GET', 'POST'])
def Iniciar_Sesion():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute('delete from carrito; ')
        flash('Register Successfully')
        mysql.connection.commit()
        cur.close()

        print("Conexion")
        usuario = request.form['user']
        contra = request.form['pass']
        cur = mysql.connection.cursor()
        cur.execute(
            'Select count(nombreUsuario) from datosUsuario where nombreUsuario = %s and estado=1 group by nombreUsuario ', [usuario])
        data = cur.fetchone()
        cur.close()
        if not data:
            print("Este usuario no existe")
            return redirect(url_for('entrada.Login_Frame'))
        else:
            cur = mysql.connection.cursor()
            cur.execute(
                'SELECT datosusuario.contrasenia  FROM datosusuario  WHERE datosusuario.nombreUsuario = %s ', [usuario])
            data = cur.fetchone()
            if contra == data[0]:
                print("accesso")
                cur.execute(
                    'SELECT tipocuenta.idTipoCuenta  FROM datosusuario INNER JOIN usuario ON datosusuario.usuario_idUsuario = usuario.idUsuario INNER JOIN tipocuenta ON usuario.tipoCuenta_idTipoCuenta = tipocuenta.idTipoCuenta  WHERE datosusuario.nombreUsuario = %s ', [usuario])
                data = cur.fetchone()
                cur.close()
                if data[0] == 1:
                    return render_template('index.html', entrada=data)
                elif data[0] == 3:
                    return render_template('admin.html', entrada=data)
            else:
                try:
                    return redirect(url_for('entrada.Login_Frame'))
                except Exception as e:
                    flash(e.args[1])
                    return redirect(url_for('entrada.Login_Frame'))


def ultimoreg(tabla):

    cadena = "Select * from "+tabla
    cur = mysql.connection.cursor()
    cur.execute(cadena)
    data = cur.fetchall()
    print(data)
    cur.close()

    if not data:
        return (0)
    else:
        for row in data:
            i = 0
            for columna in row:
                if i == 0:
                    aux = columna
                i = i+1

        return (aux)


def Agregar_carrito(prod, precio, dir):
    print("carrito")
    print(ultimoreg("carrito"))
    id = ultimoreg("carrito")+1
    print(id)
    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT sum(carrito.cantidad)  FROM carrito  WHERE carrito.Producto = %s group by carrito.cantidad>0', [prod])
    data = cur.fetchone()
    print(data)
    cur.close()

    if not data:
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO carrito (Id_carrito, Producto, Cantidad, Precio,Dir_imagen) VALUES (%s, %s, %s, %s,%s); ',
                    (id, prod, 1, precio, dir))
        flash('Register Successfully')
        mysql.connection.commit()
        cur.close()
    else:
        aux = data[0]
        cur = mysql.connection.cursor()
        cur.execute(
            ' update carrito set carrito.cantidad= %s where carrito.producto= %s ', ((aux+1, prod)))
        flash('Carrito Updated Successfully')
        mysql.connection.commit()
        cur.close()


@entrada.route('/Registro/Registro.html', methods=['GET', 'POST'])
def Registro_Usuario():
    if request.method == 'POST':
        print("Registro")
        id = ultimoreg("usuario")+1
        print(id)
        usuario = request.form['user']
        contra = request.form['pass1']
        contra2 = request.form['pass2']
        mail = request.form['email']
        now = datetime.now()
        fecha = now.date()

        cur = mysql.connection.cursor()
        cur.execute(
            'Select count(nombreUsuario) from datosUsuario where nombreUsuario = %s and estado = 1 group by nombreUsuario ', [usuario])
        data = cur.fetchone()
        cur.close()
        if not data:
            if contra == contra2:
                cur = mysql.connection.cursor()
                cur.execute(
                    'INSERT INTO usuario (idUsuario, tipoCuenta_idTipoCuenta, persona_idPersona, empresa_idEmpresa) VALUES (%s, %s, NULL, NULL); ', (id, 1))
                flash('Register Successfully')
                mysql.connection.commit()
                cur.close()

                cur = mysql.connection.cursor()
                cur.execute('INSERT INTO datosusuario (idDatosUsuario, nombreUsuario, contrasenia, fechaCreacion, estado, usuario_idUsuario) VALUES (%s, %s, %s, %s,1, %s);',
                            (id, usuario, contra, fecha, id))
                flash('Register Successfully')
                mysql.connection.commit()
                cur.close()
                return render_template('index.html')
            else:
                print("Contraseñas no coinciden")
                return redirect(url_for('entrada.regisAdmin'))
        else:
            print("Este Usuario ya existe")
            return redirect(url_for('entrada.regisAdmin'))


@entrada.route('/Registro/Registro_admin.html', methods=['GET', 'POST'])
def Registro_Admin():
    if request.method == 'POST':
        print("Registro Admin")
        id = ultimoreg("usuario")+1
        print(id)
        usuario = request.form['user']
        contra = request.form['pass1']
        contra2 = request.form['pass2']
        mail = request.form['email']
        now = datetime.now()
        fecha = now.date()

        cur = mysql.connection.cursor()
        cur.execute(
            'Select count(nombreUsuario) from datosUsuario where nombreUsuario = %s and estado = 3 group by nombreUsuario ', [usuario])
        data = cur.fetchone()
        cur.close()
        if not data:
            if contra == contra2:
                cur = mysql.connection.cursor()
                cur.execute(
                    'INSERT INTO usuario (idUsuario, tipoCuenta_idTipoCuenta, persona_idPersona, empresa_idEmpresa) VALUES (%s, %s, NULL, NULL); ', (id, 3))
                flash('Register Successfully')
                mysql.connection.commit()
                cur.close()

                cur = mysql.connection.cursor()
                cur.execute('INSERT INTO datosusuario (idDatosUsuario, nombreUsuario, contrasenia, fechaCreacion, estado, usuario_idUsuario) VALUES (%s, %s, %s, %s,1, %s);',
                            (id, usuario, contra, fecha, id))
                flash('Register Successfully')
                mysql.connection.commit()
                cur.close()
                return redirect(url_for('entrada.atrasRegistro'))
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
        cur.execute(
            'SELECT  datosusuario.nombreUsuario  FROM datosusuario INNER JOIN usuario ON datosusuario.usuario_idUsuario = usuario.idUsuario  WHERE usuario.tipoCuenta_idTipoCuenta = 3  AND datosusuario.nombreUsuario = %s ', [usuario])
        data = cur.fetchone()
        cur.close()
        if not data:
            print("Este usuario administrador no existe")
            return redirect(url_for('entrada.Quitar_Frame'))
        else:
            if data[0] == usuario:
                cur = mysql.connection.cursor()
                cur.execute(
                    ' update datosusuario set datosusuario.estado=0 where datosusuario.nombreUsuario= %s ', [usuario])
                flash('Admin Updated Successfully')
                mysql.connection.commit()
                cur.close()

                print("Usuario Eliminado")
                return redirect(url_for('entrada.atrasRegistro'))
                # return redirect(url_for('entrada.Quitar_Frame'))
