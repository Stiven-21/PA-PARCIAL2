from flask import flash
from controllers.consult_database import get_users_controller
from controllers.validations import validations_controller
from controllers.functions import send_mail_controller
from models.users import select_users
from models.users import insert_users
from config import settings
import random
import string
import hashlib

def ControllerRegister(name, last_name, user, password):
    isValid = True
    try:
        password = password
    except:
        password = ''
        
    if not validations_controller.ControllerValidateEmpty(name):
        isValid = False
        flash("Debe ingresar un nombre")
    else:
        if not validations_controller.ControllerValidateEmpty(user):
            isValid = False
            flash("Debe ingresar una direccion email")
        else:
            if validations_controller.ControllerValidateMail(user) == True:
                if not get_users_controller.GetUserWithUser(user=user):
                    if not validations_controller.ControllerValidateEmpty(password):
                        isValid = False
                        flash("Debe ingresar una contraseña")
                    else:
                        if not validations_controller.ControllerLengthField(password):
                            isValid = False
                        else:
                            if not validations_controller.ControllerValidateCaracteres(password):
                                isValid = False
                            else:
                                ControllerSendRegister(name, last_name, user, password)
                else:
                    isValid = False
                    flash("La direccion email ya se encuentra registrada")
            else:
                isValid = False
                flash("Se ha ingresado una direccion email no valida")
    return isValid

def ControllerSendRegister(name, last_name, user, password):
    validate = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5)))
    url_validate = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(60)))
    
    encrypt = hashlib.sha512(password.encode()).hexdigest()
    insert_users.CreateUser(nombre=name, apellido=last_name, user=user, password=encrypt, validate = validate, url_validate=url_validate)
    
    title = 'Bienvenido '+name+' '+last_name
    page = "<center><img src='"+settings.URL_PAGE+"/static/images/inicio.png' height='40px' width='40px'><br>"+name+" "+last_name+" Bienvenido a My App<br></center><br>"
    body = page+'<center> <h5>'+name+' '+last_name+' su cuenta ha sido registrada con exito <br> Para ativar su cuenta porfavor ingrese<br> <a href="'+settings.URL_PAGE+'/validar-cuenta/'+url_validate+'/'+validate+'" style="text-decoration:none; color: blue;">Aquí</a></h5> </center>'
    
    send_mail_controller.send_email(user, title, body)