class Persona:

    def avanza(self):
        print('Anda caminando')





class Ciclista(Persona):

    def __init__(self, nombre):
        super(). __init__(nombre)

    def avanza(self):
        print('Anda moviendome en bicicleta')


if __name__ == '__main__':
    persona = Persona('Pepe')
    persona.avanza()

    ciclista = Ciclista('Juanca')
    ciclista.avanza()