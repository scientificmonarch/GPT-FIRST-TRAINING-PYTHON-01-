# Tarification d'un parc

âge = int(input("Quel âge as-tu ?"))
if âge <= 12:
    print("Tarif enfant")
elif âge <= 17:
    print("Tarif adolescent")
elif âge <= 59:
    print("Tarif adulte")
else:
    print("Tarif senior")
    
