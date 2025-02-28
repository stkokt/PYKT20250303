# Verzweigungen mit if / elif / else

### Aufgabe 1: Zahl vergleichen
# Schreibe ein Programm, das zwei Zahlen vergleicht und ausgibt, welche größer ist.

zahl1 = 10
zahl2 = 20
if zahl1 > zahl2:
    print("Zahl1 ist größer.")
else:
    print("Zahl2 ist größer.")


### Aufgabe 2: Positive oder negative Zahl
# Schreibe ein Programm, das überprüft, ob eine Zahl positiv oder negativ ist.


zahl = -5
if zahl > 0:
    print("Die Zahl ist positiv.")
else:
    print("Die Zahl ist negativ.")


### Aufgabe 3: Gerade oder ungerade Zahl
# Schreibe ein Programm, das überprüft, ob eine Zahl gerade oder ungerade ist.


zahl = 7
if zahl % 2 == 0:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")


### Aufgabe 4: Wochentag bestimmen
# Schreibe ein Programm, das den Wochentag basierend 
# auf einer Zahl (1-7) ausgibt.


tag = 3
if tag == 1:
    print("Montag")
elif tag == 2:
    print("Dienstag")
elif tag == 3:
    print("Mittwoch")
elif tag == 4:
    print("Donnerstag")
elif tag == 5:
    print("Freitag")
elif tag == 6:
    print("Samstag")
elif tag == 7:
    print("Sonntag")
else:
    print("Ungültige Eingabe")


### Aufgabe 5: Jahreszeit bestimmen
# Schreibe ein Programm, das die Jahreszeit basierend 
# auf einem Monat (als Zahl) ausgibt.
# Winter, wenn 1,2,12
# Frühling, wenn 3,4,5
# Sommer, wenn 6,7,8
# Herbst, wenn 9,10,11
# Ungültiger Monat, wenn keine dieser Zahlen

monat = 6
if monat in [12, 1, 2]:
    print("Winter")
elif monat in [3, 4, 5]:
    print("Frühling")
elif monat in [6, 7, 8]:
    print("Sommer")
elif monat in [9, 10, 11]:
    print("Herbst")
else:
    print("Ungültiger Monat")


### Aufgabe 6: Schaltjahr überprüfen
# Schreibe ein Programm, das überprüft, ob ein Jahr ein Schaltjahr ist.


jahr = 2020
if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
    print("Das Jahr ist ein Schaltjahr.")
else:
    print("Das Jahr ist kein Schaltjahr.")


### Aufgabe 7: Notendurchschnitt
# Schreibe ein Programm, das den Notendurchschnitt berechnet und 
# eine entsprechende Meldung ausgibt.
# Sehr gut: 1.0 bis 1.5
# Gut: 1.6 bis 2.5
# Befriedigend: 2.6 bis 3.5
# Ausreichend: 3.6 bis 4.0
# Mangelhaft: 4.1 bis 5.0
# Ungenügend: über 5.0

note1 = 4.5
note2 = 3.8
note3 = 5.0
durchschnitt = (note1 + note2 + note3) / 3
print(durchschnitt)
if 1 <= durchschnitt <= 1.5:
    print("Sehr gut!")
elif 1.6 <= durchschnitt <= 2.5:
    print("Gut")
elif 2.6 <= durchschnitt <= 3.5:
    print("Befriedigend")
elif 3.6 <= durchschnitt <= 4.0:
    print("Ausreichend")
elif 4.1 <= durchschnitt <= 5.0:
    print("Mangelhaft")
else:
    print("Ungenügend")


### Aufgabe 8: Gehaltsberechnung
# Schreibe ein Programm, das das Gehalt eines Mitarbeiters 
# basierend auf seiner Arbeitszeit und Stundenlohn berechnet. 
# Überstunden (mehr als 40 Stunden) werden mit dem 1,5-fachen Stundenlohn bezahlt.


stundenlohn = 20
arbeitsstunden = 45
if arbeitsstunden > 40:
    ueberstunden = arbeitsstunden - 40
    gehalt = (40 * stundenlohn) + (ueberstunden * stundenlohn * 1.5)
else:
    gehalt = arbeitsstunden * stundenlohn
print(f"Das Gehalt beträgt: {gehalt} Euro")


### Aufgabe 9: Dreiecksart bestimmen
# Schreibe ein Programm, das die Art eines Dreiecks basierend 
# auf seinen Seitenlängen bestimmt.
# Gleichseitig: Alle Seiten gleich lang.
# Gleichschenklig: Zwei Seiten sind gleich lang
# Sonst unregelmäßig

seite1 = 5
seite2 = 5
seite3 = 5
if seite1 == seite2 == seite3:
    print("Das Dreieck ist gleichseitig.")
elif seite1 == seite2 or seite1 == seite3 or seite2 == seite3:
    print("Das Dreieck ist gleichschenklig.")
else:
    print("Das Dreieck ist unregelmäßig.")


### Aufgabe 10: Rabattberechnung
# Schreibe ein Programm, das den Rabatt auf einen Einkauf 
# basierend auf dem Einkaufswert berechnet. Für Einkäufe über 100 Euro 
# gibt es 10% Rabatt, für Einkäufe über 200 Euro 20% Rabatt.


einkaufswert = 150
if einkaufswert > 200:
    rabatt = einkaufswert * 0.20
elif einkaufswert > 100:
    rabatt = einkaufswert * 0.10
else:
    rabatt = 0
print(f"Der Rabatt beträgt: {rabatt} Euro")


### Aufgabe 11: Zugangskontrolle
# Schreibe ein Programm, das den Zugang basierend auf einem 
# Passwort gewährt oder verweigert.


passwort = "geheim"
if passwort == "geheim":
    print("Zugang gewährt")
else:
    print("Zugang verweigert")


### Aufgabe 12: Währungsumrechnung
# Schreibe ein Programm, das einen Betrag in Euro in US-Dollar 
# umrechnet, wenn der Betrag größer als 50 Euro ist.
# Angenommener Wechselkurs USD = 1.10 Euro

betrag_euro = 60
if betrag_euro > 50:
    betrag_usd = betrag_euro * 1.10
    print(f"Der Betrag in US-Dollar ist: {betrag_usd} USD")
else:
    print("Der Betrag ist zu niedrig für eine Umrechnung.")


### Aufgabe 13: Geschwindigkeitsüberwachung
# Schreibe ein Programm, das die Geschwindigkeit eines Fahrzeugs 
# überprüft und eine Strafe verhängt, wenn die Geschwindigkeit über dem Limit liegt.
# Die Strafe soll die Differenz von tatsächlicher und erlaubter Geschwindigkeit sein
# multipliziert mit 10.

geschwindigkeit = 60
limit = 50
if geschwindigkeit > limit:
    strafe = (geschwindigkeit - limit) * 10
    print(f"Sie haben das Tempolimit überschritten. Die Strafe beträgt: {strafe} Euro")
else:
    print("Sie fahren innerhalb des Tempolimits.")


### Aufgabe 14: Benotungssystem
# Schreibe ein Programm, das eine Punktzahl in eine Note umwandelt.
# Note 1 ab 90, Note 2 ab 80, Note 3 ab 70, Note 4 ab 60, Note 5 unter 60

punkte = 85
if punkte >= 90:
    note = "1"
elif punkte >= 80:
    note = "2"
elif punkte >= 70:
    note = "3"
elif punkte >= 60:
    note = "4"
elif punkte >= 50:
    note = "5"
else:
    note = "6"
print(f"Die Note ist: {note}")


### Aufgabe 15: Altersüberprüfung
# Schreibe ein Programm, das überprüft, ob eine Person alt genug ist, 
# um wählen zu dürfen (18 Jahre oder älter).


alter = 17
if alter >= 18:
    print("Sie sind alt genug, um wählen zu dürfen.")
else:
    print("Sie sind noch nicht alt genug, um wählen zu dürfen.")

