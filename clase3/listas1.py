calificaciones = [2,5,5,4,5,1]
nombres = ["Moises","Camila","Fernanda", "Pablo","Tania"]
lista_variada = [True, 10.5, "abc", [0,1,1]]

print("Estudiante:", nombres[2])
print ("Calificaciones:", calificaciones[-2])
print("Litas dentro de otra", lista_variada[3][0])
print("Imprimir un rango o slices",nombres [1:2])
print(lista_variada)

#agregar elementos a una listas
nombres.append("Anibal")
print(nombres)
#remover elementos de una lista
nombres.remove("Pablo")
print(nombres)