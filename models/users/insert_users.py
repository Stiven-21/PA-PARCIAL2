from config.database import db

def CreateUser(nombre, apellido, user, password, validate, url_validate):
    cursor = db.cursor()
    cursor.execute("insert into usuarios(nombre_usuario, apellido_usuario, user, password, validate, url_val_mail) values(%s,%s,%s,%s,%s,%s)", (
        nombre, 
        apellido, 
        user, 
        password,
        validate,
        url_validate
    ))
    cursor.close()