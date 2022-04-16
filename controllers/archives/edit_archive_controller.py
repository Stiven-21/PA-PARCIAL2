from models.archives import select_archives
from models.archives import update_archives
from controllers.validations import validations_controller
import os

def ControllerArchiveEdit(id_archivo, id_usuario):
    return select_archives.GetArchiveEditar(id_archivo, id_usuario)

def ControllerEditNameArchiveEdit(name_archive, id_archive):
    diret = '//\\.:;'
    for cam in diret:
        name_archive = name_archive.replace(cam, ' ')
    update_archives.UpdateNameArchive(name_archive, id_archive)
    
def ControllerEditAllArchiveEdit(name, delete_archive, archive, acceso, id_archivo):
    os.remove(delete_archive)
    ruta_archivo = validations_controller.ControllerSaveArchive(name, archive)
    ruta_vista = validations_controller.ControllerVistaArchive(ruta_archivo)
    tipo = validations_controller.ControllerExtractTypeArchive(archive)
    size = validations_controller.ControllerExtractPesoArchive(ruta_archivo)
    
    diret = '//\\.:;'
    for cam in diret:
        name = name.replace(cam, ' ')
        
    update_archives.UpdateAllArchive(name, ruta_archivo, ruta_vista, tipo, size, acceso, id_archivo)
    
def ControllerEditAccessArchiveEdit(acceso, id_archivo):
    update_archives.UpdateAccessArchive(acceso, id_archivo)