# Projekt Autohaus

# Klassen: Autohaus, Auto, Kunde

# Autohaus: 
#   Attribute: garage (list:Auto), umsatz (float)
#   Methoden: verkaufen (Übernimmt als Argument ein Objekt der Klasse Kunde.
#                        Der Kunde soll alle Autos angezeigt bekommen, 
#                        für die sein Geld reicht.
#                        Das gekaufte Auto soll aus der Garage des Autohauses 
#                        in die Garage des Kunden überführt werden. 
#                        Der Umsatz des Autohauses steigt um den Wert des Autos.
#                        )

# Auto:
#   Attribute: marke (str), wert (float)

# Kunde:
#   Attribute: name (str), garage (list), konto (float)

class Auto():
    def __init__(self, marke:str, wert:float):
        self.marke = marke
        self.wert = wert

    def __repr__(self):
        return self.marke

class Kunde():
    def __init__(self, name:str, konto:float):
        self.garage = []
        self.name = name
        self.konto = konto

class Autohaus():
    def __init__(self):
        self.garage = []
        self.umsatz = float()

    def verkaufen(self,kunde:Kunde):
        imBudget = []
        print(f"Hallo {kunde.name}")
        if self.garage:
            for auto in self.garage:
                if auto.wert <= kunde.konto:
                    imBudget.append(auto)
            if imBudget:
                auswahl = ""
                print("Diese Autos kannst du dir leisten:")
                for idx,auto in enumerate(imBudget):
                    if auto.wert <= kunde.konto:
                        print(f"{idx+1} -> {auto.marke} : {auto.wert} Euro")
                auswahl = input("Welches Auto (Artikelnummer) hättest du gerne? Kauf abbrechen = x\n")
                if auswahl != "x" and auswahl.isnumeric():
                    kunde.garage.append(imBudget[int(auswahl)-1])
                    kunde.konto -= imBudget[int(auswahl)-1].wert
                    self.umsatz += imBudget[int(auswahl)-1].wert
                    print(f"In deiner Garage findest du jetzt {kunde.garage}")
                    print(f"Dein Kontostand ist nun {kunde.konto}")
                    self.garage.remove(imBudget[int(auswahl)-1])
            else: print("Leider kannst du dir keins der Autos leisten")
        else: print("Leider keine Autos im Angebot")
            
Manni = Kunde("Manni", 20000)
#print(Manni.name)
Carpoint = Autohaus()
#bmw = Auto("BMW", 15000)
Carpoint.garage.extend([Auto("BMW", 15000), Auto("Mercedes", 25000), Auto("Honda", 10000)])
print(Carpoint.garage[0].marke)
Carpoint.verkaufen(Manni)
print(f"Umsatz des Autohauses beträgt: {Carpoint.umsatz}")
print(f"In der Garage des Autohauses stehen noch: {Carpoint.garage}")


