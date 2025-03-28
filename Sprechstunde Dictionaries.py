"""
Die 11 Dictionary Methoden:

.clear()	    Löscht alle Einträge des Dictionarys
.copy()	        Erstellt eine flache Kopie
.fromkeys()	    Erstellt eine Kopie aus den Schlüsseln eines Iterables
.get()	        Liest einen Wert zu einem übergebenen Schlüssel aus
.items()	    Gibt alle Schlüssel und Werte aus
.keys()	        Zeigt die Schlüssel eines Dictionary an
.pop()	        löscht den Eintrag aus dem Dictionary des übergebenen Schlüssels 
                und liefert dessen Inhalt als Rückgabewert
.popitem()	    Liefert einen Eintrag als Tupel zurück und löscht den Eintrag aus 
                dem Dictionary (im Gegensatz zu pop() muss kein Schlüssel übergeben werden)
.setdefault()	liefert den Wert eines Eintrags aus dem Dictionary, wenn der Schlüssel 
                vorhanden ist. Ist kein entsprechender Schlüssel vorhanden, wird ein 
                Schlüssel mit dem Wert im Dictionary gespeichert
.update()	    Aktualisiert einen Wert, wenn der Schlüssel vorhanden ist. Wenn noch 
                kein entsprechender Schlüssel vorhanden ist, wird Wert und Schlüssel eingetragen
.values()	    Liefert alle Werte des Dictionary zurück (ohne Schlüssel)

"""
#              key  : value
warenliste = {"Milch": 1.0, "Butter": 3.5, "Brot":2.99, "Äpfel":1.98,"Kaffee":6.99}
#             |-- ITEM --|

print("\nZeile 27 - 30\n")
print(warenliste.get("Milch"))  # Nur Rückgabe eines Wertes zu einem Key.
print(warenliste["Milch"])      # Hier auch Rückgabe eines Wertes zu einem Key,
warenliste["Milch"] += 1        # aber auch Veränderung des Wertes möglich.
print(warenliste.keys())        # Gibt die Schlüssel zurück, also Milch, Butter...

print("\nZeile 34 und 35\n")

for key in warenliste.keys():   # Ausgabe der Schlüssel in einem Loop
    print(key, end= " ")

print("\n\nZeile 39\n")

print(warenliste.values())      # Gibt die Werte zurück, also 2, 3.5, 2.99...

print("\nZeilen 43, 44\n")

for value in warenliste.values(): # Ausgabe der Schlüssel in einem Loop
    print(value, end= " ")

print("\n\nZeile 48\n")

print(f"Summe der Preise:  {round(sum(warenliste.values()),1)}") # Summieren der Werte

print("\nZeile 52\n")

print(warenliste.keys(), warenliste.values(), sep="\n") # Ausgabe beider Reihen

print("\nZeile 56\n")

print(warenliste.items())   # Ausgabe der Items, also paarweise (Schlüssel, Wert)

print("\nZeilen 60,61\n")

for produkt, preis in warenliste.items():   ## Ausgabe der Items in einem Loop
    print(produkt, preis, sep=" : ")


