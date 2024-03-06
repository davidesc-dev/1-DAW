import banco

def main():
    while True:
       
        opcion = banco.menu()
        
        if opcion == "1":
            banco.crearcuenta()
        elif opcion == "2":
            banco.consultardatos()
        elif opcion == "3":
            banco.ingreso()
        elif opcion == "4":
            banco.retirada()
        elif opcion == "5":
            banco.transferencia()
        elif opcion == "6":
            banco.calcularintereses()
        elif opcion == "7":
            banco.mostrarcuentascorrientes()
        elif opcion == "8":
            banco.mostrarcuentasahorro()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

        control = str(input("\nPulse cualquier tecla para continuar o Q para salir: "))
        if control == "q" or control == "Q":
            exit()


if __name__ == "__main__":
    main()
