def fatorial(n):
   
    if n < 0:
        raise ValueError("Fatorial não definido para números negativos.")
    if n == 0:
        return 1
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado