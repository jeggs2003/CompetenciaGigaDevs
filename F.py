linea1 = input()
contador= 0;
arreglo = (linea1.split(' ', maxsplit= len(linea1)));
arreglo1 = []

for i in range (0, len(arreglo)):
    arreglo1.append(int(arreglo[i]))

energia = arreglo1[0]

desga = []
for i in range(0, arreglo1[1]):
    num = int(input())
    desga.append(num)

for i in range(0, arreglo1[2]):
    num = int(input())
    energia = energia + num
    contador = contador + 1;

for i in range(0,len(desga)):
    if(desga[i]<=energia):
        energia = energia - desga[i]
        contador = contador +1
    elif(desga[i]>energia):
        break;

print(contador)