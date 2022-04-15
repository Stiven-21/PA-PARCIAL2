from flask import flash
from controllers.validations import validations_controller
from controllers.archives import Count_Url_Archive_Controller
from models.archives import insert_archives
import random
import string

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
    return True

def ControllerSendArchive(name, id_usuario, archive, access):
    if access is None:
        access = 'off'
    
    ruta_archivo = validations_controller.ControllerSaveArchive(archive)
    ruta_vista = validations_controller.ControllerVistaArchive(ruta_archivo)
    tipo = validations_controller.ControllerExtractTypeArchive(archive)
    url_share =  (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(90)))
    
    while Count_Url_Archive_Controller.ControllerCountUrlArchive(url_share) == True:
        url_share =  (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(90)))
    
    insert_archives.CreateArchive(name, id_usuario, ruta_archivo, ruta_vista, tipo, access, url_share)