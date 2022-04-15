from models.users import select_users

def GetProfileUserController(id):
    user = select_users.GetProfileUser(id)
    return user