from models.archives import select_archives

def ControllerArchiveIndex():
    archives = select_archives.GetArchivesForIndex()
    return archives