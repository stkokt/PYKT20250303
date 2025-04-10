import csv

# Einlesen einer CSV-Datei mit csv.reader
with open("C:/Users/StefanKoschnik/OneDrive - karriere tutor GmbH/Dokumente/Python/PYKT20250303/PYKT20250303/Wirtschaftszahlen - Kopie", mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    data = list(csv_reader)

print(data)

# Schreiben einer CSV-Datei mit csv.writer
with open('output.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

# Einlesen einer CSV-Datei mit csv.DictReader
with open('input.csv', mode='r', newline='') as file:
    csv_dict_reader = csv.DictReader(file)
    data = list(csv_dict_reader)

# Schreiben einer CSV-Datei mit csv.DictWriter
with open('output.csv', mode='w', newline='') as file:
    fieldnames = data[0].keys()  # Annahme: Alle Zeilen haben die gleichen Felder
    csv_dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_dict_writer.writeheader()
    csv_dict_writer.writerows(data)

