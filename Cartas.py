from random import randint

print("JUEGO DEL QUINCE")

gCarta1 = randint(1, 10)
gCarta2 = randint(1, 10)
gCarta3 = randint(1, 10)

hCarta1 = randint(1, 10)
hCarta2 = randint(1, 10)
hCarta3 = randint(1, 10)

print("Gloria ha sacado un ", gCarta1, ", un ", gCarta2, " y un ", gCarta3, ".")
print("Héctor ha sacado un ", hCarta1, ", un ", hCarta2, " y un ", hCarta3, ".")

gloriaTotal = gCarta1 + gCarta2 + gCarta3
hectorTotal = hCarta1 + hCarta2 + hCarta3

if hectorTotal < gloriaTotal <= 15:
    print("Ha ganado Gloria.")
if gloriaTotal < hectorTotal <= 15:
    print("Ha ganado Héctor.")
if gloriaTotal == hectorTotal and gloriaTotal <= 15:
    print("Han empatado.")
if gloriaTotal > 15 and hectorTotal > 15:
    print("No ha ganado nadie.")
if gloriaTotal > 15 and hectorTotal <=15:
    print("Ha ganado Héctor.")
if hectorTotal > 15 and gloriaTotal <= 15:
    print("Ha gandado Gloria.")
