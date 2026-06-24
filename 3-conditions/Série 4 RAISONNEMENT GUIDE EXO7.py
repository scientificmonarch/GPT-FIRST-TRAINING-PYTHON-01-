# EXERCICE 7
# Contrôle d'accès entreprise

age = int(input("Age :"))
experience = int(input("Experience :"))
if age < 18:
    print("Refusé")
elif experience < 2:
    print("Junior")
elif experience > 5:
    print("Sénior")
else :
    print("Confirmé")
