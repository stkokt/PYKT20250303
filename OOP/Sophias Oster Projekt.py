# OSTEREIERSUCHE

# Aufgabe:
# Es ist Ostern. Der Osterhase malt Eier an und versteckt sie im Garten. 
# Zwei Kinder suchen die Eier und sammeln sie in ihre Körbe ein.

# Funktionalität:
# Verstecken per Zufallsgenerator. Suchen durch gezielte Abfragen. 
# Zwei-Spieler-Modus: Wer nach 7 Zügen (jeweils) die meisten Eier gesammelt hat, hat die Ostereier-Suche gewonnen.
# Der Garten wird durch ein zweidimensionales Raster dargestellt.

# ---------- Instanziierung ------------
# Garten instanziieren
# Hase instanziieren
# Eier instanziieren
# Kinder instanziieren

# ---------- Prozeduraler Code ----------
# Eier-Methodenaufruf: Hase versteckt Eier
# Spielstart: Eiersuche
    # Kind-Methodenaufruf: Eier suchen
    # Ergebnis: Ei gefunden oder nicht
    # Ausgabe: Du hast bis jetzt X Eier im Korb, es sind noch X Eier versteckt.
# Spielende: alle Eier gefunden ODER Ende nach 7 Zügen jeweils
    # Ausgabe: Gewinner, wieviele Eier im Körbchen, wieviel Züge benötigt

import random
import os

class Garten():
    def __init__(self, breite, laenge):
        self.x = breite  # Breite des Gartens
        self.y = laenge  # Länge des Gartens
        self.garten = []  # Hauptliste für alle Zeilen

        # Matrix erstellen
        for y in range(1, laenge + 1):  # Zeilen
            zeile = []  # Liste für eine Zeile
            for x in range(breite):  # Spalten
                buchstabe = chr(65 + x)  # 'A', 'B', ...
                feld = f"{buchstabe}{y}"
                zeile.append(feld)  # Feld zur Zeile hinzufügen
            self.garten.append(zeile)  # Zeile zur Hauptliste hinzufügen

    def anzeigen(self): # Methode, um den Garten auf der Konsole auszugeben
        for zeile in self.garten:
            print(" ".join(zeile))
        
    def anzeigen_aktualisiert(self, gefundene_felder, leere_felder):
        for zeile in self.garten:
            zeile_ausgabe = []
            for feld in zeile:
                if feld in gefundene_felder:
                    zeile_ausgabe.append("🥚")  # Ei gefunden
                elif feld in leere_felder:
                    zeile_ausgabe.append("-")  # kein Ei
                else:
                    zeile_ausgabe.append(feld)  # noch nicht besucht
            print(" ".join(zeile_ausgabe))
        
class Osterhase():
    def __init__(self, name):
        self.name = name

class Osterei():
    instanzen = []

    def __init__(self, anzahl, farbe):
        self.anzahl = anzahl
        self.farbe = farbe
        self.eier = [f"{farbe}es Ei" for _ in range(anzahl)]  # Lokale Liste
        Osterei.instanzen.append(self)  # Liste aller Instanzen

    def Eier_verstecken(self, garten: Garten, versteck_dict):
        alle_felder = [feld for zeile in garten.garten for feld in zeile]
        freie_felder = list(set(alle_felder) - set(versteck_dict.keys())) # falls schon Felder belegt sind
        verstecke = random.sample(freie_felder, self.anzahl)

        for feld, ei in zip(verstecke, self.eier):
            versteck_dict[feld] = ei
            print(f"\nEin {ei} wurde versteckt.")
   
class Kind():
    def __init__(self, name):
        self.name = name
        self.koerbchen = []
        self.versuche = 7
        self.besuchte_felder = []
        self.gefundene_felder = []
        self.leere_felder = []

    def Eier_suchen(self):
        laufe = True
        while laufe:
            print(f"\nDu bist dran, {self.name}. Dies ist der aktuelle Gartenstand:")
            mein_garten.anzeigen_aktualisiert(self.gefundene_felder, self.leere_felder)
            print(f"\nWo möchtest du suchen (z.B. A1)? Du hast (noch) {self.versuche} Versuch(e).")
            feld = input()          

            # Ist das Feld überhaupt im Garten?
            alle_felder = [feld for zeile in mein_garten.garten for feld in zeile]
            if feld not in alle_felder:
                print(f"{feld} liegt außerhalb des Gartens! Versuch es nochmal.")
                laufe = True
            elif feld in self.besuchte_felder:
                print("Hier hast du schon mal gesucht – such bitte woanders.")
                laufe = True
            else:
                laufe = False  # Eingabe ist gültig

        # Nach erfolgreicher Eingabe
        self.besuchte_felder.append(feld)

        if feld in eier_versteckt_dict:
            gefundenes_ei = eier_versteckt_dict.pop(feld)
            self.koerbchen.append(gefundenes_ei)
            self.gefundene_felder.append(feld)
            print(f"Du hast ein {gefundenes_ei} gefunden, {self.name}!")
            print(f"Du hast jetzt folgende Eier im Körbchen: {self.koerbchen}")
        else:
            print("Schade! Kein Ei hier.")
            self.leere_felder.append(feld)

        self.versuche -= 1

def naechster_spieler(name_des_naechsten):
    input(f"\nJetzt ist {name_des_naechsten} dran. Bitte drücke ENTER, um abzugeben.")
    bildschirm_aufräumen()

def bildschirm_aufräumen():
    os.system('cls' if os.name == 'nt' else 'clear')   

     
# TEST

# # Garten instanziieren:
# mein_garten = Garten(6, 6)  # Garten mit 6 Spalten und 6 Zeilen
# mein_garten.anzeigen()  # Gibt den Garten aus          

# # Beispiel-Zugriffe
# # print("\nEintrag in dritter Zeile, vierte Spalte:", mein_garten.garten[2][3])  # D3
# # wert = mein_garten.garten[1][2]  # Wert in der 2. Zeile, 3. Spalte
# # print(wert)  # Gibt "C2" aus

# # Hasen instanziieren:
# mein_Hase = Osterhase("Rüdiger")
# print(f"Der Osterhase heißt {mein_Hase.name}.")

# # Eier instanziieren:
# gelbe_Eier = Osterei(4, "gelb")
# print(f"Der Osterhase hat {gelbe_Eier.anzahl} Eier {gelbe_Eier.farbe} angemalt.")
# rote_Eier = Osterei(4, "rot")
# print(f"Der Osterhase hat {rote_Eier.anzahl} Eier {rote_Eier.farbe} angemalt.")
# gruene_Eier = Osterei(4, "grün")
# print(f"Der Osterhase hat {gruene_Eier.anzahl} Eier {gruene_Eier.farbe} angemalt.")
# blaue_Eier = Osterei(4, "blau")
# print(f"Der Osterhase hat {blaue_Eier.anzahl} Eier {blaue_Eier.farbe} angemalt.")

# # alle bemalten Eier anzeigen:
# alle_bemalten_eier = []
# for ei in Osterei.instanzen:
#     alle_bemalten_eier.extend(ei.eier)
# print("Alle bemalten Eier:")
# print(alle_bemalten_eier)
# print(f"Anzahl bemalter Eier: {len(alle_bemalten_eier)}")

# # Kinder instanziieren
# Kind_1 = Kind("Marie")
# Kind_2 = Kind("Paul")

# # Versteck-Dictionary für alle Eier, wird beim Aufruf befüllt
# eier_versteckt_dict = {}

# # Eier verstecken
# gelbe_Eier.Eier_verstecken(mein_garten, eier_versteckt_dict)
# rote_Eier.Eier_verstecken(mein_garten, eier_versteckt_dict)
# gruene_Eier.Eier_verstecken(mein_garten, eier_versteckt_dict)
# blaue_Eier.Eier_verstecken(mein_garten, eier_versteckt_dict)

# # versteckte Eier anzeigen
# print(eier_versteckt_dict)

# # Eier suchen
# Kind_1.Eier_suchen()
# Kind_2.Eier_suchen()


### ----- Programmablauf -----

# Begrüßung
print ("\nHerzlich Willkommen zur Ostereiersuche!")
print ("\nEs treten zwei Kinder gegeneinander an. Wer zuerst alle Ostereier gefunden hat, hat gewonnen.")
print ("Jedes Kind hat maximal 7 Versuche.")

# Kinder
print ("\nKind 1, bitte gib deinen Namen ein: ")
name = input ()
Kind_1 = Kind(name)

print ("\nKind 2, bitte gib deinen Namen ein: ")
name = input ()
Kind_2 = Kind(name)

# Garten
print ("\nWie groß soll der Garten sein, in dem der Osterhase seine Eier versteckt?")
print ("Bitte gib eine Breite (max. 7) und eine Länge (max. 7) an!")
print ("Breite: ")
breite = int(input())
print ("Länge: ")
laenge = int(input())
mein_garten = Garten(breite, laenge)
print ("\nDu hast folgenden Garten erstellt.")
mein_garten.anzeigen()

# Hase
print (f"\nWie soll der Osterhase heißen? Bitte gib einen Namen ein: ")
name_hase = input()
mein_Hase = Osterhase(name_hase)

# Eier anmalen
print(f"\nDer Osterhase {mein_Hase.name} wird jetzt die Eier entweder gelb, rot, grün oder blau anmalen und verstecken.")
print (f"Wie viele Eier soll er gelb anmalen?")
anzahl_gelb = int(input ())
gelbe_Eier = Osterei(anzahl_gelb, "gelb")
print(f"Der Osterhase hat {gelbe_Eier.anzahl} Eier {gelbe_Eier.farbe} angemalt.")

print (f"\nWie viele Eier soll er rot anmalen?")
anzahl_rot = int(input ())
rote_Eier = Osterei(anzahl_rot, "rot")
print(f"Der Osterhase hat {rote_Eier.anzahl} Eier {rote_Eier.farbe} angemalt.")

print (f"\nWie viele Eier soll er grün anmalen?")
anzahl_gruen = int(input ())
gruene_Eier = Osterei(anzahl_gruen, "grün")
print(f"Der Osterhase hat {gruene_Eier.anzahl} Eier {gruene_Eier.farbe} angemalt.")

print (f"\nWie viele Eier soll er blau anmalen?")
anzahl_blau = int(input ())
blaue_Eier = Osterei(anzahl_blau, "blau")
print(f"Der Osterhase hat {blaue_Eier.anzahl} Eier {blaue_Eier.farbe} angemalt.")

# alle bemalten Eier anzeigen:
alle_bemalten_eier = []
for ei in Osterei.instanzen:
    alle_bemalten_eier.extend(ei.eier)
print(f"\nInsgesamt sind es jetzt {len(alle_bemalten_eier)} Eier, die {mein_Hase.name} versteckt. Es geht los!")

# Versteck-Dictionary für alle Eier, wird beim Aufruf befüllt
eier_versteckt_dict = {}

# Eier verstecken
print(f"\nBitte drücke ENTER, damit {mein_Hase.name} die Eier versteckt!")
start = input()
gelbe_Eier.Eier_verstecken(mein_garten, eier_versteckt_dict)
rote_Eier.Eier_verstecken(mein_garten, eier_versteckt_dict)
gruene_Eier.Eier_verstecken(mein_garten, eier_versteckt_dict)
blaue_Eier.Eier_verstecken(mein_garten, eier_versteckt_dict)

# Eier suchen
for _ in range(7):  # 7 Versuche je Kind
    Kind_1.Eier_suchen()
    naechster_spieler(Kind_2.name)

    Kind_2.Eier_suchen()
    naechster_spieler(Kind_1.name)

# --- Spielstand-Ausgabe nach Ende ---

print("\n--- Spielende ---")

def ausgabe_ergebnis(kind):
    print(f"\n{kind.name}:")
    print(f"- Eier im Körbchen: {len(kind.koerbchen)}")
    print(f"- Gesammelte Eier: {kind.koerbchen}")
    print(f"- Versuche: {7 - kind.versuche}")

ausgabe_ergebnis(Kind_1)
ausgabe_ergebnis(Kind_2)

# Gewinner bestimmen
if len(Kind_1.koerbchen) > len(Kind_2.koerbchen):
    print(f"\n{Kind_1.name} hat gewonnen! Herzlichen Glückwunsch!")
elif len(Kind_1.koerbchen) < len(Kind_2.koerbchen):
    print(f"\n{Kind_2.name} hat gewonnen! Herzlichen Glückwunsch!")
else:
    print("\nEs ist unentschieden – ihr seid beide echte Ostereier-Profis!")
