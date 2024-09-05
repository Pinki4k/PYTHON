diccionario ={"Hola": "Hello","Chau":"Bye"}

while True:
    palabra = input("Ingrese una palabra a traducir: ")


    if(palabra in diccionario):
        print("Español : Ingles")
        print(f"{palabra} : {diccionario[palabra]}")

    else:
        print("La palabra no existe")
        resp =input("Desea registralo (si/no), Salir(x) ")
        if resp == "si" or resp == "yes":
            traduccion = input("Ingrese la traduccion ")
            if traduccion !="":
                diccionario[palabra] = traduccion
        elif(resp == "x"):
            break