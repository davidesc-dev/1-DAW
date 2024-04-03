// Debemos controlar que no se quede vacío el nuevo campo para el mail.
// Se comprobará si es un campo de mail adecuado, mirando si contiene una @
// en su interior, y además que no haya más de 1. (Nota: “Para hacer esto no se
// pueden usar funciones especiales de cadenas de JavaScript. Hay que hacerlo
// usando bucles y condicionales”).
// Comprobar también que la “@” no sea ni el primer carácter ni el último.
// Si se cumplen todos estos requisitos, se mostrará toda la información por
// pantalla mediante un alert() y además se enviará dicha información. En caso
// contario mostraremos los mensajes adecuados al usuario, bien por no haber
// introducido datos o porque no se cumplen las condiciones del mail.


// FUNCION
function Validar_Envio() {
    // Condicional para impedir que el campo quede vacío
    if (document.formulario.correo.value.length === 0) {
        document.getElementById('mensaje').innerHTML = '<p style="color: red;">El campo de correo no puede quedar vacío</p>';
        document.getElementById('mensaje').style.display = 'block';
        document.formulario.correo.focus();
        setTimeout(() => {
            document.location.href=document.location.href;
          }, 2000);

    }
    else{
        var control = 0
        var email = (document.formulario.correo.value)
        // Bucle for que recorre cada caracter del correo excluyendo el
        // primero y el ultimo para comprobar que hay una @ 
        for (var i = 1; i < email.length - 1; i++) {
            if (email[i] === "@") {
                // Variable booleana de control para saber si se encontró alguna @
                control += 1
            }
        }
        // Condicional si el correo es valido teniendo una sola @ ni al principio ni al final
        if (control === 1) {
            document.getElementById('mensaje').innerHTML = '<p style="color: green;">El correo es correcto</p>';
            document.getElementById('mensaje').style.display = 'block';
        }
        // Condicional si no hay ninguna @
        else if (control === 0) {
            document.getElementById('mensaje').innerHTML = '<p style="color: red;">El texto no tiene formato correcto</p>';
            document.getElementById('mensaje').style.display = 'block';
            document.formulario.correo.focus();
            setTimeout(() => {
                document.location.href=document.location.href;
            }, 2000);
        }
        // Condicional si hay mas de una @
        else if (control > 1) {
            document.getElementById('mensaje').innerHTML = '<p style="color: red;">El texto no puede contener mas de una @</p>';
            document.getElementById('mensaje').style.display = 'block';
            document.formulario.correo.focus();
            setTimeout(() => {
                document.location.href=document.location.href;
            }, 2000);
        }
    }
}
