
#FUNCION PARA EL INICIO DE SESION, PIN, INTENTOS
def iniciar_sesion():
    contraseña = "1122" # contraseña designada
    intentos = 3        # intentos 
    print("--- INICIO DE SESIÓN ---")
    while intentos > 0:
        contraseña_ing = input(f"Ingrese su contraseña: ") 
        #si contraseña ingresada con contraseña designada son iguales, permite el acceso
        if contraseña_ing == contraseña:
            print("\nAcceso permitido")
            return True
        else:
        #si contraseña es diferente resta intentos hasta bloquear
            intentos -= 1
            print("Contraseña incorrecta.")
    print("\nAcceso negado, contacta a tu banco.")
    return False

#FUNCION PARA MOSTRAR MENU PRINCIPAL
def menu():
    print("\n--- Menu Cajero Automatico ---")
    print("1. Consultar Saldo")
    print("2. Depositar Dinero")
    print("3. Retirar Dinero")
    print("4. Historial de Movimientos") 
    print("5. Salir")
    return input("Seleccione una opción: ")

#FUNCION PARA SIMULAR EL PROGRAMA
def cajero():
    #si logra el login, continua con el programa
    if not iniciar_sesion():
        return 
    saldo = 1000.0  #saldo inicial 
    historial = []  #historial vacio
    continuar = True #True para continar

    print("\n--- Bienvenido al Banco Progreso ---")

    while continuar:
        opcion = menu()
        #si opcion es 1 un muestra saldo actual
        if opcion == "1":
            print(f"\n> Tu saldo actual es de: ${saldo:.2f}")
        #si opcion es 2 un muestra para depositar 
        elif opcion == "2":
            try:
                deposito = float(input("Ingrese el monto a depositar: "))
                # si es mayor que cero se ejecuta 
                if deposito > 0:
                    #suma elvalor actual con el deposito 
                    saldo += deposito
                    historial.append(f"Depósito: +${deposito:.2f}")
                    print("Depósito realizado.")
                    print(f'Saldo actual: ${saldo:.2f}')
                else:
                    print("El monto debe ser mayor a cero")
            except (ValueError):
                print("Ingrese solo números")
        
        #Opcion 3 para el retiro
        elif opcion == "3":
            retiro_limite = 500
            try:
                print('\nRecuerda que el monto máximo a retirar es de $500!')
                retiro = float(input("Ingrese el monto a retirar: "))
                #si el retiro es mayor que el saldo, muestra fondos insuficientes
                if retiro > retiro_limite:
                    print("El limite de retiro es $500, intenta de nuevo.")
                # si es igual a cero o menor, muestra lo siguiente
                elif retiro <= 0:
                    print("Ingrese un monto mayor a cero")

                elif retiro > saldo:
                    print("Fondos insuficientes.")
                else:
                    #si el saldo es mayor que retiro ejecuta todo el proceso
                    saldo -= retiro
                    historial.append(f"Retiro: -${retiro:.2f}")
                    print("Retiro realizado")
                    print(f'Saldo actual: ${saldo:.2f}')
            except (ValueError):
                print("Ingrese solo números")

        #si opcion es 4, ejecuta los movimientos recientes 
        elif opcion == "4":
            print("\n--- Movimientos de la Cuenta ---")
            #sino se encuentran movimientos, imprime lo siguiente
            if not historial:
                print("No hay movimientos recientemente")
            else:
                #si hay movimientos imprime todo lo reciente, ya sea deposito o retiro
                for movimiento in historial:
                    print(f"> {movimiento}")
            print(f"Saldo actual: ${saldo:.2f}")

        # si opcion es 5 sale del cajero 
        elif opcion == "5":
            print("Regresa pronto")
            continuar = False
        else:
            print("Ingresa una opción del (1-5)")

cajero()