def fibonacci(num_terminos):
  if (num_terminos == 0 or num_terminos == 1):
    return 1;
  else: 
    return fibonacci(num_terminos - 1) + fibonacci(num_terminos - 2)