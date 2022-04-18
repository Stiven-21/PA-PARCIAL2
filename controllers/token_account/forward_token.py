from models.users import select_users
from models.users import update_users
from controllers.functions import send_email_controller
from config import settings
import hashlib
import random
import string

def GetIdUserRegisterController(user):
    user = select_users.GetUserUser(user)
    for us in user:
        id = us['id_usuario']
    return id

def GetUserNewToken(id):
    return select_users.GetUserForNewToken(id)

def NewTokenValidateAccountController(id, user, name, last_name):
    validate = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5)))
    url_validate = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(60)))
    
    update_users.SendNewValidateAccount(id, validate, url_validate)
    
    title = 'Reenvio de token - bienvenido '+name+' '+last_name
    body = '<center> <h5>'+name+' '+last_name+' su cuenta ha sido registrada con exito <br> Para ativar su cuenta porfavor ingrese<br> <a href="'+settings.URL_PAGE+'/validar-cuenta/'+url_validate+'/'+validate+'" style="text-decoration:none; color: blue;">Aquí</a></h5> </center>'
    
    send_email_controller.SendEmail(user, title, body)