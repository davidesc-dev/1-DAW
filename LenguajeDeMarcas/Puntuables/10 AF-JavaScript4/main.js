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


// FUNCION PARA VALIDAR LOS ENVIOS
function Validar_Envio() {
    // Condicional para impedir que el campo quede vacío
    if (document.formulario.correo.value.length === 0) {
        document.getElementById('mensaje').innerHTML = '<p style="color: red;">El campo de correo no puede quedar vacío</p>';  // Busca el elemento del docuemento al que esta vinculado y cambia el html
        document.getElementById('mensaje').style.display = 'block';  // Busca el elemento llamado mensaje y cambia el estilo de none a block para que se vea
        document.formulario.correo.focus();  // Hace que el campo de correo resplandezca 
        setTimeout(() => {  // Función para añadir retraso a lo que se encuentre dentro
            document.location.href=document.location.href; // Recarga la página
          }, 2000); // El tiempo en milisegundos de retraso, en este caso, 2 segundos

    }

    // Cuando el campo NO está vacío
    else{
        var control = 0 // Variable de control booleana que será utilizada para saber cuantas @ hay
        var email = (document.formulario.correo.value) // Variable que guarda el valor del campo de correo

        for (var i = 1; i < email.length - 1; i++) { // Bucle for que recorre cada caracter del correo excluyendo el primero y el ultimo para comprobar que hay una @ 
            if (email[i] === "@") { // Condicional que se ejecuta si alguna letra del email siendo tratado como string es una "@"
                control += 1 // Si se cumple la condición se suma 1
            }
        }
        
        if (control === 1) { // Condicional si el correo es valido teniendo una sola @ que no esté ni al principio ni al final
            alert("El correo " + document.formulario.correo.value + " es correcto, será enviado en 3 segundos") // Envia una alerta
            document.getElementById('mensaje').innerHTML = '<p style="color: green;">El correo es correcto</p>'; // Cambia el html del elemento con el ID mensaje
            document.getElementById('mensaje').style.display = 'block'; //Cambia el estilo de none a block para que se vea
            document.getElementById('timer').style.display = 'block'; //Cambia el estilo de none a block para que se vea
            document.getElementById('timer').innerHTML = '<p style="color: red;">Se enviará en 3</p>'; // Cambia el html del elemento con el ID timer, este sera un temporizador cambiando el html hasta que se envie el formulario
            setTimeout(() => { // Función para añadir retraso a lo que se encuentre dentro
                document.getElementById('timer').innerHTML = '<p style="color: red;">Se enviará en 2</p>'; // Cambia el html del elemento con el ID timer
            }, 1000); // 1 segundo de cooldown
            setTimeout(() => { // Función para añadir retraso a lo que se encuentre dentro
                document.getElementById('timer').innerHTML = '<p style="color: red;">Se enviará en 1</p>'; // Cambia el html del elemento con el ID timer
            }, 2000); // 2 segundos de cooldown
            setTimeout(() => { // Función para añadir retraso a lo que se encuentre dentro
                document.getElementById("formulario1").submit() // Función que envia el formulario con el ID formulario1
            }, 3000); // 3 segundos de cooldown
        }
        
        else if (control === 0) { // Condicional si no hay ninguna @
            document.getElementById('mensaje').innerHTML = '<p style="color: red;">El texto no tiene formato correcto</p>'; // Cambia el html del elemento con el ID mensaje
            document.getElementById('mensaje').style.display = 'block'; //Cambia el estilo de none a block para que se vea
            document.formulario.correo.focus(); // Hace que el campo de correo resplandezca
            setTimeout(() => { // Función para añadir retraso a lo que se encuentre dentro
                document.location.href=document.location.href; // Recarga la página
            }, 2000); // 2 segundos de cooldown
        }
        // Condicional si hay mas de una @
        else if (control > 1) { 
            document.getElementById('mensaje').innerHTML = '<p style="color: red;">El texto no puede contener mas de una @</p>'; // Cambia el html del elemento con el ID mensaje
            document.getElementById('mensaje').style.display = 'block'; //Cambia el estilo de none a block para que se vea
            document.formulario.correo.focus(); // Hace que el campo de correo resplandezca
            setTimeout(() => { // Función para añadir retraso a lo que se encuentre dentro
                document.location.href=document.location.href; // Recarga la página
            }, 2000); // 2 segundos de cooldown
        }
    }
}