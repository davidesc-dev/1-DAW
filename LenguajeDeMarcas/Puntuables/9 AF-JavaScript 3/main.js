// Crear una aplicación en JavaScript donde se deben crear 3 funciones:
//  Función concatenar: A dicha función se le deben pasar por parámetros 2
// cadenas y debe devolver la concatenación de las mismas.
//  Función Alreves: A dicha función se le pasará una cadena por parámetros y
// devolverá dicha cadena al revés.
//  Función InsertarNumeros: Dicha función recibe como parámetro una cadena y
// devolverá dicha cadena con números insertados entre una letra y otra. Los
// números comenzarán en 1. Por ejemplo: Si la cadena recibida es: Cuarzo , el
// resultado debe ser una cadena de este tipo: C1u2a3r4z5o6
// Para hacer el ejercicio, se debe pedir al usuario las dos cadenas y hacer las llamadas
// oportunas a las 3 funciones anteriores, mostrando el resultado de las mismas.
// El programa debe funcionar bien aunque el usuario no introduzca nada.


// FUNCIONES
function concatenar(cadena1,cadena2) {
    if (cadena1.length === 0 || cadena2.length === 0) {
        alert("Alguna de las cadenas está vacía")
    }
    else{
        alert("Concatenar\n" + cadena1 + cadena2)
    }
}

function alreves(cadena) {
    if (cadena.length >= 0) {
        alert("Alreves\n" + cadena.split('').reverse().join(''))
    }
    else {
        alert("La cadena se encuenrtra vacía")
    }
}

function InsertarNumeros(cadena) {
    // if (cadena.length >= 1) {
        for (var i = 0; i < cadena.length; i++) {
            cadenaFinal += cadena[i] + (i + 1);
        }
        alert("Cadena con numeros\n" + cadenaFinal);
    // } else {
    //     alert("La cadena está vacía")
    // }
    
}


// PROGRAMA PRINCIPAL
    // FUNCION 1
var variable1 = prompt("Introduzca una primera cadena para concatenar:");
var variable2 = prompt("Introduzca una segunda cadena para concatenar:");
concatenar(variable1,variable2);

    // FUNCION 2
var variable = prompt("Introduzca una cadena para poner al reves:");
alreves(variable);

    // FUNCION 3
var variable = prompt("Introduzca una cadena para insertar numeros entre los caracteres:");
InsertarNumeros(variable);