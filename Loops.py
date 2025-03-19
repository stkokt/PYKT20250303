# DAS WICHTIGSTE BEI LOOPS IST DIE ABBRUCHBEDINGUNG!!!

# Der For- Loop (range- based Loop)

liste = [1,2,3,4,5]
# for n in liste:
#     print(n)

for n in range(len(liste)):
    #print(n)
    print(liste[n])

string = "Stefan"
for letter in string:
    print(letter)

summe = 0
for n in liste:
    summe += n
print(summe)
print(sum(liste)) # Besser!

# Der range- Parameter im For- Loop

# Range: (start, stop(bevor), step)

for n in range(10): # n fängt an bei 0 und endet bei 9
    if n % 2 == 0:
        print("Hallo")
    print("Welt")
print("Und Schluss")

for n in range(2,10):
    print(n)

for n in range(2,11,3):
    print(n)

for n in range(10, -1, -2):
    print(n)

# Der While Loop

it = 0
while it < 10:
    print("Hallo", "Iterator: ", it)
    it += 1

it1 = 1
while it1:
    print("Hallo", "Iterator: ", it1)
    it1 += 1
    if it1 == 10:
        break

# it3 = 0
# while it3:
#     it3 += 1
#     if it3 % 2 == 0:
#         continue
#     print("Hallo", "Iterator: ", it3)
#     if it3 == 10:
#         break

for n in range(11):
    if n%2==0:
        continue
    else:
        print(n)

it2 = 10
while it2:
    print("Hallo", "Iterator: ", it2)
    it2 -= 1
