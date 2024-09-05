acceso = {"Juan": 9921, "Lucas": 2122}

user = input("Ingrese su Usuario: ")
password = int(input("Ingrese su contraseña: "))

if user in acceso:
    if acceso[user] == password:
        print("Acceso Correcto")
    else:
        contador = 2
        while contador <=3:
            print(f"Contraseña incorrecta. Vuelve a Intentarlo {contador}")
            password = int(input("Ingrese su contraseña:"))
            if acceso[user] == password:
                print("Acceso Correcto")
                break
            contador += 1
        if(contador > 3):
            print("Ya no tienes intentos intenta mas tarde...")

else:
    print("El Usuario no exite")