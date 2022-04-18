from models.archives import select_archives

def ControllerArchiveIndex(search):
    archives = select_archives.GetArchivesForIndex(search)
    return archives