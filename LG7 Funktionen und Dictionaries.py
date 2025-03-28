# Aufgabe 1: Schreibe eine Funktion, die als Argument ein 
#            Dictionary von Vornamen und Nachnamen übernimmt.
#            Gebe mit dieser Funktion die Namen in der Form aus:
#            "Hallo, ich bin [Vorname] [Nachname]."

print("\nAufgabe 1\n")

zumTesten1 = {"Kater": "Garfield", "Räuber":"Hotzenplotz", "Pipi":"Langstrumpf"}

def hallo(namen:dict):
    for vn, nn in namen.items():
        print(f"Hallo, ich bin {vn} {nn}.")

hallo(zumTesten1)


# Aufgabe 2: Schreibe eine Funktion, die als Argument ein 
#            Dictionary von Waren und deren Preise übernimmt.
#            Die Funktion soll den Gesamtpreis zurückgeben.

print("\nAufgabe 2\n")
zumTesten2 = {"Milch": 1.0, "Butter": 3.5, "Brot":2.99, "Äpfel":1.98,"Kaffee":6.99}

def priceAll(waren:dict):
    return sum(waren.values())

print(priceAll(zumTesten2))

# Aufgabe 3: Schreibe eine Funktion, die als Argument das 
#            Dictionary aus Aufgabe 2 übernimmt. Die Funktion
#            soll die Warenbezeichnung des günstigsten und des 
#            teuersten Produkts ausgeben.

print("\nAufgabe 3\n")

def minmax(waren:dict):
    print(f"Günstigstes Produkt: ",*[k for k,v in waren.items() if v == min(waren.values())])
    print("Teuerstes Produkt: ",*[k for k,v in waren.items() if v == max(waren.values())])

minmax(zumTesten2)

# Variante Jaouad
def guenstig_teuer_produkt(waren_dict):
    
    guenstigster_key = min(waren_dict, key=waren_dict.get)
    teuerster_key = max(waren_dict, key=waren_dict.get)

    print(f"Günstigstes Produkt: {guenstigster_key} ({waren_dict[guenstigster_key]:.2f} €)")
    print(f"Teuerstes Produkt: {teuerster_key} ({waren_dict[teuerster_key]:.2f} €)")

guenstig_teuer_produkt(zumTesten2)

# Aufgabe 4: Schreibe eine Funktion, die als Argument ein 
#            verschachteltes Dictionary von Schülern und 
#            deren Noten in einzelnen Fächern übernimmt.
#            Die Funktion soll den Notendurchschnitt jedes 
#            Schülers und jedes Fachs zurückgeben.

print("\nAufgabe 4\n")

zumTesten4 = {
    "Max": {"Mathe": 2.5, "Deutsch": 1.2, "Englisch": 3.4},
    "Lena": {"Mathe": 1.5, "Deutsch": 2.4, "Englisch": 1.8},
    "Tom": {"Mathe": 3.3, "Deutsch": 3.0, "Englisch": 2.8}
}

def avgGrades(grades:dict):
    class_notes = {}
    for student, notes in grades.items():
        print(f"Der Notendurchschnitt von {student} ist {round(sum(notes.values())/len(notes.values()),1)}.")
    for topic in grades.values():         
        class_notes.update(topic)
    class_list = [[fach, 0, 0] for fach in class_notes.keys()]
    for classes in grades.values():
        for a_class, grade in classes.items():
            for topic in class_list:
                if a_class == topic[0]:
                    topic[1] += grade
                    topic[2] +=1
#    print(class_notes, class_list, sep="\n")
    for topic in class_list:
        print(f"{topic[0]} hat einen Notendurchschnitt von {round(topic[1]/topic[2],1)}.")

avgGrades(zumTesten4)


# Aufgabe 5: Schreibe eine Funktion, die als Argumente zwei Listen
#            übernimmt. Die eine Liste soll Artikelnummern enthalten,
#            die andere die dazugehörigen Waren. Die Funktion soll ein
#            Dictionary zurückgeben mit den Artikelnummer als Schlüssel
#            und den Waren als Wert.
#            Tipp: Beschäftige dich mit der Builtin- Funktion zip().

print("\nAufgabe 5\n")

artnr = [1000,1001,1002,1003,1004]
waren = ["Milch","Butter", "Brot", "Äpfel","Kaffee"]

def nrArt(nr:list, name:list):
    targetDict = {}
    for pair in zip(nr,name):
        targetDict.update({pair[0]:pair[1]})
    return targetDict

print(nrArt(artnr, waren))


# Aufgabe 6: Schreibe eine Funktion, die zwei Zahlenwerte als Argument übernimmt,
#            sie multipliziert und das Produkt zurückgibt. 
#            Schreibe dann eine namensgleiche Funktion, deren einziger Unterschied
#            darin besteht, dass sie drei Zahlenwerte übernimmt. Prüfe anschließend,
#            ob du die Funktion mit zwei Argumenten noch nutzen kannst.

print("\nAufgabe 6\n")

def multiply(a,b):
    return a*b

print(multiply(10,5))

def multiply(a,b,c):
    return a*b*c

print(multiply(10,5,3))
# print(multiply(10,5))

# Zeile 94 führt zu folgendem Fehler:

# Traceback (most recent call last):
#   File "c:\Users\StefanKoschnik\OneDrive - karriere tutor GmbH\Dokumente\Python\PYKT20250303\LG7 Funktionen und Dictionaries.py", line 94, in <module>
#     print(multiply(10,5))
#           ~~~~~~~~^^^^^^
# TypeError: multiply() missing 1 required positional argument: 'c'

# Das zeigt, dass die vorherige Funktionsdefinition
# überschrieben wurde.
# Ein Überladen von Funktionen (wie in anderen Programmiersprachen)
# ist in Python nicht möglich