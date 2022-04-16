from models.archives import select_archives
from models.archives import delete_archive
import os

def ControllerValidateArchiveDelete(id_archivo, id_usuario):
    Delete_Archivo = select_archives.GetArchiveDelete(id_archivo, id_usuario)
    if Delete_Archivo['COUNT(*)'] == 0:
        return False
    return True

def ControllerDeleteArchive(id_archivo, id_usuario, delete):
    os.remove(delete)
    delete_archive.DeleteArchiveUser(id_archivo, id_usuario)
    