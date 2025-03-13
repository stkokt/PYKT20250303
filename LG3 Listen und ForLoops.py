""" liste = [1, 2.5, "drei", [True, 5]]     #  leere Liste = [], = list()
print(liste[-1][1])
liste[3] = liste
print(liste[3])

string = "Hallo"

for c in string:
    print(c, end="\t")

print(string[1])

 """


listeA = [15, 7, 39, 13, 41, 21, 20, 4, 13, 
          16, 40, 28, 45, 12, 19, 10, 28, 36, 
          48, 14, 30, 3, 37, 26, 21, 1, 33, 33, 10, 11]

# Aufgabe 1: Durchlaufe die Liste A mit einem For- Loop
#            und gebe sie damit aus.

print("\nAufgabe 1\n")

for num in listeA:
    print(num, end=" ")

# Aufgabe 2: Gebe nur das erste und das letzte Element
#            der Liste A aus.

print("\nAufgabe 2\n")

print(f"Erstes Element: {listeA[0]}, letztes Element: {listeA[-1]}")

print("\nAlternative über Länge der Liste\n")
# Andere Variante
print(f"Erstes Element: {listeA[0]}, letztes Element: {listeA[len(listeA)-1]}")

# Aufgabe 3: Gebe nur die geradzahligen Elemente
#            der Liste A aus.

print("\nAufgabe 3\n")

for num in listeA:
    if num % 2 == 0:
        print(num, end=" ")

# Aufgabe 4: Ermittle und gebe aus, wieviele Elemente
#            die Liste A enthält.

print("\nAufgabe 4\n")

print(f"Anzahl der Elemente in der Liste: {len(listeA)}")

# Aufgabe 5: Gebe die Liste in der Form aus:
#            "Das 1. Element ist 15"
#            "Das 2. Element ist 7" usw.

print("\nAufgabe 5\n")

for idx, num in enumerate(listeA):
    print(f"Das {idx + 1}. Element der Liste ist {num}.")

# Aufgabe 6: Zähle die geraden und die ungeraden Zahlen
#            und gebe die jeweilige Anzahl aus.
#            Erhöhter Schwierigkeitsgrad: Nutze dafür nur eine(!)
#            Zählvariable vom Typ Liste.

print("\nAufgabe 6\n")

liste_cnt = [0,0]

for num in listeA:
    if num % 2 == 0:
        liste_cnt[0]+=1
    else:
        liste_cnt[1]+=1
print(f"Anzahl der geraden Zahlen: {liste_cnt[0]}")
print(f"Anzahl der ungeraden Zahlen: {liste_cnt[1]}")

# Aufgabe 7: Gebe die Liste A bis zur Hälfte aus.
#            (Letztes Element: 19)

print("\nAufgabe 7\n")

for idx, num in enumerate(listeA):
    if idx < len(listeA)/2:
        print(num, end = " ")

# Aufgabe 8: Gebe die Liste A ab der Hälfte aus.
#            (Erstes Element: 10)

print("\nAufgabe 8\n")

for idx, num in enumerate(listeA):
    if idx >= len(listeA)/2:
        print(num, end = " ")

# Aufgabe 9: Gebe alle Elemente der Liste A aus, 
#            die an einem geradzahligen Index stehen.

print("\nAufgabe 9\n")

for idx, num in enumerate(listeA):
    if idx % 2 == 0:
        print(num, end = " ")

# Aufgabe 10: Gebe das größte und das kleinste Element 
#             der Liste A aus, sowie die Summe
#             und den Durchschnitt aller Listenelemente.

print("\nAufgabe 10\n")

print(f"Größtes Element der Liste: {max(listeA)}")
print(f"Kleinstes Element der Liste: {min(listeA)}")
print(f"Summe aller Elemente der Liste: {sum(listeA)}")
print(f"Durchschnitt aller Element der Liste: {round(sum(listeA)/len(listeA), 2)}")

# Andere Variante:

print("\nAlternative mit Variablen\n")

maxVal = 0
minVal = listeA[0]
sumVal = 0
lenList = 0

for num in listeA:
    if num > maxVal:
        maxVal = num
    if num < minVal:
        minVal = num
    sumVal += num
    lenList += 1

print(f"Größtes Element der Liste: {maxVal}")
print(f"Kleinstes Element der Liste: {minVal}")
print(f"Summe aller Elemente der Liste: {sumVal}")
print(f"Durchschnitt aller Element der Liste: {round(sumVal/lenList, 2)}")



