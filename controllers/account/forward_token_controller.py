from controllers.functions import send_mail_controller
from models.users import update_users
from config import settings
import random
import string

def NewTokenValidateAccountController(id, user, name, last_name):
    validate = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5)))
    url_validate = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(60)))
    
    update_users.SendNewValidateAccount(id, validate, url_validate)
    
    title = 'Reenvio de token - bienvenido '+name+' '+last_name
    page = "<center><img src='"+settings.URL_PAGE+"/static/images/inicio.png' height='40px' width='40px'><br>"+name+" "+last_name+" Bienvenido a My App<br></center><br>"
    body = page+'<center> <h5>'+name+' '+last_name+' su cuenta ha sido registrada con exito <br> Para ativar su cuenta porfavor ingrese<br> <a href="'+settings.URL_PAGE+'/validar-cuenta/'+url_validate+'/'+validate+'" style="text-decoration:none; color: blue;">Aquí</a></h5> </center>'
    
    send_mail_controller.send_email(user, title, body)


