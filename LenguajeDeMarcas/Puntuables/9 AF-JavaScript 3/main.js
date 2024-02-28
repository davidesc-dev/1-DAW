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

var cadena1 = prompt("Introduzca una primera cadena:")
var cadena2 = prompt("Introduzca una segunda cadena:")

function concatenar() {
    alert("Concatenar\n"  + cadena1 + cadena2)
}

function alreves() {
    alert("Alreves\n" + cadena2 + cadena1)
}

function InsertarNumeros() {
    for (let a = 0; a < cadena1.length; contador++) {
     
      
    }
    alert("Alreves" + "<br>" + cadena2 + cadena1)
}

concatenar()

alreves()