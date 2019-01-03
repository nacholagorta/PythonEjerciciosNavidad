from random import randint

print("JUEGO DE DADOS (2)")

randomDavid = randint(1, 6)
randomCarmen = randint(1, 6)

randomDavid2 = randint(1, 6)
randomCarmen2 = randint(1, 6)

print("Carmen ha sacado un ", randomCarmen, " y un ", randomCarmen2,".")
print("David ha sacado un ", randomDavid, " y un ", randomDavid2,".")

totalCarmen = randomCarmen + randomCarmen2
totalDavid = randomDavid + randomDavid2

if totalCarmen > totalDavid:
    print("Ha ganado Carmen.")
elif totalDavid > totalCarmen:
    print("Ha ganado David.")
else:
    print("Han empatado.")