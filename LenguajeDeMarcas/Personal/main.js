const boton = document.getElementById("botonfondo")
const caja = document.getElementById("formbox")
var oscuro = false

boton.addEventListener("click",function(){
    if(oscuro){
        boton.textContent = "Modo claro"
        document.body.style.backgroundImage = "url(./assets/FondoOscuro.jpg)"
        oscuro = false
    }

    else{
        oscuro = true
        boton.textContent = "Modo oscuro"
        caja.style.boxShadow = "0 10px 100px -20px rgb(19 17 17)"
        document.body.style.backgroundImage = "url(./assets/FondoClaro.jpg)"
    }
})


