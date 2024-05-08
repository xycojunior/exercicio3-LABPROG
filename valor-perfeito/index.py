def valor_perfeito(valor):
    soma_divisores = 0
    for i in range(1, valor):
        if valor % i == 0:
            soma_divisores += i
    return soma_divisores == valor 

print(valor_perfeito(28))