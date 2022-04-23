from flask import flash, session
from controllers.validations import validations_controller
from controllers.consult_database import get_users_controller
import hashlib

def ControllerLogin(user, password):
    isValid = True
    try:
        password = password
    except:
        password = ''
    
    if not validations_controller.ControllerValidateEmpty(user):
        isValid = False
        flash("Ingrese la direccion email")
    else:
        if not get_users_controller.GetUserWithUser(user):
            isValid = False
            flash("La direccion email no esta registrada")
        else:
            if not validations_controller.ControllerValidateEmpty(password):
                isValid = False
                flash("Ingrese la contraseña")
            else:
                password_encrypt = hashlib.sha512(password.encode()).hexdigest()
                user_login = get_users_controller.GetUserForLogin(user, password_encrypt)
                if not user_login:
                    isValid = False
                    flash("Contraseña incorrecta")
                else:
                    if user_login['validate'] != 'true':
                        isValid = False
                        flash("Su cuenta esta registrada!")
                        flash("Pero aun no ha sido activada")
                    else:
                        session['id_usuario'] = user_login['id_usuario']
    return isValid
        