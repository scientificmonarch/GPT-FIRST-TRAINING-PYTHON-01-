
import random

borne_min = 1
borne_max = 1000

names = ["clarisse", "fredo", "Albert", "jacques"]
# index:    0         1        2          3

# Générer les passes
pass_generes = []

for name in names:
    numero_aleatoire = random.randint(borne_min, borne_max)
    pass_generé = name + str(numero_aleatoire)
    pass_generes.append(pass_generé)
    print(f"{name} → {pass_generé}")

print("\nListe des passes générés :")
print(pass_generes)

soiree_pass = ["clarisse145", "fredo237", "Albert542", "jacques724"]
    # index :           0             1           2           3
print("Bienvenue à la soirée !!!")
admin = "stephane52"

# vérification de pass
while True:
    invite = input("Votre passe : ")
    if invite == admin or invite in soiree_pass:
        print("Acces autorisé !")
        break
    else:
        print("Acces refusé !")
 

