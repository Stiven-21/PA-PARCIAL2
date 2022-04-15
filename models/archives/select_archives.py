from config.database import db

def GetArchivesUser(id_usuario):
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM archivos WHERE id_usuario ="'+id_usuario+'" ORDER BY id_archivo DESC')
    archives = cursor.fetchall()
    cursor.close()
    return archives

def GetTotalArchivesUser(id_usuario):
    cursor = db.cursor(dictionary = True)
    cursor.execute('SELECT COUNT(*) FROM archivos WHERE id_usuario = "'+id_usuario+'" ')
    total_archives = cursor.fetchone()
    cursor.close()
    return total_archives