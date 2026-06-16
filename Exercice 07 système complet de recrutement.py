# Système complet de recrutement
age = int(input("Age :"))
experience = int(input("Experience :"))

if age < 18:
    print("Refusé")
elif experience < 2:
    print("Junior")
elif experience <= 5:
    print("Confirmé")
else :
    print("Sénior")

 
