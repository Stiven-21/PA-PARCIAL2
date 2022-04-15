from models.archives import select_archives

def ControllerShareArchive(url):
    return select_archives.GetArchiveShare(url)