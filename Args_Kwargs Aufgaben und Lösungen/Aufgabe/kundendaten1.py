kundendaten = [
    {"vorname": "Rome",     "nachname": "Turner",  "bundesland": "Bayern"},
    {"vorname": "Brooklyn", "nachname": "English", "bundesland": "NRW"},
    {"vorname": "Junior",   "nachname": "Novak",   "bundesland": "Berlin"},
    {"vorname": "Kaiya",    "nachname": "Bullock", "bundesland": "Sachsen"},
    {"vorname": "Kaisley",  "nachname": "Cherry",  "bundesland": "NRW"}
]

def kundeninfo(kundendaten):
    for kunde in kundendaten:
        print(f"Vorname: {kunde["vorname"]:<10} Nachname: {kunde["nachname"]:<10} Bundesland: {kunde["bundesland"]:<10}")

# ----------------------------------------------------------------------------------------

print("-----------------------")
print("Kundendaten unsortiert:")
kundeninfo(kundendaten)


# Aufgabe: Sortiere die Kundendaten nach Bundesländer
print("-----------------------")
print("Kundendaten sortiert nach Bundesländer:")
# Lösung: Anfang
...
kundeninfo(sorted(kundendaten, key=...))
# Lösung: Ende


# Aufgabe: Sortiere die Kundendaten nach Vornamen
print("-----------------------")
print("Kundendaten sortiert nach Vornamen:")
# Lösung: Anfang
...
kundeninfo(sorted(kundendaten, ...))
# Lösung: Ende


# Aufgabe: Sortiere die Kundendaten nach Nachnamen
print("-----------------------")
print("Kundendaten sortiert nach Nachnamen:")
# Lösung: Anfang
...
kundeninfo(sorted(kundendaten, ...))
# Lösung: Ende
