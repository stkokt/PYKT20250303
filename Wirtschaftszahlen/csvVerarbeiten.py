import csv

# Lese diese Dateien ein
# - Erwerbstaetige1
# - Konsumentwicklung
# - Lohnentwicklung

# Bilde diese Ratios:
# Anteil der Land-, Forst- und Fischereiarbeiter sowie der Dienstleister an den Gesamtbeschäftigten.
# Anteil der Wohn- sowie der Lebenserhaltungskosten (Nahrung/Genuss) am Gesamtkonsum.
# Verhältnis von Netto- zu Bruttolöhnen. 
# 
# Recherchiere, wie du diese Ratios in eine CSV- Datei zurückschreiben kannst. 

# Einlesen einer CSV-Datei mit csv.reader
with open("Erwerbstaetige1.csv", mode='r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=";")
    dataErwerb = list(csv_reader)

headerErwerb = dataErwerb.pop(0)

#print(dataErwerb)
# print(header)
ratioLandForstFisch = [[ds[0],round(float(ds[2])/float(ds[1]),2)] for ds in dataErwerb]
#print(ratioLandForstFisch)
ratioDienstleister = [[ds[0],round(float(ds[5])/float(ds[1]),2)] for ds in dataErwerb]
#print(ratioDienstleister)

with open("Konsumentwicklung.csv", mode='r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=";")
    dataKonsum = list(csv_reader)

headerKonsum = dataKonsum.pop(0)
# 1 047, ' 350'
ratioLebensmittel = [[ds[0],round(float(ds[2].replace(" ","").replace(",","."))/float(ds[1].replace(" ","").replace(",",".")),2)] for ds in dataKonsum]
#print(ratioLebensmittel)
ratioWohnen = [[ds[0],round(float(ds[4].replace(" ","").replace(",","."))/float(ds[1].replace(" ","").replace(",",".")),2)] for ds in dataKonsum]
#print(ratioWohnen)

# ratioLebensmittel = [[ds[0],round(float(ds[2].strip(" ").replace(",","."))/float(ds[1].strip(" ").replace(",",".")),2)] for ds in dataKonsum]
# print(ratioLebensmittel)
# ratioWohnen = [[ds[0],round(float(ds[4].strip(" ").replace(",","."))/float(ds[1].strip(" ").replace(",",".")),2)] for ds in dataKonsum]
# print(ratioWohnen)

with open("Lohnentwicklung.csv", mode='r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=";")
    dataLohn = list(csv_reader)

headerLohn = dataLohn.pop(0)

#print(dataLohn)

ratioNettoBrutto = [[ds[0],round(float(ds[4].replace(" ","").replace(",","."))/float(ds[3].replace(" ","").replace(",",".")),2)] for ds in dataLohn]
#print(ratioNettoBrutto)

# Implementierung ohne Delimiter (welches Zeichen trennt die Datenfelder)
with open("Erwerbstaetige1.csv", mode='r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    dataErwerb = list(csv_reader)

headerErwerb = dataErwerb.pop(0)

splittedDataset = []

for dataset in dataErwerb:
    splittedDataset.append(dataset[0].split(";"))

#print(splittedDataset)

anteil_LFF = []

for dataset in splittedDataset:
    anteil_LFF.append([dataset[0],round((float(dataset[2])/float(dataset[1])),2)])

print(anteil_LFF)


# Schreiben über csv.writer

# with open('output_csvWriter.csv', mode='w', newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(ratioLandForstFisch)

# Einlesen einer CSV-Datei mit csv.DictReader
# with open('Erwerbstaetige1.csv', mode='r', newline='') as file:
#     csv_dict_reader = csv.DictReader(file, delimiter=";")
#     data = list(csv_dict_reader)

# print(data)

# Schreiben über DictWriter

# with open('output.csv', mode='w', newline='') as file:
#     fieldnames = data[0].keys()  # Annahme: Alle Zeilen haben die gleichen Felder
#     csv_dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
#     csv_dict_writer.writeheader()
#     csv_dict_writer.writerows(data)



