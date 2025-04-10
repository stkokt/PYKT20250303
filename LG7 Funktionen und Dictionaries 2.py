# Aufgabe 1: Schreibe eine Funktion, die einen Münzwurf
#            simuliert und das Ergebnis ausgibt. Nutze dazu 
#            eine geeignete Methode des random- Moduls.

print("\nAufgabe 1\n")

def flipcoin()->None:
    from random import choice
    print(choice(["Kopf", "Zahl"]))

flipcoin()

# Alternative mit Rückgabewert
def flipcoin1()->str:
    from random import choice
    return choice(["Kopf", "Zahl"])

print(flipcoin1())

# Aufgabe 2: Schreibe eine Funktion, die mehrere Münzwurfe
#            simuliert und die Häufigkeit von Kopf und Zahl
#            ausgibt. Nutze dazu eine geeignete Methode des 
#            random- Moduls.

print("\nAufgabe 2\n")

def multiFlipcoin(loops):
    from random import choice
    kopf = 0
    zahl = 0
    for n in range(loops):
        wurf = choice(["Kopf", "Zahl"])
        if wurf == "Kopf":
            kopf += 1
        else:
            zahl += 1
    print(f"Bei {loops} Münzwürfen fiel {kopf} mal Kopf und {zahl} mal Zahl." )

multiFlipcoin(100)

# Alternative unter Verwendung der flipcoin1- Funktion
def multiFlipcoin1(loops):
    kopf = 0
    zahl = 0
    for n in range(loops):
        if flipcoin1() == "Kopf":
            kopf += 1
        else:
            zahl += 1
    print(f"Bei {loops} Münzwürfen fiel {kopf} mal Kopf und {zahl} mal Zahl." )

multiFlipcoin1(100)

# Aufgabe 3: Schreibe eine Funktion, die zwei Punkte als Dictionary übernimmt, welche
#            Koordinaten für eine Gerade in einem Koordinatensystem darstellen.
#            Also z.B. {"x1": 0, "y1": 1, "x2": 1 , "y2": 2}
#            Berechne hieraus den Y- Achsenabschnitt und die Formel der linearen Funktion.
#            Grundformel: f(x) = mx + n
#            m = (y2 - y1)/(x2 - x1)
#            n ist der Y- Achsenabschnitt.

print("\nAufgabe 3\n")

points = {"x1": 0, "y1": 1, "x2": 1 , "y2": 2}
points2 = {"x1": 2, "y1": 1, "x2": 1 , "y2": -7}

def linearFunktion(coord:dict):
    # m = (y2 - y1)/(x2 - x1)
    m = (coord["y2"] - coord["y1"]) / (coord["x2"] - coord["x1"])
    # Grundformel nach n umstellen
    # n = f(x) - mx
    n = coord["y1"] - m*coord["x1"]
    print(f"Die Formel der Geraden ist f(x) = {m}x + {n}. Die Y- Achse wird bei y = {n} geschnitten.")
    print(f"Die Formel der Geraden ist f(x) = {m}x {"+" if n>=0 else "-"} {abs(n)}. Die Y- Achse wird bei y = {n} geschnitten.")

linearFunktion(points2)

# Aufgabe 4: Schreibe eine Funktion, 
#            die den größten Teiler einer Zahl findet.

print("\nAufgabe 4\n")

def maxDivisor(zahl):
    mdiv = zahl//2
    if type(zahl) != int:
        print("Keine Integerzahl übergeben.")
        return 0
    else:
        while zahl % mdiv != 0:
            mdiv -= 1
        print(f"Größter Teiler ist {mdiv}.")
        return mdiv
    
maxDivisor(1_000_001)

# Aufgabe 5: Schreibe eine Funktion, die aus folgendem
#            Dictionary 'leute' das Durchschnittsalter errechnet.

print("\nAufgabe 5\n")

leute = {"Kerstin": 50, "Manfred": 65, "Lilly": 25}

def avgAge(crowd:dict):
    return round(sum(crowd.values())/len(crowd),2)

print(avgAge(leute))

# Aufgabe 6: Schreibe eine Funktion, die aus dem Dictionary 'leute'
#            die älteste errechnet.

print("\nAufgabe 6\n")

def oldest(crowd:dict):
    maxKey = ""
    maxVal = 0
    for k,v in crowd.items():
        if v > maxVal:
            maxKey = k
            maxVal = v
    print(f"Die älteste Person ist {maxKey}.")

oldest(leute)

# Aufgabe 7: Schreibe die Funktion aus Aufgabe 5 so um,
#            dass sie mehrere Personen ausgeben kann, die
#            alle das höchste Alter haben, aber nur eine 
#            Person, sollte diese die älteste sein.

print("\nAufgabe 7\n")

leute2 = {"Kerstin": 50, "Manfred": 65, "Lilly": 25, "Egon" : 65, "Ida" : 55}

def oldest2(crowd:dict):
    maxKey = []
    maxVal = 0
    for k,v in crowd.items():
        if v > maxVal:
            maxKey.clear()
            maxKey.append(k)
            maxVal = v
        elif v == maxVal:
            maxKey.append(k)
    if len(maxKey) > 1:
        #print(f"{("".join(str(maxKey).split()).strip("[]")).replace("'", "")} sind die Ältesten.")
        #print(*maxKey, "sind die Ältesten.")
        print(", ".join(maxKey[0:-1]),"und",maxKey[-1], "sind die Ältesten.")
    else:            
        print(f"{maxKey} ist am ältesten.")

oldest2(leute2)

# Aufgabe 8:  Schreibe eine Funktion zur Kreisberechnung, die zwei Argumente übernimmt: 
#             einen Zahlenwert und einen String, der aussagt, ob dieser Zahlenwert als Radius, Umfang 
#             oder Fläche zu verstehen ist. Radius soll dabei als Defaultwert eingestellt sein. Die 
#             Funktion soll dann die jeweils restlichen Werte ausgeben.

print("\nAufgabe 8\n")

def kreis(val:int|float, mod:str="r")->None:    # Argument "mod" ist per default mit "r" für Radius belegt
    '''
    mod bezeichnet, welchen Wert die übergebene 
    Variable darstellt
    Radius="r"      Durchmesser="d"
    Fläche="a"      Umfang="u"
    '''
    from math import pi, sqrt   # Import der Mathebibliothek für PI und Wurzelziehen

    match mod:  # die verschiedenen Berechnungen in Abhängigkeit vom Modus
        case "r":
            d=2*val
            a=pi*val**2
            u=pi*2*val
            print(f"Durchmesser: {round(d, 2)}, Flaeche: {round(a, 2)}, Umfang: {round(u, 2)}")
        case "d":
            r=val/2
            a=(pi*val**2)/4
            u=pi*val
            print(f"Radius: {round(r, 2)}, Flaeche: {round(a, 2)}, Umfang: {round(u, 2)}")
        case "a":
            r=sqrt(val/pi)
            d=2*r
            u=pi*2*r
            print(f"Radius: {round(r, 2)}, Durchmesser: {round(d, 2)}, Umfang: {round(u, 2)}")
        case "u":
            r=val/(2*pi)
            d=2*r
            a=pi*r**2
            print(f"Radius: {round(r, 2)}, Durchmesser: {round(d, 2)}, Flaeche: {round(a, 2)}")

kreis(10)       # Aufruf der Funktion mit nur einem Argument (default=Radius)
kreis(20, "a")  # Aufruf mit zwei Argumenten, erster Wert gilt als Fläche

def kreis1(val:int|float, mod:str="r")->None:    # Argument "mod" ist per default mit "r" für Radius belegt
    '''
    mod bezeichnet, welchen Wert die übergebene 
    Variable darstellt
    Radius="r"      Durchmesser="d"
    Fläche="a"      Umfang="u"
    '''
    from math import pi, sqrt   # Import der Mathebibliothek für PI und Wurzelziehen

    radius = 0

    match mod:  # die verschiedenen Berechnungen in Abhängigkeit vom Modus
        case "r":
            radius = val
        case "d":
            radius = val/2
        case "a":
            radius = sqrt(val/pi)
        case "u":
            radius = val/(2*pi)

    d=2*radius
    a=pi*radius**2
    u=pi*2*radius
    print(f"Radius: {round(radius, 2)}, Durchmesser: {round(d, 2)}, Flaeche: {round(a, 2)}, Umfang: {round(u, 2)}")

kreis1(10)       # Aufruf der Funktion mit nur einem Argument (default=Radius)
kreis1(20, "a")  # Aufruf mit zwei Argumenten, erster Wert gilt als Fläche


# Aufgabe 9:  Schreibe einen Passwortgenerator, der als Argument die Länge des Passwortes übernimmt
#             und dieses zurück gibt.

print("\nAufgabe 9\n")

#   Einfacher Passwortgenerator unter Verwendung der Module 'random' und 'string'
def pwgenSimple(pwLength:int)->str:
    """
    @param pwLength: Integerzahl für die Anzahl der auszugebenen Zeichen
    @return: Zufällige Zeichenkette
    """
    # hexdigits enthält nur die Zeichen, die bei einer 
    # Hexadezimal- Codierung verwendet werden.
    # Eigentlich aber bräuchten wir alle Groß- und Kleinbuchstaben.
    from string import hexdigits, punctuation
    from random import sample 
    pwPool=hexdigits + punctuation
    # print(pwPool)     # nur einkommentieren, um den Zeichenpool zu sehen
    return "".join(sample(pwPool, pwLength))    # Sampleliste wird in einen leeren String gejoint

print(pwgenSimple(20))

# Aufgabe 10:  Schreiben einen weiteren Passwortgenerator, der als Argumente die Anzahl der Zeichen
#             aus dem Bereich der Kleinbuchstaben, der Großbuchstaben, der Zahlen und der Sonderzeichen
#             übernimmt und ein entsprechendes Passwort zurück gibt.

print("\nAufgabe 10\n")

def pwgenPro1(lows:int, caps:int, nums:int, specs:int=0)->str:  
    # siehe ab Zeile 125, sinngemäß gleich, nur hier unter Verwendung des String- Moduls
    from random import sample, shuffle
    from string import ascii_lowercase, ascii_uppercase, digits, punctuation
    lowLetters=sample(ascii_lowercase, lows)
    capLetters=sample(ascii_uppercase, caps)
    numbers=sample(digits, nums)
    specChar=sample(punctuation, specs)
    pw=[]
    pw.extend(lowLetters+capLetters+numbers+specChar)
    shuffle(pw)
    return "".join(pw)

print(pwgenPro1(2,3,4,4))

def pwgenPro2(lows:int, caps:int, nums:int, specs:int=0)->str:
    from random import sample, shuffle
    lowLetters=sample(range(97, 123), lows) # range(97, 123): Kleinbuchstaben im Ascii-Code
    capLetters=sample(range(65, 91), caps)  # range(65, 91): Großbuchstaben im Ascii-Code
    numbers=sample(range(48, 58), nums)     # range(48, 58): Zahlen im Ascii-Code
    specChar=sample(range(35, 39), specs)   # range(35, 39): Einige Soderzeichen im Ascii-Code
    pw=[]                                   # leere Liste angelegt
    pw.extend(lowLetters+capLetters+numbers+specChar)   # und erweitert um die Einzellisten
    pw=[chr(num) for num in pw] # Umwandlung der numerischen Ascii- Entsprechung in Zeichen
    shuffle(pw)                 # Durchmischen
    return "".join(pw)          # und in einen leeren String joinen

print(pwgenPro2(2,3,4,4))