window.onload = function(){
    var contenedor = document.getElementById('contenedor_carga');

    contenedor.style.visibility = 'hidden';
    contenedor.style.opacity = '0';
}

document.getElementById("funsubir").onclick = function(){
    var contenedor = document.getElementById('contenedor_carga');

    contenedor.style.visibility = 'visible';
    contenedor.style.opacity = '1';
}