from config.database import db

def UserValidate(validate, url_validate):
    cursor = db.cursor()
    cursor.execute('UPDATE usuarios SET validate = "true", url_val_mail = "" WHERE validate="'+validate+'" AND url_val_mail="'+url_validate+'"')
    cursor.close()
    
def SendUrlPassword(user, url_pass):
    cursor = db.cursor()
    cursor.execute('UPDATE usuarios SET url_pass = "'+url_pass+'" WHERE user="'+user+'" ')
    cursor.close()

def SendPasswordRecuperate(url, password):
    cursor = db.cursor()
    cursor.execute('UPDATE usuarios SET password = "'+password+'", url_pass="" WHERE url_pass="'+url+'" ')
    User = cursor.fetchone()
    
    cursor.close()
    return User

