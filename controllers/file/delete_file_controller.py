from controllers.consult_database import get_archives_controllers
from models.archives import delete_archive
from config import settings
import os
def ControllerDeleteFile(id_user, id_file):
    isValid = True
    if not get_archives_controllers.ControllerFileIsOfUser(id_file, id_user):
        isValid = False
    else:
        ControllerSendDeleteFile(id_file, id_user)
    return isValid
    
def ControllerSendDeleteFile(id_file, id_user):
    delete = get_archives_controllers.ControllerArchiveEdit(id_file, id_user)
    os.remove(settings.ROUTE_IMAGE+delete['ruta_archivo'])
    delete_archive.DeleteArchiveUser(id_file, id_user)