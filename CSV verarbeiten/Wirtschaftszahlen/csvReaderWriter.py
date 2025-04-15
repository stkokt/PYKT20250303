

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

import csv
# Implementierung ohne Delimiter (welches Zeichen trennt die Datenfelder)
with open("Erwerbstaetige1.csv", mode='r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    dataErwerb = list(csv_reader)

headerErwerb = dataErwerb.pop(0)
#print(dataErwerb)

splittedDataset = []

for dataset in dataErwerb:
    splittedDataset.append(dataset[0].split(";"))

#print(splittedDataset)

anteil_LFF = []

for dataset in splittedDataset:
    anteil_LFF.append([dataset[0],round((float(dataset[2])/float(dataset[1])),2)])

print(anteil_LFF)

# Einlesen einer CSV-Datei mit csv.reader
with open("Erwerbstaetige1.csv", mode='r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=";")
    dataErwerb = list(csv_reader)

headerErwerb = dataErwerb.pop(0)

#print(dataErwerb)
#print(headerErwerb)
ratioLandForstFisch = [[ds[0],round(float(ds[2])/float(ds[1]),2)] for ds in dataErwerb]
#print(ratioLandForstFisch)
ratioDienstleister = [[ds[0],round(float(ds[5])/float(ds[1]),2)] for ds in dataErwerb]
#print(ratioDienstleister)

import csv
with open("Konsumentwicklung.csv", mode='r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=";")
    dataKonsum = list(csv_reader)

headerKonsum = dataKonsum.pop(0)
#print(dataKonsum)


#print(headerKonsum)
# 1 047, ' 350'
ratioLebensmittel = [[ds[0],round(float(ds[2].replace(" ","").replace(",","."))/float(ds[1].replace(" ","").replace(",",".")),2)] for ds in dataKonsum]
#print(ratioLebensmittel)
ratioWohnen = [[ds[0],round(float(ds[4].replace(" ","").replace(",","."))/float(ds[1].replace(" ","").replace(",",".")),2)] for ds in dataKonsum]
#print(ratioWohnen)


with open("Lohnentwicklung.csv", mode='r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=";")
    dataLohn = list(csv_reader)

headerLohn = dataLohn.pop(0)
#print(headerLohn)
#print(dataLohn)

ratioNettoBrutto = [[ds[0],round(float(ds[4].replace(" ","").replace(",","."))/float(ds[3].replace(" ","").replace(",",".")),2)] for ds in dataLohn]
#print(ratioNettoBrutto)

header_ratios = ["Jahr","ratioLandForstFisch", "ratioDienstleister", "ratioLebensmittel", 
                 "ratioWohnen", "ratioNettoBrutto"]
jahre = [ds[0] for ds in ratioWohnen]
wr1 = [ds[1] for ds in ratioLandForstFisch]
wr2 = [ds[1] for ds in ratioDienstleister]
wr3 = [ds[1] for ds in ratioLebensmittel]
wr4 = [ds[1] for ds in ratioWohnen]
wr5 = [ds[1] for ds in ratioNettoBrutto]

ratios = list(zip(jahre, wr1, wr2, wr3, wr4, wr5))

print(ratios)

#print("Ratios",wirtschaft_ratio)
# Schreiben über csv.writer

with open('output_ratios.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file, delimiter=";")
    csv_writer.writerow(header_ratios)
    csv_writer.writerows(ratios)
