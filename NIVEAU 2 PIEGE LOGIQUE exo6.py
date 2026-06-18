#EXERCIE 6
# Validation d'inscription

age = int(input("Age :"))
if age <= 0:
    print("Erreur de saisie")
elif age > 120:
    print("Erreur de saisie")
elif age < 18:
    print("Mineur")
else : 
    print("Majeur")
