from operator import  attrgetter
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
        #Va tomando el correspondiente indice de la listaEntrada y asignando a los argumentos para crear un objeto e tipo Elemento
        Auxiliar = Elemento(a[0], int(a[1]), int(a[2]))
        #En la lista va agregando los objetos de tipo Elemento
        objetos.append(Auxiliar)
    return objetos

#Funcion para ordenar la lista de Elementos que recibe mediante el atributo beneficioxpeso 
def ordenar(elementos):
    ordenados = sorted(elementos, key=attrgetter('beneficioxpeso'))
    print('Elementos Ordenados')
    for x in ordenados:
        print(x)
    return ordenados

complejidad = 0
#Funcion que resulve el problema planteado
# Teorema: si se ordenan los objetos de forma decreciente en cuanto a su relación (utilidad/ponderación= bi/ci), y se introducen en la mochila enteros en este orden mientras quepan, y cuando no quede capacidad para uno entero se añade la porción que aún tenga cabida, el resultado al que se llega es una solución óptima.
def funcionObjetivo(solucion, objetos):
    global complejidad
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
            complejidad = complejidad + 1
        else: #En caso que sea mayor al peso de la mochila
            #Tomamos una parte del objeto para completar el tamnio mochila
            solucion[i] = (tamanioMochila-pesoActual)/objetos[i].peso
            #Agreagamos al pesoActual
            pocentaje = str(solucion[i] * 100)
            pesoActual += ((tamanioMochila-pesoActual)/objetos[i].peso)*objetos[i].peso
            print(f' peso actual: {pesoActual} || porcentaje tomado del objeto {objetos[i].nombre} : {pocentaje}% \n')
            complejidad = complejidad + 1
        i= i-1
    return solucion

#Funcion para imprimir en un formato el conjunto solucion
def mostrarSolucion(solucion, objetos):
    solucionImpresa = ""
    total = 0
    for a in range(len(solucion)):
        solucionImpresa = solucionImpresa + str(solucion[a]) +' .......'
        total += (solucion[a]) * objetos[a].beneficio
    solucionImpresa = solucionImpresa + '\nBeneficio Total: '+ str(total)
    return solucionImpresa

# Funcion para imprimir opciones, retorna el valor ingesado por teclado
def menu():
    des = input(''' \tMenu 
    1. Ingresar valores manualmente
    2. Valores previamente definidos
    Seleccione Una Opcion: ''')
    return int(des)

def main():
    global complejidad
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
        print(mostrarSolucion(solucion, objetos))
        print('Tiene una complejidad total de: ' + str(complejidad))
    else:
        objetosEntrada = [('1', 18, 25), ('2', 15, 24), ('3', 10, 15), ]
        p = int(len(objetosEntrada))
        solucion = [None] * p  # Conjunto Solucion Vacio
        objetos = llenarObjetosLista(objetosEntrada) 
        objetos = ordenar(objetos)
        solucion = funcionObjetivo(solucion, objetos)
        #Mostramos la solucion
        print(mostrarSolucion(solucion, objetos))
        print('Tiene una complejidad total de: ' + str(complejidad))

main()


