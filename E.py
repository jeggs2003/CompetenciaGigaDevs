Optimiza este código de Python
linea1 = input()

datos = []
datos = (linea1.split(' ', maxsplit= 2));

numero = int(datos[0])
posciongn = int(datos[1])
polen = []
polen2 = []

linea2 = input()
polen2 = linea2.split(' ', maxsplit= numero);

for i in range (0, numero):
    polen.append(int(polen2[i]))
contador = 0;

for i in range (0,posciongn):
    contador = 0;
    polen.sort();
    valorstring = str(polen[numero-1])
    for i in range (0, len(valorstring)):
        contador = contador + int(valorstring[i]);
    polen[numero-1] = polen[numero-1] - contador;

print(contador)
