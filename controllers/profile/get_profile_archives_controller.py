from models.archives import select_archives

def GetProfileArchivesController(id_usuario):
    archives = select_archives.GetArchivesUser(id_usuario)
    return archives

def GetCantidadArchivesProfileController(id_usuario):
    total_archives = select_archives.GetTotalArchivesUser(id_usuario)
    return total_archives