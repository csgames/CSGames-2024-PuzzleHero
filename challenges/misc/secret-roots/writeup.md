# Secret Roots

## Write-up

En connaissant la date et l'heure précise auquelle la plante a été semée, on peut récupérer un timestamp par l'epoch.
L'epoch représente en fait un seed pour la fonction randint en Python. La génération d'un entier random entre 0 et 255 représente l'ingrédient (ici le byte)
utilisé dans le mélange qui permet de faire croître la plante. L'outil utilisé pour mélanger l'eau et le byte est XOR. À chaque jour pendant 12 jours, le mélange donne un caractère unicode qui représente un caractère du flag.

Exemple en Python:

import time
import random
from random import seed

def get_bytes():
    epoch = 14743497759 # La date auquel la graine a été plantée (15 Mars 2437 à 08:02:39)
    seed(epoch)
    result = []
    for i in range(12):
        result.append(random.randint(0, 255))
    return result


water = [230, 127, 45, 58, 102, 85, 189, 237, 73, 139, 144, 236]

bytes = get_bytes() #[172, 10, 94, 110, 70, 30, 140, 161, 5, 171, 177, 184]

- XOR the elements from water and salt and print them to form the desired output
for i in range(12):
    print(chr(water[i]^bytes[i]), end="")



## Flag

`JusT K1LL !T`