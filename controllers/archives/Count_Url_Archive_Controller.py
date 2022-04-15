from models.archives import select_archives

def ControllerCountUrlArchive(url):
    cant = select_archives.GetCountArchivesUrl(url)
    if cant['COUNT(*)'] == 1:
        return True
    return False
