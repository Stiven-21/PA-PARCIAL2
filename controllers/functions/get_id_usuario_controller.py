from models.users import select_users
import hashlib

def GetIdUser(user, password):
    password_encrypt = hashlib.sha512(password.encode()).hexdigest()
    usuario = select_users.GetUserLogin(user=user, password=password_encrypt)
    for user in usuario:
        id = user['id_usuario']
    return id