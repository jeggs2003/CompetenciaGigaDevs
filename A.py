
linea1 = input()

posicion = int(linea1.index(" "))
strnumero = "";
strestatura = "";

for i in range (0,posicion):
    strnumero = strnumero + linea1[i];

for i in range (posicion, len(linea1)):
    strestatura = strestatura + linea1[i];

numero = int(strnumero)
estatura = int(strestatura)
minimas = []

linea2 = input()
conc = ""
for i in range (0,len(linea2)):
    if(linea2[i]!=" "):
        conc = conc + linea2[i];

    elif(linea2[i]== " " ):
        num = int(conc)
        minimas.append(num)
        conc = ""
        num = 0

num = int(conc)
minimas.append(num)

contador = 0;

for i in range (0,numero):
    if(minimas[i]<=estatura):
        contador = contador + 1


print(contador)

