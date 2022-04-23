from flask import flash
from models.archives import select_archives

def GetArchivesIndex(search):#RETORNA TODOS LOS ARCHIVOS PUBLICOS Y LOS DEL BUSCADOR
    archives = select_archives.GetArchivesForIndex(search)
    if archives is None:
        flash("No se encontraron archivos")
    return archives

def GetAllArchivesOfUser(id):#RETORMA TODOS LOA RCHIVOS DE UN USUARIO
    return select_archives.GetArchivesUser(id)

def GetCountArchivesOfUser(id):#RETORNA LA CANTIDAD DE ARCHIVOS DE ESE USUARIO
    return select_archives.GetTotalArchivesUser(id)
    
def ControllerCountUrlArchive(url):#RETORNA SI HAY ARCHIVOS CON ESA URL
    cant = select_archives.GetCountArchivesUrl(url)
    if cant['COUNT(*)'] == 1:
        return True
    return False

def ControllerFileIsOfUser(id_archivo, id_usuario):#RETORNA SI EL ARCHIVO PERTENESE AL USUARIO LOGEADO
    Delete_Archivo = select_archives.GetArchiveDelete(id_archivo, id_usuario)
    if Delete_Archivo['COUNT(*)'] == 0:
        return False
    return True

def ControllerArchiveEdit(id_archivo, id_usuario):#RETORNA LOS DATOS DEL ARCHIVO A EDITAR
    return select_archives.GetArchiveEditar(id_archivo, id_usuario)

def ControllerPreviewFile(url):#RETORNA LOS DATOS DEL ARCHIVO PARA LA VISTA
    return select_archives.GetArchiveShare(url)

def GetArchiveDownload(id):#RETORNA LOS DATOS DEL ARCHIVO A DESCARGAR
    return select_archives.GetArchiveDownload(id)