import random

while True:
    aleatorio = random.randrange(0, 3)
    elijePc = ""
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    opcion = int(input("Elege tu opcion "))

    if opcion == 1:
        eligeUsuario = "Piedra"
    elif opcion == 2:
        eligeUsuario = "Papel"
    elif opcion == 3:
        eligeUsuario = "Tijera"
    print("Elejiste: ", eligeUsuario)

    if aleatorio == 0:
        eligePc = "Piedra"
    elif aleatorio == 1:
        eligePc = "Papel"
    elif aleatorio == 2:
        eligePc = "Tijera"
    print("La maquina elijio: ", elijePc)
    print(". . .")
    if eligePc == "Piedra" and eligeUsuario == "Papel":
        print("Ganaste, papel envuelve Piedra")
    elif eligePc == "Papel" and eligeUsuario == "Tijera":
        print("Ganaste , Tijera corta papel")
    elif eligePc == "Tijera" and eligeUsuario == "Piedra":
        print("Ganaste, Piedra machaca Tijera")
    if eligePc == "Papel" and eligeUsuario == "Piedra":
        print("Perdiste, Papel envuelve Piedra")
    elif elijePc == "Tijera" and eligeUsuario == "Papel":
        print("Perdiste, Tijera corta Papel")
    elif eligePc == "Piedra" and eligeUsuario == "Tijera":
        print("Perdiste, Piedra machaca Tijera")
    elif eligePc == eligeUsuario:
        print("empate")

    