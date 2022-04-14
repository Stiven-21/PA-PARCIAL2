document.getElementById('password').addEventListener('input', function(evt) {
    const campo = evt.target,
          cantidad = document.getElementById('cantidad'),
          caracteres = document.getElementById("caracteres"),
          regex = /^(?=.*\d)(?=.*[a-záéíóúüñ]).*[A-ZÁÉÍÓÚÜÑ]/;

    let cant = campo.value
    if(cant.length < 8){
      cantidad.style.color = "Red";
    }else{
      cantidad.style.color = "Green";
    }

    if (regex.test(campo.value)) {
      caracteres.style.color = "Green";
    } else {
      caracteres.style.color = "Red";
    }
});