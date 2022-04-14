from flask import flash
from controllers.functions import send_email_controller
from controllers.validations import validations_controller
from models.users import select_users
from models.users import insert_users
from config import settings
import random
import string
import hashlib

def ControllerRegister(name, user, password):
    try:
        password = password
    except:
        password = ""
    isValid = True
    
    if not validations_controller.ControllerValidateEmpty(name):
        isValid = False
        flash("debe ingresar un nombre")
    else:
        if not validations_controller.ControllerValidateEmpty(user):
            isValid = False
            flash("debe ingresar un Email")
        else:
            validar_email = validations_controller.ControllerValidateMail(user)
            if validar_email == True:
                usuario = select_users.GetUserUser(user=user)
                if not usuario:
                    if not validations_controller.ControllerValidateEmpty(password):
                        isValid = False
                        flash("Ingrese una contraseña")
                    else:
                        if not validations_controller.ControllerLengthField(password):
                            isValid = False
                        else:
                            if not validations_controller.ControllerValidateCaracteres(password):
                                isValid = False
                else:
                    isValid = False
                    flash("El Email ya se encuentra registrado")
            else:
                isValid = False
                flash("Se ha ingresado un correo no valido")

    if isValid == False:
        return False
    return True

def ControllerSendRegister(name, last_name, user, password):
    validate = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5)))
    url_validate = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(60)))
    
    encrypt = hashlib.sha512(password.encode()).hexdigest()
    insert_users.CreateUser(nombre=name, apellido=last_name, user=user, password=encrypt, validate = validate, url_validate=url_validate)
    
    title = 'Bienvenido '+name+' '+last_name
    body = '<center> <h5>'+name+' '+last_name+' su cuenta ha sido registrada con exito <br> Para ativar su cuenta porfavor ingrese<br> <a href="'+settings.URL_PAGE+'/validar-cuenta/'+url_validate+'/'+validate+'" style="text-decoration:none; color: blue;">Aquí</a></h5> </center>'
    
    send_email_controller.SendEmail(user, title, body)