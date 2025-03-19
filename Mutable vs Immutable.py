# Mutable vs Immutable

""" Mutable (veränderbar) sind

    L = Listen
    S = Sets
    D = Dictionaries    
"""

a = 10
print("Wert von a nach Initialisierung: ", end = "\t")
print(a)
print("Adresse von a nach Initialisierung: ", end = "\t")
print(id(a))

a = 11
print("\nWert von a nach Neuzuweisung: ", end = "\t")
print(a)
print("Adresse von a nach Neuzuweisung: ", end = "\t")
print(id(a))

b = 10
print("\nWert von b nach Initialisierung: ", end = "\t")
print(b)
print("Adresse von b nach Initialisierung: ",id(b))

"""
  Das Speicherkonzept von Python funktioniert anders als in
  anderen Programmiersprachen. In Python bekommen Werte eine 
  Speicheradresse, nicht Variablen. Daher greifen Variablen 
  auf dieselbe Speicheradresse zu, wenn sie denselben Wert
  annehmen.
  In der folgenden Liste ist die 10 das letzte Element. Auch hier
  wird auf die Speicheradresse der 10 geschaut, also dieselbe wie b.
"""

liste = [8,9,10]
print("\nAdresse von 10 in Liste: ",id(liste[-1]))

"""
Initialisierung der Variable c durch Zuweisung (des Wertes) von a.
c schaut jetzt auf die Speicheradresse von 11, weil a den Wert 11 hat.
"""
c = a
print("\nWert von c nach Initialisierung mit a: ", c)

"""
Die Frage ist: Bleiben die Variablen a und c miteinander
verknüpft? Ändert also die Variable c ihren Wert, wenn der 
Wert von a geändert wird?
"""
a = 12
print("\nWert von a nach Neuzuweisung: ", a)
print("Wert von c nach Neuzuweisung von a: ",c)

"""
Die Antwort ist also "Nein" für unveränderbare
Datentypen. Aber wie ist das bei veränderbaren
Datentypen?
Wir weisen der Liste 1 die Liste von oben zu:
"""

liste1 = liste
print("\nWerte von liste1 nach Initialisierung mit liste: ", liste1)

"""
Liste 1 enthält jetzt dieselben Werte wie Liste.
Wir verändern nun einen Wert innerhalb(!) der Liste
und beobachten, ob sich damit auch die Werte der 
Liste 1 verändert haben.
"""
liste[1] = 7
print("\nWerte von liste1 nach Änderung innerhalb liste: ",liste1)

"""
Antwort: Ja, auch die Werte von Liste 1 ändern sich.
Warum ist das so? Schauen wir uns mal die Adresse von 
Liste und Liste 1 und deren Elemente an.
"""
print("\nAdressen der liste und deren Elemente:")
print(hex(id(liste)))
print(hex(id(liste[0])))
print(hex(id(liste[1])))
print(hex(id(liste[2])))

liste[2] = 11

print(liste)
print(hex(id(liste)))
print(hex(id(liste[0])))
print(hex(id(liste[1])))
print(hex(id(liste[2])))

print(liste1)
print(hex(id(liste1)))
print(hex(id(liste1[0])))
print(hex(id(liste1[1])))
print(hex(id(liste1[2])))

liste2 = liste.copy()
print(liste2)
print(liste2)
print(hex(id(liste2)))
print(hex(id(liste2[0])))
print(hex(id(liste2[1])))
print(hex(id(liste2[2])))

liste = [8,7,11]
print(id(liste), id(liste1))
print(liste1)

liste3 = [1]
print(len(liste3))
if liste3:
    print("Hallo")

string5 = "St3fan"
print(len(string5))

print(len(3))



