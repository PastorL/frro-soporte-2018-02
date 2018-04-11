def generar_n_caracteres(num,n):
    restult = ""
    for x in range(0, num):
        restult = restult + n
    return restult

print(generar_n_caracteres(9,"M"))
