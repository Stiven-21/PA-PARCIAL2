from config.database import db

def DeleteArchiveUser(id_archivo, id_usuario):
    cursor = db.cursor()
    cursor.execute('DELETE FROM archivos WHERE id_archivo="'+id_archivo+'" AND id_usuario="'+id_usuario+'"  ')
    cursor.close()