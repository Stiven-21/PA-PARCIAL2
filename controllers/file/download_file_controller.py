from controllers.consult_database import get_archives_controllers

def ControllerDownload(logeado, id_user, file, id_file):
    if logeado == False:
        if file['accesso'] == 'off':
            return False
    else:
        if not get_archives_controllers.ControllerFileIsOfUser(id_file, id_user):
            if file['accesso'] == 'off':
                return False
    return True