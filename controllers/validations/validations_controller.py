import os
from flask import flash, session
from datetime import datetime
from config import settings
import re

def ControllerValidateMail(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None

def ControllerArchiveEmpty(archivo):
    if archivo.filename == "":
        flash("Debe selecionar un archivo")
        return False   
    return True

def ControllerAccess(access):
    if access is None:
        return 'off'
    return 'on'
    
def ControllerValidateEmpty(campo):
    if campo == "":
        return False
    return True

def ControllerValidateCaracteres(password):
    SpecialSym =['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','=','?','@','[',']','^','_','`','{','|','}','~']
    isValid = True
    if not any(char.isdigit() for char in password):
        isValid = False
        flash("La contraseña debe contener almenos un numero")
    if not any(char.isupper() for char in password):
        isValid = False
        flash("La contraseña debe contener almenos una mayuscula")
    if not any(char in SpecialSym for char in password):
        isValid = False
        flash("La contraseña debe contener almenos un caracter especial")
    if isValid == False:
        return False
    return True

def ControllerFieldEquals(campo1, campo2):
    if campo1 != campo2:
        flash("La contraseña debe contener minimo 8 caracteres")
        return False
    return True

def ControllerLengthField(campo):
    if len(campo) < 8:
        flash("La contraseña debe contener minimo 8 caracteres")
        return False
    return True

def ControllerEstaIniciado():
    return True if 'id_usuario' in session else False

def ControllerExtractTypeArchive(archive):
    name_archive = archive.filename
    name_archive = name_archive.split(".")
    
    tipo = name_archive[-1]
    return tipo

def ControllerExtractPesoArchive(ruta):
    peso = convert_bytes(os.stat(settings.ROUTE_IMAGE+ruta).st_size)
    return peso

def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def ControllerSaveArchive(name,archive):
    now = datetime.now()
    name_archive = archive.filename
    name_archive = name_archive.split(".")
    
    diret = '//\\.:; '
    for cam in diret:
        name = name.replace(cam, '-')
    
    new_name = str(name)+'-'+str(now.date())+'-'+str(now.hour)+'-'+str(now.minute)+'-'+str(now.second)+'-'+str(now.microsecond)+'.'+str(name_archive[-1])
    archive.save(settings.ROUTE_IMAGE + archive.filename)
    os.rename(settings.ROUTE_IMAGE + archive.filename, settings.ROUTE_IMAGE + new_name)
    ruta_archivo =  new_name
    return ruta_archivo

def ControllerVistaArchive(ruta_save):
    ruta = ruta_save.split(".")
    type = ruta[-1].lower()
    ruta_vista = settings.ROUTE_IMAGE_DEFAULT+"no-image.jpg"

    if type in ['html','htm']:
        ruta_vista = settings.ROUTE_IMAGE_DEFAULT+"html.jpg"
    if type == 'css':
        ruta_vista = settings.ROUTE_IMAGE_DEFAULT+"css.png"
    if type == 'js':
        ruta_vista = settings.ROUTE_IMAGE_DEFAULT+"css.png"
    if type == 'pdf':
        ruta_vista = settings.ROUTE_IMAGE_DEFAULT+"pdf.jpg"
    if type  in ['docx','doc', 'docm', 'dotx']:
        ruta_vista = settings.ROUTE_IMAGE_DEFAULT+"word.jpg"
    if type  in ['xlsx', 'xlsm', 'xltx', 'xltm', 'xlsb', 'xlam']:
        ruta_vista = settings.ROUTE_IMAGE_DEFAULT+"excel.jpg"
    if type  in ['pptx', 'pptm', 'potx', 'potm', 'ppam', 'ppsx', 'ppsm', 'sldx', 'sldm', 'thmx']:
        ruta_vista = settings.ROUTE_IMAGE_DEFAULT+"point.png"
    if type  in ['jpg', 'png', 'tif', 'bmp', 'psd', 'raw']:
        ruta_vista = settings.ROUTE_IMAGE + ruta_save
    if type  in ['rar', 'zip']:
        ruta_vista = settings.ROUTE_IMAGE_DEFAULT+"rar.jpg"
    if type  in ['mp4', 'mov', 'wmv', 'avi', 'avchd', 'mkv', 'gif']:
        ruta_vista = settings.ROUTE_IMAGE_DEFAULT+"mp4.png"
    if type == 'exe':
        ruta_vista = settings.ROUTE_IMAGE_DEFAULT+"ejecutable.png"
    
    return ruta_vista