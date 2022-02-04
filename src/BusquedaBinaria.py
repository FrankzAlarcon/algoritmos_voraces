import random
#Metodo para ingresar elementos a una lista
def ingresarLista():
    lista=[]
    num=int(input("Cuantos elementos desea ingresar: "))
    for a in range(1,num+1):
        aux=input(f'Ingrese el elemento {a} : ')
        lista.append(aux) #Ingresamos el elemento a la lista
    print(lista)
    return lista

def ingresarListaRandom():
    lista = []
    num = int(input("Cuantos elementos desea ingresar: "))
    for a in range(1, num+1):
        aux = random.randint(1,1000)
        lista.append(aux)  # Ingresamos el elemento a la lista
    print(lista)
    return lista

#Metodo de busqueda Binaria implementando la tecnica de programación Divide y Venceras
#Busca en toda la lista dividiéndola en segmentos 
def busquedaBinaria(lista, numero):
    #Recibe una lista de elementos donde iterar y el elemento a buscar
    # Determina el rango del segmento a bucar que empieza en 0 y termina en len(lista) - 1.
    inicio = 0  
    final = len(lista)-1
    lista.sort()  # Ordenamos la lista utilizando la funcion sort
    #Itera mientras el rango del segmento a buscar tenga elementos
    while inicio <= final:
        #Seleccionamos la posicion mitad
        mitad = int((inicio+final)/2)
        #Verificamos si el elemento mitad es igual al numero a buscar
        if lista[mitad]==numero:
            #Se retorna su posicion
            return mitad
        #Si el numero a buscar es menor que el elemento mitad de la lista, sigue buscando
        elif lista[mitad] > int(numero):
            #se conserva el rango de la izquierda: [izq, medio-1], descartando la otra mitad de la derecha
            final = mitad-1
        #Si el numero a buscar es mayor que el elemento mitad de la lista, sigue buscando
        else:
            #se conserva el rango de la derecha: [izq, medio-1], descartando la otra mitad de la izquierda
            inicio = mitad+1
        # si no salió del ciclo, vuelve a iterar con el nuevo rango definico

    # Si salió del ciclo sin retorn nada, el valor no se encuentra en la lista retornando -1
    return -1

def menu():
    print('''
    \t*** Menu *** \t 
    1. Ingresar nueva lista
    2. Ingresar Lista Random
    3. Busqueda Binaria
    4. Salir
    ''')
    des=int(input("Seleccione una opcion: "))
    return des

def main():
    des=0
    listaAux = []
    while(des!=4):
        des=menu()
        #Opcion 1
        if des==1:
            listaAux = ingresarLista()
        #Opcion 2
        elif des == 2:
            listaAux = ingresarListaRandom()
        #Opcion 3
        elif des==3:
            num=input('Por favor ingrese el elemento a buscar: ')
            auxiliar=int(busquedaBinaria(listaAux, num))
            print(listaAux)
            if(auxiliar==-1):
                print("No se encontro el elemento en la lista")
            else:
                print(f'El elemento {num} se encuentra en la posición {auxiliar+1}')
        #Opcion 4
        elif des==4:
            print('Saliendo....')
        
main()