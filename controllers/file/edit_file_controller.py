from controllers.validations import validations_controller
from models.archives import update_archives
from config import settings
from flask import flash
import os

def ControllerEditFile(name, archivo, id_file, access, edit):
    isValid = True
    if not validations_controller.ControllerValidateEmpty(name):
        isValid = False
        flash("No se permite el campo nombre vacio")
    else:
        ControllerSendEditFile(name, archivo, id_file, access, edit)
    return isValid

def ControllerSendEditFile(name, archivo, id_file, access, edit):
    if not validations_controller.ControllerValidateEmpty(archivo.filename):
        if access != edit['accesso']:
            update_archives.UpdateAccessArchive(access, id_file)
        ControllerEditNameFileEdit(name, id_file)
    else:
        ControllerEditAllFileEdit(name, archivo, access, id_file, edit)
        
def ControllerEditNameFileEdit(name_archive, id_archive):
    diret = '//\\.:;'
    for cam in diret:
        name_archive = name_archive.replace(cam, ' ')
    update_archives.UpdateNameArchive(name_archive, id_archive)
        
def ControllerEditAllFileEdit(name, archive, acceso, id_archivo, edit):
    os.remove(settings.ROUTE_IMAGE+edit['ruta_archivo'])
    ruta_archivo = validations_controller.ControllerSaveArchive(name, archive)
    ruta_vista = validations_controller.ControllerVistaArchive(ruta_archivo)
    tipo = validations_controller.ControllerExtractTypeArchive(archive)
    size = validations_controller.ControllerExtractPesoArchive(ruta_archivo)
    
    diret = '//\\.:;'
    for cam in diret:
        name = name.replace(cam, ' ')
        
    update_archives.UpdateAllArchive(name, ruta_archivo, ruta_vista, tipo, size, acceso, id_archivo)
    