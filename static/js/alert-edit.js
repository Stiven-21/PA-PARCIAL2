const edit_archive = document.querySelector(".btn-edit")

if(edit_archive){
    edit_archive.addEventListener('click', (e) => {
        if(!confirm('¿Esta seguro que desea guardar los cambios?')){
            e.preventDefault()
        }else{
            var contenedor = document.getElementById('contenedor_carga');
            
            contenedor.style.visibility = 'visible';
            contenedor.style.opacity = '1';
        }
    });
}