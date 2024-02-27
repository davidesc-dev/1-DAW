var tabla = ""
var tablas = ""

for (i=1; i<11; i++){
    var tabla = ""
    for (j=0; j<11; j++){
        var numeromultiplicado = i * j;
        tabla += i + "x" + j + "=" + numeromultiplicado + "\n";
    }
    tablas += tabla + "\n";
}


alert(tablas);