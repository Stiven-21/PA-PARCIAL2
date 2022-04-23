from flask import Flask, render_template, request, redirect, session, url_for, flash, send_from_directory

from controllers.logged_in import logged_in_controller
from controllers.consult_database import get_archives_controllers
from controllers.consult_database import get_users_controller
from controllers.validations import validations_controller
from controllers.sign_in import sign_in_controller
from controllers.sign_up import sign_up_controller
from controllers.account import forward_token_controller
from controllers.account import activate_account_controller
from controllers.account import recover_account_controller
from controllers.account import form_password_controller
from controllers.file import create_file_controller
from controllers.file import edit_file_controller
from controllers.file import delete_file_controller
from controllers.file import preview_file_controller
from controllers.file import download_file_controller
from config import settings


app = Flask(__name__)
app.secret_key = 'fjifjidfjied5df45df485h48@'

#INDEX
@app.route("/", methods =['POST','GET'])
def index():
    logeado = logged_in_controller.ControllerLoggedIn()
    search = ""
    if request.method ==  'POST':
        search = request.form.get('search')
        if search == '':
            return redirect(url_for('index'))
        archives = get_archives_controllers.GetArchivesIndex(search)
        return render_template("index.html",logeado = logeado, archives = archives)
    else:
        archives = get_archives_controllers.GetArchivesIndex(search)
        return render_template("index.html",logeado = logeado, archives = archives)
    
#LOGIN -- SIGN IN
@app.route("/login", methods =['POST','GET'])
def login():
    logeado = logged_in_controller.ControllerLoggedIn()
    if logeado == True:
        return redirect(url_for('profile'))
    
    if request.method ==  'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        if not sign_in_controller.ControllerLogin(user, password):
            return render_template("sign_in/sign_in.html",logeado = logeado, user = user)
        return redirect(url_for('index'))
    else:
        return render_template("sign_in/sign_in.html",logeado = logeado)
    
#LOGOUT
@app.get("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))

#REGISTER -- SIGN UP
@app.route("/register", methods =['POST','GET'])
def register():
    logeado = logged_in_controller.ControllerLoggedIn()
    if logeado == True:
        return redirect(url_for('profile'))
    
    if request.method ==  'POST':
        name = request.form.get('name')
        last_name = request.form.get('last_name')
        user = request.form.get('user')
        password = request.form.get('password')
        if not sign_up_controller.ControllerRegister(name, last_name, user, password):
            return render_template("sign_up/sign_up.html",logeado = logeado, name = name, last_name = last_name, user = user)
        id_new_user = get_users_controller.GetIdUserRegisterController(user)
        return render_template("sign_up/sign_up.html", logeado = logeado, alerta = True, id_new_user = id_new_user)
    else:
        return render_template("sign_up/sign_up.html",logeado = logeado)        
        
#RESSEND OF TOKEN
@app.get("/register/<id>")
def newToken(id):
    logeado = logged_in_controller.ControllerLoggedIn()
    if logeado == True:
        return redirect(url_for('profile'))
    user = get_users_controller.GetUserNewToken(id)
    if user == None:
        return redirect(url_for('register'))
    if user['validate'] == 'true':
        return redirect(url_for('login'))
    forward_token_controller.NewTokenValidateAccountController(str(user['id_usuario']), str(user['user']), str(user['nombre_usuario']), str(user['apellido_usuario']))
    return render_template("sign_up/sign_up.html", logeado = logeado, alerta = True, id_new_user = str(user['id_usuario']))

#ACTIVATE ACCOUNT
@app.get("/validar-cuenta/<urluser>/<token>")
def validateAccount(urluser, token):
    if not get_users_controller.GetUserWithValidateAndUrl(token, urluser):
        return render_template("error/url_not_exist.html")
    else:
        activate_account_controller.ActivateAccount(token, urluser)
        return render_template("validations/account_activate.html")

#RECOVER OF ACCOUNT
@app.route("/recover-account", methods =['POST','GET'])
def recover():
    logeado = logged_in_controller.ControllerLoggedIn()
    if logeado == True:
        return redirect(url_for('profile'))
    
    if request.method ==  'POST':
        user = request.form.get('user')
        if not recover_account_controller.RecoverAccount(user):
            return render_template("recover_account/recover_account.html", logeado = logeado, user = user)
        return render_template("recover_account/recover_account.html", logeado = logeado, alerta = True)
    else:
        return render_template("recover_account/recover_account.html", logeado = logeado)

#PASSWORDS FORM
@app.route("/recover-account/<url>", methods =['POST','GET'])
def recoverAccount(url):
    if not get_users_controller.GetUserWithUrlpassword(url):
        return render_template("error/url_not_exist.html")
    
    if request.method ==  'POST':
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if not form_password_controller.FormPassword(password1, password2, url):
            return render_template("recover_account/form_new_password.html", urluser = url)
        return redirect(url_for('index'))
    else:
        return render_template("recover_account/form_new_password.html", urluser = url)

#PROFILE
@app.get("/profile")
def profile():
    logeado = logged_in_controller.ControllerLoggedIn()
    if logeado == False:
        return redirect(url_for('register'))
    user = get_users_controller.GetDateOfUserForProfile(str(session.get('id_usuario')))
    archives = get_archives_controllers.GetAllArchivesOfUser(str(session.get('id_usuario')))
    total_archives = get_archives_controllers.GetCountArchivesOfUser(str(session.get('id_usuario')))
    return render_template("profile/profile.html",logeado = logeado, user = user, archives = archives, total_archives = total_archives)
    
#CREATE FILE
@app.route("/create-file", methods =['POST','GET'])
def CreateFile():
    logeado = logged_in_controller.ControllerLoggedIn()
    if logeado == False:
        return redirect(url_for('login'))
    
    if request.method ==  'POST':
        name_archive = request.form.get("name_archivo")
        archivo = request.files['file']
        access = validations_controller.ControllerAccess(request.form.get("access"))
        if not create_file_controller.ControllerCreateArchive(name_archive, str(session.get('id_usuario')), archivo, access):
            return render_template("file/create_file.html", logeado = logeado, access = access, name_archivo = name_archive)
        return redirect(url_for('profile'))
    else:
        return render_template("file/create_file.html", logeado = logeado, access = 'off')

#EDIT FILE
@app.route("/file/edit-file/<id_file>", methods =['POST','GET'])
def editFile(id_file):
    logeado = logged_in_controller.ControllerLoggedIn()
    if logeado == True:
        if not get_archives_controllers.ControllerFileIsOfUser(id_file, str(session.get('id_usuario'))):
            return render_template('error/not_autorice_file.html',logeado = logeado)
        else:
            edit = get_archives_controllers.ControllerArchiveEdit(id_file, str(session.get('id_usuario')))
            name_archivo = edit['nombre_archivo']#NOMBRE ARCHIVO 
            ruta = edit['ruta_vista']
            ruta = ruta.split(".")
            img = ruta[1]+"."+ruta[2]#IMAGEN
            name_select = edit['ruta_archivo']#NOMBRE ARCHIVO EN EL SERVIDOR
            tipo = edit['type']#TIPO ARCHIVO
            access = edit['accesso']#ACCESO   
    else:
        return redirect(url_for('login'))
    
    if request.method ==  'POST':
        name_archivo = request.form.get("name_archivo")
        archivo = request.files['file']
        access_archive = validations_controller.ControllerAccess(request.form.get("access"))
        edit = get_archives_controllers.ControllerArchiveEdit(id_file, str(session.get('id_usuario')))
        if validations_controller.ControllerValidateEmpty(archivo.filename) == True:
            flash('Si presiona a guardar sin seleccionar un archivo, se conservara el archivo anterior a la editacion')
            img = "/static/images/types/no-image.jpg"
            name_select = 'no definido'
            tipo = 'no definido'
            
        if not edit_file_controller.ControllerEditFile(name_archivo, archivo, id_file, access_archive, edit):
            return render_template("file/edit_file.html", logeado = logeado, name_archivo = name_archivo, img = img, name_select = name_select, tipo = tipo, access = access_archive)
        session.pop('_flashes', None)
        return redirect(url_for('profile'))
    else:
        return render_template("file/edit_file.html",  logeado = logeado, name_archivo = name_archivo, img = img, name_select = name_select, tipo = tipo, access = access)

#DELETE FILE
@app.get("/file/delete-file/<id_file>")
def deleteFile(id_file):
    logeado = logged_in_controller.ControllerLoggedIn()
    if logeado == False:
        return redirect(url_for('login'))
    if not delete_file_controller.ControllerDeleteFile(str(session.get('id_usuario')), id_file):
        return render_template('error/not_autorice_file.html',logeado = logeado)
    return redirect(url_for('login'))
    
#PREVIEW FILE
@app.get("/file/preview/<url>")
def PreviewFile(url):
    logeado = logged_in_controller.ControllerLoggedIn()
    preview = get_archives_controllers.ControllerPreviewFile(url)
    if preview is None:
        return render_template('error/file_not_exist.html',logeado = logeado)
    if not preview_file_controller.ControllerPreviewFile(preview, str(session.get('id_usuario'))):
        return render_template('error/not_autorice_url.html',logeado = logeado)
    ruta = preview['ruta_vista']
    ruta = ruta.split(".")
    img = ruta[1]+"."+ruta[2]#IMAGEN
    return render_template('file/preview_file.html',logeado = logeado, img = img, share = preview, link = settings.URL_PAGE)

#DOWNLOAD FILE
@app.get("/file/download/<id_file>")
def download(id_file):
    logeado = logged_in_controller.ControllerLoggedIn()
    file = get_archives_controllers.GetArchiveDownload(id_file)
    if not download_file_controller.ControllerDownload(logeado, str(session.get('id_usuario')), file, id_file):
        return render_template('error/not_autorice_file.html',logeado = logeado)
    return send_from_directory(settings.ROUTE_IMAGE, path=file['ruta_archivo'], as_attachment = True)

#app.run(debug=True)

