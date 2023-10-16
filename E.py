linea1 = input()
numero, posciongn = map(int, linea1.split(maxsplit=2))

linea2 = input()
polen = list(map(int, linea2.split(maxsplit=numero)))

for _ in range(posciongn):
    polen.sort()
    max_valor = polen[-1]
    contador = sum(map(int, str(max_valor)))
    polen[-1] -= contador

print(contador)