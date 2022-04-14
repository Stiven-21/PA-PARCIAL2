from flask import flash, session
import re

def ControllerValidateMail(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None

def ControllerArchiveEmpty(archivo):
    if archivo.filename == "":
        flash("Debe selecionar un archivo")
        return False   
    return True

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