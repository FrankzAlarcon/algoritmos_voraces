#importamos cmath para emplear la funcion log
from cmath import log
# Definicion de la funcion es_solucion, ingresando como parametros un arrary que contiene el dato y la cantidad, y el valor a devolver
def es_solucion(solucion, valor_devolver):
    #Inicializacion de total en 0
    total = 0
    #Se repite hasta que no existan elementos en solucion, almacenando cada elemento de solucion en la variable moneda
    for moneda in solucion:
        #total se forma a partir de redondear a dos decimales la suma del total mas el producto de los dos primeros elementos del vector 
        #Se repite hasta que se acabe el vector solucion, insertando los valores que tiene inicialemnte y repitiendolo hasta completar el valor a devolver
        total = round(total + ( moneda[0] * moneda[1]), 2)
    #de tener todas las monedas a devolver emplea un condicional de igualdad que retorna true en caso de que el total sea igual al valor a devolver    
    #en caso contrario retorna false
    if (total == valor_devolver):
        return True
    else:
        return False
 #Define la funcion que imprime un vector que almacena vectores donde se imprime el valor de la moneda y la cantidad de onedas
def cambio(conjunto_candidatos, valor_devolver):
    solucion = []
    #ordenamos el vector con la finalidad que en un inicio el algoritmo escoga las monedas de denominacion mas altas para que se use 
    #La menor cantidad de monedas posible
    conjunto_candidatos.sort()
    #inicializa el restante igualando con el valor_devolver ingresado
    restante = valor_devolver
    #Realiza repeticiones mientras el vector conjunto_candidatos tenga datos, y es_solucion con los valores hasta ese entonces del vector solucion sea falso 
    while conjunto_candidatos and not es_solucion(solucion, valor_devolver):
        #Saca datos del vector conjunto_candidatos
        dato = conjunto_candidatos.pop()
        #compara si el dato es menor o igual al valor restante
        if (dato <= restante):
        #la cantidad sale partir de la parte entera del cociente al realizar la divicion entre restante y dato respectivamente    
            cantidad = restante // dato
            #se almacena el valor almacenado en dato y cantidad en el arreglo de vectores solucion 
            solucion.append([dato, cantidad])
            #el restante es a partir de reedondear a dos decimales el restante menos el dato multiplicada por la cantidad
            restante = round(restante - (dato * cantidad), 2)
            complejidad = complejidad + 1
    #Si es_solucion da el valor de verdadero implica que existe una forma de devolver el valor, caso contrario  imprimie none        
    if(es_solucion(solucion, valor_devolver)):
        #Calculo de complejidad
        complejidad=(2*len(solucion) + 1 + len(solucion)*log(len(solucion)))
        print("El valor de la complejidad del algoritmo es: ", complejidad)
        return solucion
    else:
        return None

monedas = [0.01, 0.05, 1, 0.25, 0.5, 0.1]
vuelto = cambio(monedas, 0.75)
print("La cantidad necesaria para devolver el vuelto es: ", vuelto)
