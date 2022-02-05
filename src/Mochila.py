from operator import  attrgetter

from numpy import object0
class Elemento:
    def __init__(self, nombre, peso, beneficio):
        self.nombre = nombre
        self.peso = peso
        self.beneficio = beneficio
        self.beneficioxpeso = beneficio/peso

    def __str__(self):
        return f'Elemento: {self.nombre} Peso: {self.peso} Beneficio: {self.beneficio} BenefXUni: {self.beneficioxpeso}'


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
    
    return objetos


def llenarObjetosLista(listaEntrada):
    objetos = []
    for a in listaEntrada:
        Auxiliar = Elemento(a[0], int(a[1]), int(a[2]))
        objetos.append(Auxiliar)
    return objetos


def ordenar(elementos):
    ordenados = sorted(elementos, key=attrgetter('beneficioxpeso'))
    print('Elementos Ordenados')
    for x in ordenados:
        print(x)
    return ordenados

def funcionObjetivo(solucion, objetos):
    tamanioMochila = int(input('Ingrese el tamanio de la mochila: '))
    pesoActual = 0
    #Comenzamos a iterar desde atrás por que allí se ecnuentran los elementos con mayor beneficio por unidad.
    i = len(solucion)-1
    while((pesoActual <= tamanioMochila) and (i >= 0)): #,ientras el pesoActual no exceda el tamanioMochila y existan elementos para ingresar en la mochila
        print(f' peso actual: {pesoActual} peso del objeto {objetos[i].nombre} : {objetos[i].peso} \n')
        if(pesoActual + objetos[i].peso < tamanioMochila):
            #Tomamos el objeto
            solucion[i] = 1
            #Agreagamos al peso actual
            pesoActual += objetos[i].peso
            pocentaje = str(solucion[i] *100)
            print(f' peso actual: {pesoActual} || porcentaje tomado del objeto {objetos[i].nombre} : {pocentaje}% \n')
        else: #En caso que sea mayor al peso de la mochila
            #Tomamos una parte del objeto para completar el tamnio mochila
            solucion[i] = (tamanioMochila-pesoActual)/objetos[i].peso
            #Agreagamos al pesoActual
            pocentaje = str(solucion[i] * 100)
            pesoActual += ((tamanioMochila-pesoActual)/objetos[i].peso)*objetos[i].peso
            print(f' peso actual: {pesoActual} || porcentaje tomado del objeto {objetos[i].nombre} : {pocentaje}% \n')
        i= i-1
    return solucion


def main():
    des= menu()

    objetos = []  # Conjunto Objetos
    if(des==1):
        p = int(input('Ingrese el numero de objetos que existen: ')) #Preguntamos cuantos objetos existen
        #Llenamos los objetos 
        solucion = [[None] * p]  # Conjunto Solucion Vacio
        objetos=llenarObjetos(p)
        #Ordenamos la lista de objetos por beneficioxUni
        objetos=ordenar(objetos)
        #Funcion para reslver el problema
        solucion = funcionObjetivo(solucion, objetos)
        for x in solucion:
            print(x)
    else:
        objetosEntrada = [('1', 18, 25), ('2', 15, 24), ('3', 10, 15), ]
        p = int(len(objetosEntrada))
        solucion = [None] * p  # Conjunto Solucion Vacio
        print(solucion)
        print(len(solucion))
        objetos = llenarObjetosLista(objetosEntrada) 
        objetos = ordenar(objetos)
        solucion2 = funcionObjetivo(solucion, objetos)
        for x in solucion2:
            print(x)
def mostrarSolucion(solucion, objetos):
    solucionImpresa = ""
    total = 0
    for a in solucion:
        solucionImpresa = solucionImpresa + solucion 

def menu():
    des= input(''' \tMenu 
    1. Ingresar valores manualmente
    2. Valores previamente definidos
    Seleccione Una Opcion: ''')
    return int(des)



main()


