from config.database import db

def CreateArchive():
    cursor = db.cursor()
    
    cursor.close()