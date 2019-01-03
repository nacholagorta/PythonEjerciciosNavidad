import random

print("PIEDRA, PAPEL,...¡TIJERA!")

opciones = ['PIEDRA', 'PAPEL', 'TIJERA']

juan = random.choice(opciones)
ines = random.choice(opciones)

print("Inés ha sacado ", ines, ".")
print("Juan ha sacado ", juan, ".")

if juan == 'PIEDRA' and ines == 'PAPEL':
    print("Ha ganado Inés.")
elif juan == 'PIEDRA' and ines == 'TIJERA':
    print("Ha ganado Juan.")
elif juan == 'PIEDRA' and ines == 'PIEDRA':
    print("Han empatado.")
elif juan == 'PAPEL' and ines == 'PIEDRA':
    print("Ha ganado Juan.")
elif juan == 'PAPEL' and ines == 'PAPEL':
    print("Han empatado.")
elif juan == 'PAPEL' and ines == 'TIJERA':
    print("Ha ganado Inés.")
elif juan == 'TIJERA' and ines == 'PIEDRA':
    print("Ha ganado Inés.")
elif juan == 'TIJERA' and ines == 'PAPEL':
    print("Ha ganado Juan.")
elif juan == 'TIJERA' and ines == 'TIJERA':
    print("Han empatado.")