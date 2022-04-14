from controllers.functions import funciones

def SendEmail(user, title, body):
    funciones.send_email(user = user, title = title, body = body)