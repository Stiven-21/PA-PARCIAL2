from flask import flash
from controllers.functions import send_email_controller
from controllers.validations import validations_controller
from models.users import update_users
import hashlib


def FormPassword(password1, password2):
    try:
        password1 = password1
    except:
        password1 = ""
    try:
        password2 = password2
    except:
        password2 = ""
    isValid = True    
    
    if not validations_controller.ControllerValidateEmpty(password1):
        isValid = False
        flash("Es necesario que ingrese una contraseña")
    else:
        if not validations_controller.ControllerValidateEmpty(password2):
            isValid = False
            flash("Es necesario que repita la contraseña ingresada")
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
                        
    if isValid == False:
        return False
    
    return True

def SendEmailFormPassword(usuario, password, urluser):
    for email in usuario:
        user = email['user']
        
    password_encrypt = hashlib.sha512(password.encode()).hexdigest()
    update_users.SendPasswordRecuperate(url = urluser, password = password_encrypt)
    
    title = 'Recuperacion exitosa'
    body = '<h5>El proceso de recuperacion de cuenta se ha realizado con exito!</h5>'
    send_email_controller.SendEmail(user, title, body)
    