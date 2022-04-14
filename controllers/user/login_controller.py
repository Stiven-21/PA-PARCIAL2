from flask import flash
from controllers.validations import validations_controller
from models.users import select_users
import hashlib

def ControllerLogin(user, password):
    try:
        password = password
    except:
        password = ""
    
    isValid = True
    
    if not validations_controller.ControllerValidateEmpty(user):
        isValid = False
        flash("Ingrese un Email")
    else:
        usuario = select_users.GetUserUser(user=user)
        if not usuario:
            isValid = False
            flash("El email no se encuentra registrado")
        else:
            if not validations_controller.ControllerValidateEmpty(password):
                isValid = False
                flash("Ingrese la contraseña")
            else:
                password_encrypt = hashlib.sha512(password.encode()).hexdigest()
                usuario = select_users.GetUserLogin(user=user, password=password_encrypt)
                if not usuario:
                    isValid = False
                    flash("Contraseña incorrecta")
                else:
                    for user in usuario:
                        if(user['validate'] != 'true'):
                            isValid = False
                            flash("Su cuenta esta registrada!")
                            flash("Pero aun no ha sido activada")
                        
    if isValid == False:
        return False

    return True