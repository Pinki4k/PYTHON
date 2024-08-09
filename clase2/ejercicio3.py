# Operdores aritmeticos
#imprimir la suma de 3 + 4
print("La suma de 10 + 4 es:", 3 + 4)

#Resolver todas las operaciones: 10-4, 10*4, 10/4, 10%4, 10//4, 10**4
print("el resultado de 10-4 es:", 10-4)
print("la operacion de 10*4 es:",10*4)
print("la operacion de 10/4 es:",10/4)
print("la operacion de 10%4 es:",10%4)
print("la operacion de 10**4", 10**4)
#resolver la ecuacion cuadratica: 2x-7x+3 = 0
a= 2
b= -7
c= 3
x1 =(b+ (b**2 - 4 *a *c)**0.5)/(2*a)
x2 =(b- (b**2 - 4 *a *c)**0.5)/(2*a)
print("el resultado de x1 es de:", x1)
print("el resultado de x2 es de:", x2)
# Operaciones con cadenas de texto
print("SNPP" + "CTTFPPJ " + " PROGRAMACION PYTHON")
#print("AULA " + 2102) #aqui tendremos un error, 2102 no es una cadena de texto. usar str()

# Operaciones mixtas
print("Tun chi " * 5)
print("Ja " * (2**3))

print(3 > 4)
print(3 < 4)
print(3>= 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

# Operaciones con cadenas de texto
print("python" > "PYTHON")
print ("aaaa" >="abaa") # Ordenacion alfabetica por ASCII
print(len("aaaa")>= len("abaa")) #Cuenta caracteres

print("python"!= "python")

### Operadores Logicos

print(10 > 4 and "Z" > "A")
print(10 > 4 or "Z" > "A")
print(not(10 > 4) and "Z" > "A")
