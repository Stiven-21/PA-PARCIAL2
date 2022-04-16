const delete_archive = document.querySelectorAll(".btn-delete")

if(delete_archive){
    const btnArray = Array.from(delete_archive)
    btnArray.forEach((btn) =>{
        btn.addEventListener('click', (e) => {
            if(!confirm('¿Esta seguro que desea eliminar el archivo?')){
                e.preventDefault()
            }
        });
    })
}