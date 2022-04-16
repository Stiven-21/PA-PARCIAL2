from config.database import db

def UpdateNameArchive(name_archive, id_archive):
    cursor = db.cursor()
    cursor.execute('UPDATE archivos SET nombre_archivo = "'+name_archive+'" WHERE id_archivo = "'+id_archive+'" ')
    cursor.close()
    
def UpdateAllArchive(name_archive, ruta_archivo, ruta_vista, type, size, acces, id_archive):
    cursor = db.cursor()
    cursor.execute('UPDATE archivos SET nombre_archivo = "'+name_archive+'", ruta_archivo = "'+ruta_archivo+'", ruta_vista = "'+ruta_vista+'", type = "'+type+'", size = "'+size+'", accesso = "'+acces+'" WHERE id_archivo="'+id_archive+'" ')
    cursor.close()
    
def UpdateAccessArchive(acces, id_archive):
    cursor = db.cursor()
    cursor.execute('UPDATE archivos SET accesso = "'+acces+'" WHERE id_archivo="'+id_archive+'" ')
    cursor.close()