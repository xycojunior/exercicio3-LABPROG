def verifica_vogal(caractere):
    vogais = "aeiouAEIOU"
    if caractere in vogais:
        return 1
    else:
        return 0
print(verifica_vogal("b"))