document.getElementById('user').addEventListener('input', function(evt) {
    campo = evt.target;
    text = document.getElementById('validate_email');
        
    emailRegex = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;
    if (emailRegex.test(campo.value)) {
      text.innerText = "E-mail válido";
      text.style.color = "Green"
    } else {;
      text.innerText = "E-mail invalido";
      text.style.color = "Red";
    }
});