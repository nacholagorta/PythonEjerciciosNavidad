import random

print("PIEDRA, PAPEL,...¡TIJERA!")

opciones = ['PIEDRA', 'PAPEL', 'TIJERA', 'LAGARTO', 'SPOCK']

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
elif juan == 'PIEDRA' and ines == 'LAGARTO':
    print("Ha ganado Inés.")
elif juan == 'PIEDRA' and ines == 'SPOCK':
    print("Ha ganado Juan.")
elif juan == 'PAPEL' and ines == 'PIEDRA':
    print("Ha ganado Juan.")
elif juan == 'PAPEL' and ines == 'PAPEL':
    print("Han empatado.")
elif juan == 'PAPEL' and ines == 'TIJERA':
    print("Ha ganado Inés.")
elif juan == 'PAPEL' and ines == 'LAGARTO':
    print("Ha ganado Juan.")
elif juan == 'PAPEL' and ines == 'SPOCK':
    print("Ha gando Inés.")
elif juan == 'TIJERA' and ines == 'PIEDRA':
    print("Ha ganado Inés.")
elif juan == 'TIJERA' and ines == 'PAPEL':
    print("Ha ganado Juan.")
elif juan == 'TIJERA' and ines == 'TIJERA':
    print("Han empatado.")
elif juan == 'TIJERA' and ines == 'LAGARTO':
    print("Ha ganado Inés.")
elif juan == 'TIJERA' and ines == 'SPOCK':
    print("Ha ganado Juan.")
elif juan == 'LAGARTO' and ines == 'PIEDRA':
    print("Ha ganado Juan.")
elif juan == 'LAGARTO' and ines == 'PAPEL':
    print("Ha ganado Inés .")
elif juan == 'LAGARTO' and ines == 'TIJERA':
    print("Ha ganado Juan.")
elif juan == 'LAGARTO' and ines == 'LAGARTO':
    print("Han empatado.")
elif juan == 'LAGARTO' and ines == 'SPOCK':
    print("Ha ganado Inés.")
elif juan == 'SPOCK' and ines == 'PIEDRA':
    print("Ha ganado Inés.")
elif juan == 'SPOCK' and ines == 'PAPEL':
    print("Ha ganado Juan.")
elif juan == 'SPOCK' and ines == 'TIJERA':
    print("Ha ganado Inés.")
elif juan == 'SPOCK' and ines == 'LAGARTO':
    print("Ha ganado Juan.")
elif juan == 'SPOCK' and ines == 'SPOCK':
    print("Han empatado.")