var var1 = Number(prompt("Introduzca un primer numero"));
var var2 = Number(prompt("Introduzca un segundo numero"));
var suma = var1+var2;
var resta = var1-var2;
var producto = var1*var2;
var division = var1/var2;
var resto = var1%var2;


document.write(var1 + "+" + var2 + "=" + suma + "<br>");
document.write(var1 + "-" + var2 + "=" + resta + "<br>");
document.write(var1 + "x" + var2 + "=" + producto + "<br>");
document.write(var1 + "/" + var2 + "=" + division + "<br>");
document.write(var1 + "%" + var2 + "=" + resto);