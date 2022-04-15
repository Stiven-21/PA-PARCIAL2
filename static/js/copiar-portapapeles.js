document.getElementById("portapapeles").onclick = function(){
    var aux = document.createElement("input");
    aux.setAttribute("value", document.getElementById('text-copy').innerHTML);
    document.body.appendChild(aux);
    aux.select();
    document.execCommand("copy");
    document.body.removeChild(aux);
}