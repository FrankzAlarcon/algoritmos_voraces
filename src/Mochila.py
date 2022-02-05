class elemento:
    def __init__(self, nombre, peso, beneficio):
        self.nombre = nombre
        self.peso = peso
        self.beneficio = beneficio
        self.beneficioxpeso = beneficio/peso


def llenarObjetos(numElementos):
    objetos = []
    #Creamos una lista de nombres, pesos y beneficios
    nombres = [], pesos = [], benificios = []
    #Identificamos en una sola linea ingresada por teclado cada nombre, pesos y beneficios  de los elementos separado por ", " 
    nombres = input('Ingrese el vector de elementos: *separados por una coma y espacio (, ) * = ').split(sep=', ')
    pesos = input('Ingrese el vector de elementos: *separados por una coma y espacio (, ) * = ').split(sep=', ')
    benificios = input('Ingrese el vector de elementos: *separados por una coma y espacio (, ) * = ').split(sep=', ')
    #Si existieron más elementos ingresados se redifine la lista con el num correcto
    nombres = nombres[:numElementos]
    pesos = pesos[:numElementos]
    
   


    
    
    for x in range(0, len(nombres)):


    peso = input('Ingrese el peso del elemento: ')
    for elemento in range (numElementos):
        print
        



def main():
    p = int(input('Ingrese el numero de objetos que existen: ')) #Preguntamos cuantos objetos existen
    llenarObjetos(p)
 


['1', '2', '3, 4, 5']

main()


