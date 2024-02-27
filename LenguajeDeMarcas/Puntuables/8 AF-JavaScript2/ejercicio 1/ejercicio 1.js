var numero = prompt("Indique un numero:")
var tabla = ""

for (i=0; i<11; i++){
    var numeromultiplicado = numero * i;
    tabla += numero + "x" + i + "=" + numeromultiplicado + "\n";
}

alert(tabla);