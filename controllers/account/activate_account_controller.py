from models.users import update_users

def ActivateAccount(token, urluser):
    update_users.UserValidate(validate = token, url_validate=urluser)