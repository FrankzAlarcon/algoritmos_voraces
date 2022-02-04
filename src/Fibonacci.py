#Calcula el término (n+1)-ésimo de la secuencia de fibonacci
def fibonacci(num_termino):
  #Solo admite enteros positivos
  if num_termino < 0 or (type(num_termino) is not int):
    return "Solo enteros positivos";
  if (num_termino == 0 or num_termino == 1):
    #Si es 0 o 1 caso base, devuelve 1
    #fib(0) = 1, fib(1) = 1
    return 1;
  else: 
    #Suma los dos numeros anteriores
    return fibonacci(num_termino - 1) + fibonacci(num_termino - 2)