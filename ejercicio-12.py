import sys

def contar(num):
    restult = 0
    for x in range(1, int(num)+1):
        restult = restult + x
    return restult


print("Ingrese un número...")
num = sys.stdin.read(1)
print(contar(num))
