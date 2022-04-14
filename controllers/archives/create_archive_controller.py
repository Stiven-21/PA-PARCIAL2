from flask import flash

from controllers.validations import validations_controller

def ControllerCreateArchive(name, archive, access):
    isValid = True
    
    if access is None:
        access = 'off'

    if not validations_controller.ControllerValidateEmpty(name):
        isValid = False
        flash("Debe darle un nombre al archivo")
    else:
        if not validations_controller.ControllerArchiveEmpty(archive):
            isValid = False
            
    if isValid == False:
        return False
    return False

def ControllerSendArchive(name, archive, acceess):
    if access is None:
        access = 'off'
    
    print("HORA DE SUBIR EL ACRIVO")