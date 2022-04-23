from flask import  session
def ControllerEstaIniciado():
    return True if 'id_usuario' in session else False

def ControllerLoggedIn():
    if not ControllerEstaIniciado():
        return False
    return True 