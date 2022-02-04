
def busqueda_binaria(lista, x):

    # Busca en toda la lista dividiéndola en segmentos y considerando
    # a la lista completa como el segmento que empieza en 0 y termina
    # en len(lista) - 1.

    izq = 0  # izq guarda el índice inicio del segmento
    der = len(lista) - 1  # der guarda el índice fin del segmento

    # un segmento es vacío cuando izq > der:
    while izq <= der:
        # el punto medio del segmento
        medio = (izq+der)/2

        print("DEBUG:", "izq:", izq, "der:", der, "medio:", medio)

        # si el medio es igual al valor buscado, lo devuelve
        if lista[medio] == x:
            return medio

        # si el valor del punto medio es mayor que x, sigue buscando
        # en el segmento de la izquierda: [izq, medio-1], descartando la
        # derecha
        elif lista[medio] > x:
            der = medio-1

        # sino, sigue buscando en el segmento de la derecha:
        # [medio+1, der], descartando la izquierda
        else:
            izq = medio+1
        # si no salió del ciclo, vuelve a iterar con el nuevo segmento

    # salió del ciclo de manera no exitosa: el valor no fue encontrado
    return -1

# Código para probar la búsqueda binaria

def ingresarLista():
    lista=[]
    num=int(input("Cuantos elementos desea ingresar: "))
    for a in range(1,num+1):
        aux=input(f'Ingrese el elemento {a} : ')
        lista.append(aux) #Ingresamos el elemento a la lista
    lista.sort #Ordenamos la lista utilizando la funcion sort
    return lista

def busquedaBinaria(lista, busqueda):
    inicio = 0
    final = len(lista-1)
    while 

def menu():
    print('''
    \t*** Menu *** \t 
    1. Ingresar nueva lista
    2. Busqueda Binaria
    3. Salir
    ''')
    des=int(input("Seleccione una opcion: "))
    return des

def main():
    des=0
    while(des!=3):
        des=menu()
        if des==1:
            listaAux = ingresarLista()
            print(listaAux)
        elif des==2:

            print('2')
        elif des==3:
            print('Saliendo....')
        

# def main():
#     lista = input("Dame una lista ordenada ([[]] para terminar): ")
#     while lista != [[]]:
#         x = input("¿Valor buscado?: ")
#         resultado = busqueda_binaria(lista, x)
#         print "Resultado:", resultado
#         lista = input("Dame una lista ordenada ([[]] para terminar): ")
main()