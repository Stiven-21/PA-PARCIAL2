from config.database import db

def CreateArchive(name, id_usuario, ruta_archivo, ruta_vista, type, size , access, url_share):
    cursor = db.cursor()
    cursor.execute("insert into archivos(id_usuario, nombre_archivo, ruta_archivo, ruta_vista, type, size, accesso, url_share) values(%s,%s,%s,%s,%s,%s,%s,%s)", (
        id_usuario,
        name,
        ruta_archivo,
        ruta_vista,
        type,
        size,
        access,
        url_share
    ))
    cursor.close()