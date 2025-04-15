# Aufgaben zu Funktionen mit variablen Argumenten,
# Keywordargumenten und Funktionen als Argument

# Aufgabe 1: Schreibe eine Funktion, die beliebig viele
#            Strings als Argumente übernimmt und sie 
#            konkatiniert (also aneinander hängt).

print("\nAufgabe 1\n")

def konkatiniere(*strings):
    return "".join(strings)

print(konkatiniere("Hallo", "Welt"))


# Aufgabe 2: Schreibe die Funktion aus Aufgabe 1 so um,
#            dass zusätzlich ein Trennzeichen als Argument
#            übergeben werden kann 
#            (aber nicht muss, also Defaultwert für Trennzeichen definieren).

print("\nAufgabe 2\n")

def konkatiniereMitTrennzeichen(*strings, trennzeichen = ""):
    return f"{trennzeichen}".join(strings)

print(konkatiniereMitTrennzeichen("Hallo", "Welt", trennzeichen = " "))

# Aufgabe 3: Schreibe eine Funktion, die Keywordargumente übernimmt, mit denen
#            sie einen formatierten Briefkopf ausgibt.
#            z.B. in der Form:
#            Frau
#            Lisa Müller
#            Bahnhofstraße 5
#            12345 Berlin

print("\nAufgabe 3\n")

mueller = {"anrede":"Frau", "vorname":"Lisa", 
           "nachname":"Müller", "strasse":"Bahnhofstraße",
           "hausnummer":"5","plz":"12345","stadt":"Berlin"}

def briefkopf(**personendaten):
    print(personendaten['anrede'])
    print(personendaten['vorname'], personendaten['nachname'])
    print(personendaten['strasse'], personendaten['hausnummer'])
    print(personendaten['plz'], personendaten['stadt'])

briefkopf(**mueller)

print()

briefkopf(anrede="Frau", vorname="Lisa", nachname="Mueller", strasse="Bahnhofstraße", hausnummer="5", plz="12345", stadt="Berlin")


# Aufgabe 4: Schreibe eine Funktion, die eine Argumentenliste von Zahlen
#            und eine Funktion als Argument übernimmt, mit der die Zahlen
#            verarbeitet werden. 
#            Schreibe zwei Funktionen, die du als Argument in dieser Funktion
#            verwenden kannst.
#            1. verdopple(zahl) : Soll jede übergebene Zahl verdoppeln
#            2. filtereUngerade(): Soll nur ungerade Zahlen zurückgeben

print("\nAufgabe 4\n")

def verarbeite(func:callable, *zahlen):
    t=list()
    for zahl in zahlen:
        if func(zahl) != None:
            t.append(func(zahl))
    return tuple(t)
    
def verdopple(zahl):
    return zahl*2

def filtereUngerade(zahl):
    if zahl % 2 == 1:
        return zahl

a,b,c =verarbeite(verdopple, 1,2,3)
print(a,b,c)

print(verarbeite(filtereUngerade, 1,2,3))

