def Fib(n):
    if n<2:
        return (1, n)
    
    chamadas_1, valor_1 = Fib(n-1)
    chamadas_2, valor_2 = Fib(n-2)

    return (1+chamadas_1+chamadas_2, valor_1+valor_1)

n = int(input())
chamadas, valor = Fib(n)

print(f"Fib({n}) = {valor} ({chamadas} chamadas)")
