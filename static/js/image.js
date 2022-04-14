document.getElementById('file').onchange = function(e){
    archivo = this.value
    type = archivo.split('.').pop()
    nombre_archivo = archivo.replace(/^.*[\\\/]/, '');

    document.getElementById('nombre').innerHTML = 'Nombre: '+nombre_archivo
    document.getElementById('tipo').innerHTML = 'Tipo: '+type

    switch(type)
    {
        case 'pdf':
        case 'PDF':
            document.getElementById('vista_previa').src = "/static/images/types/pdf.jpg"
            break;

        case 'docx':
        case 'doc':
        case 'docm':
        case 'dotx':
            document.getElementById('vista_previa').src = "/static/images/types/word.jpg"
            break;
        
        case 'xlsx':
        case 'xlsm':
        case 'xltx':
        case 'xltm':
        case 'xlsb':
        case 'xlam':
            document.getElementById('vista_previa').src = "/static/images/types/excel.jpg"
            break;

        case 'pptx':
        case 'pptm':
        case 'potx':
        case 'potm':
        case 'ppam':
        case 'ppsx':
        case 'ppsm':
        case 'sldx':
        case 'sldm':
        case 'thmx':
            document.getElementById('vista_previa').src = "/static/images/types/point.png"
            break;

        case 'jpg':
        case 'png':
        case 'tif':
        case 'bmp':
        case 'psd':
        case 'gif':
        case 'raw':
            reader = new FileReader();
            reader.readAsDataURL(e.target.files[0]);
            reader.onload = function(){
                document.getElementById('vista_previa').src = reader.result
            }
            break;

        case 'exe':
            document.getElementById('vista_previa').src = "/static/images/types/ejecutable.png"
            break;

        default:
            document.getElementById('vista_previa').src = "/static/images/types/not-preview.png"
            break;
    }
}