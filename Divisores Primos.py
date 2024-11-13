def divisores(numero):
    lista = [i for i in range(1, numero+1) if numero%i==0]
    return lista
