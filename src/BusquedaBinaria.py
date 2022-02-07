import random
#Metodo para ingresar elementos a una lista
def ingresarLista():
    lista=[]
    num=int(input("Cuantos elementos desea ingresar: "))
    for a in range(1,num+1):
        aux=input(f'Ingrese el elemento {a} : ')
        lista.append(aux) #Ingresamos el elemento a la lista
    print(lista)
    lista.sort()
    return lista

def ingresarListaRandom():
    lista = []
    num = int(input("Cuantos elementos desea ingresar: "))
    for a in range(1, num+1):
        aux = random.randint(1,1000)
        lista.append(aux)  # Ingresamos el elemento a la lista
    print(lista)
    lista.sort()
    return lista

#Metodo de busqueda Binaria implementando la tecnica de programación Divide y Venceras
#Busca en toda la lista dividiéndola en segmentos 
def busquedaBinariaRecursiva(lista, bajo, alto, numero):
    #Recibe una lista de elementos donde va a buscar determinado numero 
    #Bajo y Alto equivalen a los valores de las posiciones extremas del rango de la lista
    # Determina la posicion mitad de la lista  
    if bajo > alto: #Caso Base
        #Si el numero a buscar no se encontró en la lista
        return -1
    mitad = (int(bajo) + int(alto)) // 2 #Calculamos la poscion media de la lista
    if lista[mitad] == numero:
        #Si se ecnontró el numero a buscar en la lista
        return mitad
    elif lista[mitad] < numero: 
        #Si el numero a buscar es mayor que el elemento mitad de la lista, sigue buscando
        #se conserva el rango desde la mitad hacia la derecha [medio+1, derecha], descartando la otra mitad izquierda
        return busquedaBinariaRecursiva(lista, mitad+1, alto, numero)
    else:
        #Caso Contrario, Si el numero a buscar es menor que el elemento mitad de la lista, sigue buscando
        #se conserva el rango desde la mitad hacia la izquierda [izquierda, medio-1] descartando la otra mitad derecha

        return busquedaBinariaRecursiva(lista, bajo, mitad-1, numero)
    
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
            num=int(input('Por favor ingrese el elemento a buscar: '))
            auxiliar = busquedaBinariaRecursiva(listaAux, 0, len(listaAux)-1, num)
            print(auxiliar)
            print(listaAux)
            if(auxiliar == -1):
                print("No se encontro el elemento en la lista")
            else:
                print(f'El elemento {num} se encuentra en la posición {auxiliar+1}')
        #Opcion 4
        elif des==4:
            print('Saliendo....')
        
main()