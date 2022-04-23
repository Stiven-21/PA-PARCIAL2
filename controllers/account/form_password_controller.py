from flask import flash
from controllers.consult_database import get_users_controller
from controllers.validations import validations_controller
from controllers.functions import send_mail_controller
from models.users import update_users
from config import settings
import hashlib

def FormPassword(password1, password2, url):
    isValid = True
    try:
        password1 = password1
    except:
        password1 = ""
    try:
        password2 = password2
    except:
        password2 = ""
    if not validations_controller.ControllerValidateEmpty(password1):
        isValid = False
        flash("Es necesario ingresar una nueva contraseña")
    else:
        if not validations_controller.ControllerValidateEmpty(password2):
            isValid  = False
            flash("Es necesario repetir la contraseña ingresada")
        else:
            if not validations_controller.ControllerFieldEquals(password1, password2):
                isValid = False
                flash("Las contraseñas deben ser iguales")
            else:
                if not validations_controller.ControllerLengthField(password1):
                    isValid = False
                else:
                    if not validations_controller.ControllerValidateCaracteres(password1):
                        isValid = False
                    else:
                        SendEmailFormPassword(password1, url)
    return isValid
        
def SendEmailFormPassword(password, url):
    password_encrypt = hashlib.sha512(password.encode()).hexdigest()
    user_account = get_users_controller.GetUserWithUrlpassword(url)
    
    title = 'Recuperacion exitosa'
    page = "<center><img src='"+settings.URL_PAGE+"/static/images/inicio.png' height='40px' width='40px'><br>My App<br></center><br>"
    body = page+'<h5>Usuario(a) '+str(user_account["nombre_usuario"])+' '+str(user_account["apellido_usuario"])+' El proceso de recuperacion de cuenta se ha realizado con exito!</h5>'
    send_mail_controller.send_email(str(user_account["user"]), title, body)
    update_users.SendPasswordRecuperate(url = url, password = password_encrypt)
    