from flask import flash
from controllers.functions import send_email_controller
from models.users import select_users
from models.users import update_users
from config import settings
import string
import random


def RecuperateAccount(user):
    isValid = True

    if user == "":
        isValid = False
        flash("Ingrese un email")
    else:
        usuario = select_users.GetUserUser(user=user)
        if not usuario:
            isValid = False
            flash("Este email no se encuetra registrado")
            
    if isValid == False:
        return False
    
    return True

def SendEmailRecuperateAccount(user):
    url_pass = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(60)))
    
    update_users.SendUrlPassword(user=user, url_pass=url_pass)
    
    title = 'Recuperacion de cuenta'
    body = '<h5>Para recuperar su cuenta porfavor ingrese <a href="'+settings.URL_PAGE+'/recuperar-cuenta/'+url_pass+'" style="text-decoration:none; color: blue;">Aquí</a></h5>'

    send_email_controller.SendEmail(user, title, body)
    