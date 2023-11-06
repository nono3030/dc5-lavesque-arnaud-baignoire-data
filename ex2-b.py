
liste_nombres = [1, 5, 3, 8, 2, 7, 10, 4, 6, 9]

maximum = liste_nombres[0]
minimum = liste_nombres[0]

for nombre in liste_nombres:
    if nombre > maximum:
        maximum = nombre
    if nombre < minimum:
        minimum = nombre

somme = 0
for nombre in liste_nombres:
    somme += nombre

moyenne = somme / len(liste_nombres)

print("Maximum :", maximum)
print("Minimum :", minimum)
print("Moyenne :", moyenne)
