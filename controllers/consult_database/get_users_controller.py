from models.users import select_users

def GetUserWithUser(user):#TRAE USUARIO CON EMAIL
    return select_users.GetUserUser(user = user)

def GetUserForLogin(user, password):#TRAE USUARIO CON EMAIL Y PASSWORD
    return select_users.GetUserLogin(user=user, password=password)

def GetIdUserRegisterController(user):#RETORNA SOLO EL ID DEL USUARIO
    user = select_users.GetUserUser(user=user)
    return user['id_usuario']

def GetUserNewToken(id):#RETORNA TODOS LOS DATOS DEL USUARIO AL QUE SE LE REENVIARAEL TOKEN
    return select_users.GetUserForNewToken(id)

def GetUserWithValidateAndUrl(token, urluser):#RETORNA USUARIO PARA ACTIVAR
    return select_users.GetUserValidate(validate = token, url_validate=urluser)

def GetUserWithUrlpassword(url):#RETORNA USUARIOS CON ESA URL
    return select_users.GetUrlPassword(url_pass = url)

def GetDateOfUserForProfile(id):#RETORNA LOS DATOS DEL PERFIL DEL USUARIO
    return select_users.GetProfileUser(id)
