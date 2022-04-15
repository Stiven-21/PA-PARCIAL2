from ast import Delete
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

def GetArchivesForIndex():
    cursor = db.cursor(dictionary = True)
    cursor.execute('SELECT * FROM archivos WHERE accesso="on" ORDER BY id_archivo DESC')
    archives = cursor.fetchall()
    cursor.close()
    return archives

def GetCountArchivesUrl(url):
    cursor = db.cursor(dictionary = True)
    cursor.execute('SELECT COUNT(*) FROM archivos WHERE url_share = "'+url+'" ')
    cant_url = cursor.fetchone()
    cursor.close()
    return cant_url

def GetArchiveDelete(id_archivo, id_usuario):
    cursor = db.cursor(dictionary = True)
    cursor.execute('SELECT COUNT(*) FROM archivos WHERE id_archivo="'+id_archivo+'" AND id_usuario="'+id_usuario+'"  ')
    Delete = cursor.fetchone()
    cursor.close()
    return Delete

def GetArchiveShare(url):
    cursor = db.cursor(dictionary = True)
    cursor.execute('SELECT * FROM archivos WHERE url_share="'+url+'" ')
    share = cursor.fetchone()
    cursor.close()
    return share