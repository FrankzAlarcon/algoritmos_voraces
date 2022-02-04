from Fibonacci import fibonacci


if __name__ == "__main__":
  secuenciaFibonacci = ""
  for number in range(10):
    secuenciaFibonacci = secuenciaFibonacci + str(fibonacci(number)) + ", "
  print(str(secuenciaFibonacci[:-2]))
  print(fibonacci(5))