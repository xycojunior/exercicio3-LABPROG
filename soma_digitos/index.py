def soma_digitos(numero):
    numeroStr = str(numero)
    soma = sum(int(digito) for digito in numeroStr)
    return soma
    
print(soma_digitos(2222))