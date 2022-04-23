from controllers.validations import validations_controller
from controllers.consult_database import get_archives_controllers
from models.archives import insert_archives
from flask import flash
import random
import string

def ControllerCreateArchive(name, id_usuario, archive, access):
    isValid = True
    if not validations_controller.ControllerValidateEmpty(name):
        isValid = False
        flash("Debe darle un nombre al archivo")
    else:
        if not validations_controller.ControllerValidateEmpty(archive.filename):
            isValid = False
            flash("Debe seleccionar un archivo")
        else:
            ControllerSendArchive(name, id_usuario, archive, access)
            
    return isValid

def ControllerSendArchive(name, id_usuario, archive, access):
    ruta_archivo = validations_controller.ControllerSaveArchive(name, archive)
    ruta_vista = validations_controller.ControllerVistaArchive(ruta_archivo)
    tipo = validations_controller.ControllerExtractTypeArchive(archive)
    url_share =  (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(90)))
    size = validations_controller.ControllerExtractPesoArchive(ruta_archivo)
    
    while get_archives_controllers.ControllerCountUrlArchive(url_share) == True:
        url_share =  (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(90)))
    
    diret = '//\\.:; '
    for cam in diret:
        name = name.replace(cam, ' ')
    
    insert_archives.CreateArchive(name, id_usuario, ruta_archivo, ruta_vista, tipo, size, access, url_share)