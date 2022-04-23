from flask import flash
from controllers.consult_database import get_users_controller
from controllers.validations import validations_controller
from controllers.functions import send_mail_controller
from models.users import update_users
from config import settings
import string
import random

def RecoverAccount(user):
    isValid = True
    if not validations_controller.ControllerValidateEmpty(user):
        isValid = False
        flash("De ingresar su email")
    else:
        if not get_users_controller.GetUserWithUser(user):
            isValid = False
            flash("La direccion email no esta registrada")
        else:
            SendEmailRecuperateAccount(user)
    return isValid

def SendEmailRecuperateAccount(user):
    url_pass = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(60)))
    update_users.SendUrlPassword(user=user, url_pass=url_pass)
    user_account = get_users_controller.GetUserWithUser(user)
    
    title = 'Recuperacion de cuenta'
    page = "<center><img src='"+settings.URL_PAGE+"/static/images/inicio.png' height='40px' width='40px'><br>"+str(user_account['nombre_usuario'])+" "+str(user_account['apellido_usuario'])+" Bienvenido a My App<br></center><br>"
    body = page+'<center><h5>Estimado(a) usurio(a) para que se posible realizar la <br> recuperacion de su cuenta, porfavor ingrese <a href="'+settings.URL_PAGE+'/recover-account/'+url_pass+'" style="text-decoration:none; color: blue;">Aquí</a></h5><center>'

    send_mail_controller.send_email(user, title, body)