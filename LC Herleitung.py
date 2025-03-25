# Liste von 10 aufeinander folgenden Zahlen

# Variante 1: einfach so schreiben
liste = [1,2,3,4,5,6,7,8,9,10]

# Variante 2: Über einen while- Loop und der Methode append()
liste1 = []
cnt = 1
while cnt < 11:
    liste1.append(cnt)
    cnt+=1

# Variante 3: Ein range- Objekt in eine Liste konvertieren
liste2 = list(range(1,11))

# Variante 4: Über einen for- Loop und der Methode append()
liste3=[]
for n in range(1,11):
    liste3.append(n)

# Variante 5: List- Comprehension (LC)
# Die LC lässt sich aus dem for- Loop ableiten.
# Die Loop- Bedingung wird in die LC übernommen.
# Das append() entfällt, indem die Variable vor 
# die Loop- Bedingung geschrieben wird

liste4=[zahl for zahl in range(1,11)]

print(liste,liste1,liste2,liste3,liste4,sep="\n")

# Nur die geraden Zahlen von 0 bis 10
# Variante 1: LC mit step- Parameter im range- Objekt.
liste5=[zahl for zahl in range(0,11,2)]

# Variante 2: Über einen for- Loop und if- Verzweigung
liste6=[]
for n in range(0,11):
    if n % 2 == 0:
        liste6.append(n)
    else:
        continue

# Variante 3: Eine LC mit if- Verzeigung
liste7 = [zahl for zahl in range(0,11) if zahl%2==0]

# Alle geraden Zahlen wie sie sind 
# und alle ungeraden Zahlen um 1 erhöht

# Variante 1: Über einen for- Loop und if- else 
liste8=[]
for n in range(0,11):
    if n % 2 == 0:
        liste8.append(n)
    else:
        liste8.append(n+1)

# Variante 2: Eine LC mit if- else
liste9=[zahl if zahl%2==0 else zahl+1 for zahl in range(0,11)]

print(liste5, liste6,liste7,liste8, liste9,sep="\n")
# Alle gerade Zahlen direkt, 
# alle durch 3 teilbaren Zahlen um 1 erhöht 
# und alle anderen Zahlen um 3 erhöht

# Variante 1: Über einen for- Loop und if- elif- else
# kommt gleich

liste10=[]
for zahl in range(0,11):
    if zahl%2 == 0:
        liste10.append(zahl)
    elif zahl%3==0:
        liste10.append(zahl+1)
    else:
        liste10.append(zahl+3)

# Variante 2: Über eine LC mit verschachteltem if- else
liste11=[zahl if zahl%2==0 else zahl+1 if zahl%3==0 else zahl+3 for zahl in range(0,11)]

print(liste10,liste11, sep="\n")