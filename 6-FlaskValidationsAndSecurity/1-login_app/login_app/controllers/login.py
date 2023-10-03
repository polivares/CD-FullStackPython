from login_app import app
from login_app.models.usuario import Usuario
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from flask import flash

# Creación de objeto Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Esta ruta recibe solicitudes de tipo GET y POST
    # Si la solicitud es de tipo GET, eso quiere decir que estamos accediendo a la ruta
    # de forma regular. Si la solicitud es de tipo POST, eso quiere decir que estamos
    # recibiendo información a través de un formulario
    if request.method == 'POST':
        # Si la solicitud es de tipo POST, simplemente quiere decir que recibimos información
        # desde un formulario y procedemos a utilizar dicha información
        email = request.form.get("email")
        password = request.form.get("password")
        usuario = Usuario.getEmail(email) # Acá tenemos un objeto con toda la info. de el usuario
        # Verificación de contraseña para login utilizando hash
        # usuario is None valida que el usuario exista en la BD
        # not bcrypt.check_password_hash(usuario.password, password) compara el hash de
        # la contraseña almacenada en la BD con el hash que se genera por la contraseña 
        # recién ingresada.
        if usuario is None or not bcrypt.check_password_hash(usuario.password, password):
            flash("Invalid Email/Password")
            return redirect('/')
        # Si no entramos al if anterior, quiere decir que el usuario existe correctamente en la BD
        # y por lo tanto, podemos crear una sesión para dicho usuario.
        session["id"] = usuario.id
        return redirect('/profile')
    else:
        # Si la solicitud no es de tipo POST, suponemos que es de tipo GET
        # y renderizamos la vista respectiva
        return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Empezamos haciendo validaciones sobre los datos
        # Primera validación es respecto de las contraseñas (son iguales?)
        if request.form['password'] == request.form['confirm_password']:
            # Si las contraseñas son iguales, capturamos el resto de los datos
            data = dict(request.form)
            # Generación de hash
            data['password'] = bcrypt.generate_password_hash(
                request.form['password'])
            if Usuario.validate_usuario(request.form):
                usuario = Usuario.save(data)
                session["id"] = usuario.id
                return redirect("/profile")
        else:
            flash("Password must be the same")
    return render_template('signup.html')


@app.route('/profile')
def profile():
    if session.get('id') == None:
        return redirect('/')
    else:
        usuario = Usuario.getId(session)
        return render_template("profile.html", usuario=usuario)


@app.route('/logout')
def logout():
    session.clear()

    return redirect('/login')
