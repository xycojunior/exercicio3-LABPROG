def idade_anos(anos, meses, dias):
    cal_anos = anos * 365
    cal_meses = meses * 30
    total_dias = cal_anos + cal_meses + dias
    return total_dias
print(idade_anos(40, 3, 8))
