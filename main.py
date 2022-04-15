from flask import Flask, render_template, request, redirect, session, url_for
from config import settings
from models.users import select_users

from controllers.user import login_controller
from controllers.user import register_controller
from controllers.user import activate_account_controller
from controllers.user import recuperate_account_controller
from controllers.user import form_password_controller
from controllers.functions import get_id_usuario_controller
from controllers.archives import create_archive_controller
from controllers.archives import delete_archive_controller
from controllers.share import share_archive_controller
from controllers.validations import validations_controller
from controllers.profile import get_profile_user_controller
from controllers.profile import get_profile_archives_controller
from controllers.index import archives_index_controller

app = Flask(__name__)
app.secret_key = 'fjifjidfjied5df45df485h48@'

@app.get("/")
def index():
    logeado = True
    if not validations_controller.ControllerEstaIniciado():
        logeado = False
    archives = archives_index_controller.ControllerArchiveIndex()
    return render_template("index.html", logeado = logeado, archives = archives, link = settings.URL_PAGE)

@app.get("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))

#LOGIN
@app.get("/login")
def login():
    logeado = True
    if not validations_controller.ControllerEstaIniciado():
        logeado = False
    if logeado == True:
        return redirect(url_for('profile'))
        
    return render_template("users/login.html",logeado = logeado)
 
@app.post("/login")
def loginPost():
    logeado = True
    if not validations_controller.ControllerEstaIniciado():
        logeado = False
    if logeado == True:
        return redirect(url_for('profile'))
    
    user = request.form.get('user')
    password = request.form.get('password')
    
    if not login_controller.ControllerLogin(user, password):
        return render_template("users/login.html", user = user, logeado = logeado)
    
    id = get_id_usuario_controller.GetIdUser(user, password)
    session['id_usuario'] = id

    return redirect(url_for('index'))

#REGISTRER
@app.get("/register")
def register():
    logeado = True
    if not validations_controller.ControllerEstaIniciado():
        logeado = False
    if logeado == True:
        return redirect(url_for('profile'))
    return render_template("users/register.html",logeado = logeado)

@app.post("/register")
def registerPost():
    logeado = True
    if not validations_controller.ControllerEstaIniciado():
        logeado = False
    if logeado == True:
        return redirect(url_for('profile'))
    name = request.form.get('name')
    last_name = request.form.get('last_name')
    user = request.form.get('user')
    password = request.form.get('password')
    alerta = False
    
    if not register_controller.ControllerRegister(name, user, password):
        return render_template("users/register.html", name=name, user = user, last_name = last_name, logeado = logeado)
    
    register_controller.ControllerSendRegister(name, last_name, user, password)
    alerta = True
    return render_template("users/register.html", alerta = alerta, logeado = logeado)

#PERFIL DEL USUARIO
@app.get("/profile")
def profile():
    logeado = True
    if not validations_controller.ControllerEstaIniciado():
        return redirect(url_for('login'))
    user = get_profile_user_controller.GetProfileUserController(str(session.get('id_usuario')))
    archives = get_profile_archives_controller.GetProfileArchivesController(str(session.get('id_usuario')))
    total_archives = get_profile_archives_controller.GetCantidadArchivesProfileController(str(session.get('id_usuario')))
    return render_template("profile/perfil.html",logeado = logeado, user = user, archives = archives, total_archives = total_archives, link = settings.URL_PAGE)

#ACTIVATE ACCOUNT
@app.get("/validar-cuenta/<urluser>/<token>")
def validar_cuenta(urluser, token):
    usuario = select_users.GetUserValidate(validate = token, url_validate=urluser)
    if not usuario:
        return render_template("errores/url_not_exist.html")
    else:
        activate_account_controller.ActivateAccount(token, urluser)
        return render_template("validate/account_activate.html")

#RECUPERAR CUENTA
@app.get("/recuperar-cuenta")
def recuperar():
    logeado = True
    if not validations_controller.ControllerEstaIniciado():
        logeado = False
    return render_template("users/recuperate_account.html", logeado = logeado)

@app.post("/recuperar-cuenta")
def recuperarPost():
    logeado = True
    if not validations_controller.ControllerEstaIniciado():
        logeado = False
    user = request.form.get('user')
    alerta = False
    
    if not recuperate_account_controller.RecuperateAccount(user):
        return render_template("users/recuperate_account.html", user = user, logeado = logeado)
    
    recuperate_account_controller.SendEmailRecuperateAccount(user)
    alerta = True
    return render_template("users/recuperate_account.html", alerta = alerta, logeado = logeado)

@app.get("/recuperar-cuenta/<urluser>")
def recuperar_cuenta(urluser):
    if urluser != "":
        usuario = select_users.GetUrlPassword(url_pass = urluser)
        if not usuario:
            return render_template("errores/url_not_exist.html")
        else:
            return render_template("users/form_new_password.html", urluser = urluser)

@app.post("/recuperar-cuenta/<urluser>")
def recuperar_cuentaPost(urluser):
    if urluser != "":
        usuario = select_users.GetUrlPassword(url_pass = urluser)
        if not usuario:
            return render_template("errores/url_not_exist.html")
        else:
            password1 = request.form.get('password1')
            password2 = request.form.get('password2')

            if not form_password_controller.FormPassword(password1, password2):
                return render_template("users/form_new_password.html", urluser = urluser)
            
            form_password_controller.SendEmailFormPassword(usuario, password1, urluser)             
            return render_template("index.html")

#CREAR ARCHIVO
@app.get("/crear-archivo")
def CreateArchive():
    logeado = True
    if not validations_controller.ControllerEstaIniciado():
        return redirect(url_for('login'))
    return render_template("archives/crear_archivo.html", logeado = logeado)

@app.post("/crear-archivo")
def CreateArchivePost():
    logeado = True
    if not validations_controller.ControllerEstaIniciado():
        return redirect(url_for('login'))
    name_archive = request.form.get("name_archivo")
    archivo = request.files['file']
    access_archive = request.form.get("access")
    
    if not create_archive_controller.ControllerCreateArchive(name_archive, archivo, access_archive):
        return render_template("archives/crear_archivo.html", name_archivo = name_archive, logeado = logeado)
    
    create_archive_controller.ControllerSendArchive(name_archive, str(session.get('id_usuario')), archivo, access_archive)
    return redirect(url_for('profile'))

#EDITAR ARCHIVO
@app.get("/Archivo/editar/<id>")
def EditArchive(id):
    return "EDITAR ARCHIVO"

#ELIMINAR ARCHIVO
@app.get("/archivo/borrar-archivo/<id>")
def DeleteArchive(id):
    logeado = True
    if not validations_controller.ControllerEstaIniciado():
        return redirect(url_for('login'))
    id_usuario = str(session.get('id_usuario'))
    if not delete_archive_controller.ControllerValidateArchiveDelete(id, id_usuario):
        return render_template('errores/not_autorice_delete.html',logeado = logeado)
        
    delete_archive_controller.ControllerDeleteArchive(id, id_usuario)
    return redirect(url_for('profile'))
    
#COMPARTIR
@app.get("/archive/<url>")
def Share(url):
    logeado = True
    if not validations_controller.ControllerEstaIniciado():
        logeado = False
    share = share_archive_controller.ControllerShareArchive(url)
    if share is None:
        return render_template('errores/archive_not_exist.html',logeado = logeado)
    
    if share['id_usuario'] != session.get('id_usuario'): 
        if share['accesso'] == 'off':
            return render_template('errores/not_autorice_url.html',logeado = logeado)
    return render_template('archives/share.html',logeado = logeado, share = share)

app.run(debug=True)