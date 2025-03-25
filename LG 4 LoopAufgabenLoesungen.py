# Aufgaben zu Loops

listeA = [1,2,3,4,5,6,7,8,9,10]

# Aufgabe 1: Gebe die Liste A bis zu der Zahl aus, 
#            deren Quadratzahl größer 50 ist.

print("\nAufgabe 1\n")

for n in listeA:
    if n ** 2 <= 50:
        print(n)
    else:
        break


# Aufgabe 2: Gebe aus Liste A die Zahlen aus,
#            deren Quadratzahlen nicht durch 3 teilbar sind.

print("\nAufgabe 2\n")

for n in listeA:
    if n**2 % 3 != 0:
        print(n) 
    else:
        continue

# Aufgabe 3: Erstelle ein Konsolenmenü, mit dem du wahlweise
#            eine der folgenden Listen ausgibst. 

listeA = [1,2,3,4,5,6,7,8,9,10]
listeB = [11,12,13,14,15,16,17,18,19,20]
listeC = [21,22,23,24,25,26,27,28,29,30]

print("\nAufgabe 3\n")

mod = ""
while mod != "x":
    print("a = Liste A\t b = Liste B\tc = Liste C")
    mod = input("Gebe den Buchstaben der Liste an, die du ausgeben willst oder x für 'Abbrechen':")
    match mod:
        case "a":
            print(listeA)
        case "b":
            print(listeB)
        case "c":
            print(listeC)
        case "x":
            break
        case _:
            pass

# Aufgabe 4: Gebe die Namen derjenigen Personen aus,
#            deren E-Mail-Adressen auf '@google.com' enden.
#      Tipp: Nutze dazu Methoden der Klasse 'str'.

mailadressen = ["max.mustermann@gmx.com"
                ,"anna.schmidt@google.com"
                ,"peter.müller@google.com"
                ,"lena.meier@gmx.com"
                ,"klaus.wagner@google.com"
                ,"maria.schulz@google.com"
                ,"thomas.becker@gmx.com"
                ,"julia.fischer@gmx.com"
                ,"michael.hoffmann@google.com"
                ,"sophia.weber@google.com"]

print("\nAufgabe 4\n")

for adr in mailadressen:
    if adr.endswith("@google.com"):
        tmp_str = adr.replace("@google.com", "")
        # tmp_str = tmp_str.replace(".", " ")
        tmp_str = tmp_str.split(".")
        for string in tmp_str:
            string = string.capitalize()
            print(string, end=" ")
        print()



if mailadressen[0].__contains__("x.com"):
    print("Hello")

print("stefan koschnik".title())


# Aufgabe 5: Erzeuge folgende Ausgabe mit einem Loop:
#            0
#            01
#            012
#            0123
#            01234

print("\nAufgabe 5\n")

n = 1
while n < 6:
    for num in range(n):
        print(num, end="")
    n += 1
    print()

# Variante 2

cnt = 0
liste_triangle = [0,1,2,3,4]
#print(liste_triangle[:cnt+3:])
while cnt < len(liste_triangle):
    print(*liste_triangle[:cnt+1:])
    cnt+=1

print(*liste_triangle)


# Aufgabe 6: Erzeuge folgende Ausgabe mit einem Loop:
#                *
#               ***
#              *****
#             *******
#            *********
"""
Tipp: Eine andere Darstellung könnte sein:

----*
---***
--*****
-*******
*********
"""

print("\nAufgabe 6\n")

hoehe = 7
for i in range(hoehe):
    # Leerzeichen vor den Sternen
    leerzeichen = ' ' * (hoehe - i - 1)
    # Sterne für die aktuelle Zeile
    sterne = '*' * (2 * i + 1)
    # Ausgabe der Zeile
    print(leerzeichen + sterne)

# Aufgabe 7: Erstelle eine Liste mittels 2 ranges,
#            die die Buchstaben in der Ascii Tabelle
#            repräsentieren. Gebe anschließend die 
#            die Buchstaben aus.
#      Tipp: Nutze dazu die Builtin- Funktionen list() und chr().

print("\nAufgabe 7\n")

import time

print(time.time())
buchstaben = list(range(65, 91)) + list(range(97, 123))
for b in buchstaben:
    print(chr(b), end="")
# 0,001393
print(time.time())

buchstaben_liste = []
for zahl in range (65, 123):
    if 91 <= zahl <= 96:
        continue
    buchstabe = chr(zahl)
    buchstaben_liste.append(buchstabe)
print(buchstaben_liste)
#0.000065
print(time.time())
 


