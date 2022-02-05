class Elemento:
    def __init__(self, nombre, peso, beneficio):
        self.nombre = nombre
        self.peso = peso
        self.beneficio = beneficio
        self.beneficioxpeso = beneficio/peso

    def __str__(self):
        return f'Elemento: {self.nombre} Peso: {self.peso} Beneficio: {self.beneficio} '


def llenarObjetos(numElementos):
    objetos = []
    #Creamos una lista de nombres, pesos y beneficios
    nombres, pesos, beneficios = [], [], []
    #Identificamos en una sola linea ingresada por teclado cada nombre, pesos y beneficios  de los elementos separado por ", " 
    nombres = input('Ingrese el vector de elementos: *separados por una coma y espacio (, ) * : ').split(sep=', ')
    pesos = input('Ingrese el vector de pesss: *separados por una coma y espacio (, ) * : ').split(sep=', ')
    beneficios = input('Ingrese el vector de beneficios: *separados por una coma y espacio (, ) * : ').split(sep=', ')
    #Si existieron más elementos ingresados se redifine la lista con el num correcto
    nombres = nombres[:numElementos]
    pesos = pesos[:numElementos]
    beneficios = beneficios[:numElementos]
    #Vamos a iterar en las listas anteriores para crear objetos de tipo Elemento y almacenarlos en una nueva lista
    for a in range(numElementos):
        Auxiliar = Elemento(nombres[a],int(pesos[a]),int(beneficios[a]))
        objetos.append(Auxiliar)

    for x in objetos:
        print(x)






def main():
    p = int(input('Ingrese el numero de objetos que existen: ')) #Preguntamos cuantos objetos existen
    llenarObjetos(p)
 


main()


