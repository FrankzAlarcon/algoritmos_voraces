
def es_solucion(solucion, valor_devolver):
    total = 0
    for moneda in solucion: #Se recorre el conjunto solucoion para tomar los valores de m
        total = round(total + ( moneda[0] * moneda[1]), 2) #Valor con dos decimales
    if (total == valor_devolver): #Si suma el valor del vuelto es igual a lo que se ingreso por teclado
        return True
    else:
        return False

def cambio(conjunto_candidatos, valor_devolver):
    solucion = [] #Conjunto Solucion
    restante = valor_devolver #El vuelto restante
    while conjunto_candidatos and not es_solucion(solucion, valor_devolver):
        dato = conjunto_candidatos.pop()
        if (dato <= restante): #Si las cantidad de una moneda es menor al vuelto restante
            cantidad = restante // dato
            solucion.append([dato, cantidad]) #Se agrega al conjunto solucion la cantidad
            restante = round(restante - (dato * cantidad), 2) #Se redonde a dos cifras
    if(es_solucion(solucion, valor_devolver)):
        return solucion
    else:
        return None

monedas = [0.01, 0.05, 0.1, 0.25, 0.5, 1]
vuelto = cambio(monedas, 2.5)
print(vuelto)