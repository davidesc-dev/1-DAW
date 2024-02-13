'''Descripción del programa: Este programa ejecuta un juego


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
eleccion = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
eleccion = input("Te encuentras en tu casa y estas muy aburrido, quedarse/salir: ")
if eleccion == "quedarse":
    eleccion = input("Tu madre se enfada contigo porque te pasas todo el dia en casa jugando, te quita el movil y no te queda otra que salir fuera, ir a biblioteca/tienda: ")
    if eleccion == "biblioteca":
        eleccion = input("Estas un rato estudiando y te quedas hasta que cierran, tienes que decidir como irte, andar/bus: ")
        if eleccion == "andar":
            eleccion = input("Vas andando pero ves que unos maleantes se acercan en tu direccion, te acaban parando, te sacan una navaja y te dicen que les des todo lo que tienes, que haces, llamar policia/huir: ")
            if eleccion == "llamar policia":
                eleccion = input("Te recuerdo que no tienes movil porque te lo quitó tu madre, por lo que no te queda mas que correr por tu vida \nEchas a correr pero te tropiezas, estas arrinconado, que haces, rendirse/pelear: ")
                if eleccion == "rendirse":
                    print("Te dejan irte pero no sin antes quitarte hasta los zapatos, vuelves vivo a casa de suerte y encima tu madre te regaña por imprudente \n **HAS SOBREVIVIDO**")
                else:
                    print("¿En serio? Que vas a hacer contra un arma blanca. Ya te puedes imaginar lo que pasa (nada bonito) \n **HAS PERDIDO**")
            else:
                eleccion = input("Echas a correr pero te tropiezas, estas arrinconado, que haces, rendirse/pelear: ")
                if eleccion == "rendirse":
                    print("Te dejan irte pero no sin antes quitarte hasta los zapatos, vuelves vivo a casa de suerte y encima tu madre te regaña por imprudente \n **HAS SOBREVIVIDO**")
                else:
                    print("¿En serio? Que vas a hacer contra un arma blanca. Ya te puedes imaginar lo que pasa (nada bonito) \n **HAS PERDIDO**")
        else:
            print("Coges el bus y vuelves a casa sin mayor problema \n **FELICIDADES HAS GANADO**")
    else:
        eleccion = input("Vas a la tienda, cuanto decides gastarte, poco/mucho: ")
        if eleccion == "mucho":
            eleccion = input("Compraste bastantes cosas de la tienda gastandote asi todo el dinero que llevabas. \nAhora se hace de noche y tienes que volver, como vuelves, andar/bus: ")
            if eleccion == "andar":
                eleccion = input("Vas andando pero ves que unos maleantes se acercan en tu direccion, te acaban parando, te sacan una navaja y te dicen que les des todo lo que tienes, que haces, llamar policia/huir: ")
                if eleccion == "llamar policia":
                    eleccion = input("Te recuerdo que no tienes movil porque te lo quitó tu madre, por lo que no te queda mas que correr por tu vida \nEchas a correr pero te tropiezas, estas arrinconado, que haces, rendirse/pelear: ")
                    if eleccion == "rendirse":
                        print("Te dejan irte pero no sin antes quitarte hasta los zapatos, vuelves vivo a casa de suerte y encima tu madre te regaña por imprudente \n **HAS SOBREVIVIDO**")
                    else:
                        print("¿En serio? Que vas a hacer contra un arma blanca. Ya te puedes imaginar lo que pasa (nada bonito) \n **HAS PERDIDO**")
                else:
                    eleccion = input("Echas a correr pero te tropiezas, estas arrinconado, que haces, rendirse/pelear: ")
                    if eleccion == "rendirse":
                        print("Te dejan irte pero no sin antes quitarte hasta los zapatos, vuelves vivo a casa de suerte y encima tu madre te regaña por imprudente \n **HAS SOBREVIVIDO**")
                    else:
                        print("¿En serio? Que vas a hacer contra un arma blanca. Ya te puedes imaginar lo que pasa (nada bonito) \n **HAS PERDIDO**")
            else:
                eleccion = input("Compraste tanto que no tienes dinero para el bus, por lo que no te queda otra que andar \nVas andando pero ves que unos maleantes se acercan en tu direccion, te acaban parando, te sacan una navaja y te dicen que les des todo lo que tienes, que haces, llamar policia/huir: ")
                if eleccion == "llamar policia":
                    eleccion = input("Te recuerdo que no tienes movil porque te lo quitó tu madre, por lo que no te queda mas que correr por tu vida \nEchas a correr pero te tropiezas, estas arrinconado, que haces, rendirse/pelear: ")
                    if eleccion == "rendirse":
                        print("Te dejan irte pero no sin antes quitarte hasta los zapatos, vuelves vivo a casa de suerte y encima tu madre te regaña por imprudente \n **HAS SOBREVIVIDO**")
                    else:
                        print("¿En serio? Que vas a hacer contra un arma blanca. Ya te puedes imaginar lo que pasa (nada bonito) \n **HAS PERDIDO**")
                else:
                    eleccion = input("Echas a correr pero te tropiezas, estas arrinconado, que haces, rendirse/pelear: ")
                    if eleccion == "rendirse":
                        print("Te dejan irte pero no sin antes quitarte hasta los zapatos, vuelves vivo a casa de suerte y encima tu madre te regaña por imprudente \n **HAS SOBREVIVIDO**")
                    else:
                         print("¿En serio? Que vas a hacer contra un arma blanca. Ya te puedes imaginar lo que pasa (nada bonito) \n **HAS PERDIDO**")
        else:
            eleccion = input("Compraste un par de cosas, pero aun te sobra dinero \nAhora se hace de noche y tienes que volver, como vuelves, andar/bus: ")
            if eleccion == "andar":
                eleccion = input("Vas andando pero ves que unos maleantes se acercan en tu direccion, te acaban parando, te sacan una navaja y te dicen que les des todo lo que tienes, que haces, llamar policia/huir: ")
                if eleccion == "llamar policia":
                    eleccion = input("Te recuerdo que no tienes movil porque te lo quitó tu madre, por lo que no te queda mas que correr por tu vida \nEchas a correr pero te tropiezas, estas arrinconado, que haces, rendirse/pelear: ")
                    if eleccion == "rendirse":
                        print("Te dejan irte pero no sin antes quitarte hasta los zapatos, vuelves vivo a casa de suerte y encima tu madre te regaña por imprudente \n **HAS SOBREVIVIDO**")
                    else:
                        print("¿En serio? Que vas a hacer contra un arma blanca. Ya te puedes imaginar lo que pasa (nada bonito) \n **HAS PERDIDO**")
                else:
                    eleccion = input("Echas a correr pero te tropiezas, estas arrinconado, que haces, rendirse/pelear: ")
                    if eleccion == "rendirse":
                        print("Te dejan irte pero no sin antes quitarte hasta los zapatos, vuelves vivo a casa de suerte y encima tu madre te regaña por imprudente \n **HAS SOBREVIVIDO**")
                    else:
                        print("¿En serio? Que vas a hacer contra un arma blanca. Ya te puedes imaginar lo que pasa (nada bonito) \n **HAS PERDIDO**")
            else:
                print("Al tener dinero de sobra, puedes pagar el bus. Subes y vuelves a casa sin mayor problema \n **FELICIDADES HAS GANADO**")     
else:
    eleccion = input("Sales y piensas a donde dirigirte, biblioteca/tienda: ")
    if eleccion == "biblioteca":
        eleccion = input("Estas un rato estudiando y te quedas hasta que cierran, tienes que decidir como irte, andar/bus: ")
        if eleccion == "andar":
            eleccion = input("Vas andando pero ves que unos maleantes se acercan en tu direccion, te acaban parando, te sacan una navaja y te dicen que les des todo lo que tienes, que haces, llamar policia/huir: ")
            if eleccion == "llamar policia":
                print("Llamas a la policia con tu movil, estos aparecen rapidamente y se encargan de los maleantes, llegas andando a tu casa sin ningun problema mas \n **FELICIDADES HAS GANADO**")
            else:
                eleccion = input("Echas a correr pero te tropiezas, estas arrinconado, que haces, rendirse/pelear: ")
                if eleccion == "rendirse":
                    print("Te dejan irte pero no sin antes quitarte hasta los zapatos, vuelves vivo a casa de suerte y encima tu madre te regaña por imprudente \n **HAS SOBREVIVIDO**")
                else:
                    print("¿En serio? Que vas a hacer contra un arma blanca. Ya te puedes imaginar lo que pasa (nada bonito) \n **HAS PERDIDO**")
        else:
            print("Coges el bus y vuelves a casa sin mayor problema \n **FELICIDADES HAS GANADO**")
    else:
        eleccion = input("Vas a la tienda, cuanto decides gastarte, poco/mucho: ")
        if eleccion == "mucho":
            eleccion = input("Compraste bastantes cosas de la tienda gastandote asi todo el dinero que llevabas. \nAhora se hace de noche y tienes que volver, como vuelves, andar/bus: ")
            if eleccion == "andar":
                eleccion = input("Vas andando pero ves que unos maleantes se acercan en tu direccion, te acaban parando, te sacan una navaja y te dicen que les des todo lo que tienes, que haces, llamar policia/huir: ")
                if eleccion == "llamar policia":
                    print("Llamas a la policia con tu movil, estos aparecen rapidamente y se encargan de los maleantes, llegas andando a tu casa sin ningun problema mas \n **FELICIDADES HAS GANADO**")
                else:
                    eleccion = input("Echas a correr pero te tropiezas, estas arrinconado, que haces, rendirse/pelear: ")
                    if eleccion == "rendirse":
                        print("Te dejan irte pero no sin antes quitarte hasta los zapatos, vuelves vivo a casa de suerte y encima tu madre te regaña por imprudente \n **HAS SOBREVIVIDO**")
                    else:
                        print("¿En serio? Que vas a hacer contra un arma blanca. Ya te puedes imaginar lo que pasa (nada bonito) \n **HAS PERDIDO**")
            else:
                eleccion = input("Compraste tanto que no tienes dinero para el bus, por lo que no te queda otra que andar \nVas andando pero ves que unos maleantes se acercan en tu direccion, te acaban parando, te sacan una navaja y te dicen que les des todo lo que tienes, que haces, llamar policia/huir: ")
                if eleccion == "llamar policia":
                    print("Llamas a la policia con tu movil, estos aparecen rapidamente y se encargan de los maleantes, llegas andando a tu casa sin ningun problema mas \n **FELICIDADES HAS GANADO**")
                else:
                    eleccion = input("Echas a correr pero te tropiezas, estas arrinconado, que haces, rendirse/pelear: ")
                    if eleccion == "rendirse":
                        print("Te dejan irte pero no sin antes quitarte hasta los zapatos, vuelves vivo a casa de suerte y encima tu madre te regaña por imprudente \n **HAS SOBREVIVIDO**")
                    else:
                         print("¿En serio? Que vas a hacer contra un arma blanca. Ya te puedes imaginar lo que pasa (nada bonito) \n **HAS PERDIDO**")
        else:
            eleccion = input("Compraste un par de cosas, pero aun te sobra dinero \nAhora se hace de noche y tienes que volver, como vuelves, andar/bus: ")
            if eleccion == "andar":
                eleccion = input("Vas andando pero ves que unos maleantes se acercan en tu direccion, te acaban parando, te sacan una navaja y te dicen que les des todo lo que tienes, que haces, llamar policia/huir: ")
                if eleccion == "llamar policia":
                    if eleccion == "llamar policia":
                        print("Llamas a la policia con tu movil, estos aparecen rapidamente y se encargan de los maleantes, llegas andando a tu casa sin ningun problema mas \n **FELICIDADES HAS GANADO**")
                else:
                    eleccion = input("Echas a correr pero te tropiezas, estas arrinconado, que haces, rendirse/pelear: ")
                    if eleccion == "rendirse":
                        print("Te dejan irte pero no sin antes quitarte hasta los zapatos, vuelves vivo a casa de suerte y encima tu madre te regaña por imprudente \n **HAS SOBREVIVIDO**")
                    else:
                        print("¿En serio? Que vas a hacer contra un arma blanca. Ya te puedes imaginar lo que pasa (nada bonito) \n **HAS PERDIDO**")
            else:
                print("Al tener dinero de sobra, puedes pagar el bus. Subes y vuelves a casa sin mayor problema \n **FELICIDADES HAS GANADO**")   