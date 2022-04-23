
def ControllerPreviewFile(preview, id_user):
    if id_user is None:
        if preview['accesso'] == 'off':
            return False
    else:
        if str(preview['id_usuario']) != id_user:
            print(str(preview['id_usuario'])+" -- "+id_user)
            if preview['accesso'] == 'off':
                return False
    return True