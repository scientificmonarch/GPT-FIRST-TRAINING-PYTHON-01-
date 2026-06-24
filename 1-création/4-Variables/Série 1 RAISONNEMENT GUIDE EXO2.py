# EXERCICE 2 : vérification d'âge

text = ("Quel est votre âge ?")
age = int(input(text))
if age >= 18:
    print("Adulte")
elif age < 13:
    print("Enfant")
else : 
    print("Adolescent")
