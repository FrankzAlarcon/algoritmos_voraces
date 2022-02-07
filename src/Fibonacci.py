#Calcula el término (n+1)-ésimo de la secuencia de fibonacci

complejidad = 0

def fibonacci(num_termino):
  global complejidad
  #Solo admite enteros positivos
  if num_termino < 0 or (type(num_termino) is not int):
    return "Solo enteros positivos";
  if (num_termino == 0 or num_termino == 1):
    #Si es 0 o 1 caso base, devuelve 1
    #fib(0) = 1, fib(1) = 1
    complejidad =complejidad + 1
    return 1;
  else: 
    #Suma los dos numeros anteriores
    complejidad =complejidad + 1
    return fibonacci(num_termino - 1) + fibonacci(num_termino - 2)

def mostrarSerieFibonacci(num_datos):
    global complejidad
    secuenciaFibonacci = ""
    complejidadTotal = 0
    for number in range(num_datos):
      secuenciaFibonacci = secuenciaFibonacci + str(fibonacci(number)) + ", "
      print('Complejidad del fibonacci de ' + str(number) + ' es ' + str(complejidad))
      complejidadTotal = complejidadTotal + complejidad
      complejidad = 0
    print('Secuencia: ' + str(secuenciaFibonacci[:-2]))
    print('Tiene una complejidad total de: ' + str(complejidadTotal))

if __name__ == "__main__": 
  mostrarSerieFibonacci(10)