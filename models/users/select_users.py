from config.database import db

def GetUserLogin(user, password):
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuarios WHERE user="'+user+'" AND PASSWORD="'+password+'"')
    usuario = cursor.fetchall()
    cursor.close()
    return usuario

def GetUserUser(user):
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuarios WHERE user="'+user+'"')

    usuario = cursor.fetchall()
    cursor.close()
    return usuario

def GetUserValidate(validate, url_validate):
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuarios WHERE validate="'+validate+'" AND url_val_mail="'+url_validate+'"')

    usuario = cursor.fetchall()
    cursor.close()
    return usuario

def GetUrlPassword(url_pass):
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuarios WHERE url_pass ="'+url_pass+'" ')

    usuario = cursor.fetchall()
    cursor.close()
    return usuario

def GetProfileUser(id):
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuarios WHERE id_usuario ="'+id+'" ')
    usuario = cursor.fetchone()
    cursor.close()
    return usuario
    