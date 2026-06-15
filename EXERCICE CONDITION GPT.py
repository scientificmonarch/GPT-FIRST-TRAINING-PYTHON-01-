# Accès au cinéma

age = int(input("Entrée votre âge pour accéder au cinéma !"))
if age >=18:
    print("Accès autorisé")
else:
    print("Accès refusé")

# Température
text = ("quelle est la température ?")
temp = int(input(text))
if temp >= 30:
    print("il fait chaud !")
else:
    print("il ne fait pas chaud !")

# Note scolaire
note = float(input("Quelle est ta note ?"))
if note >= 10:
    print("Admis")
else:
    print("Ajourné")

#Contrôle de vitesse
text = ("Quelle est votre vitesse")
vitesse = int(input(text))
if vitesse > 50:
    print(("Trop rapide !"))
else:
    print("Vitesse correcte !")

# Mention scolaire
note = float(input("Quel est ta note ?"))
if note >= 16:
    print("Excellent !")
elif note>= 14:
    print("Très bien !")
elif note >=10:
    print("Passable !")
else:
    print("Insuffisant !")

# Jeu du niveau
age = int(input("Quel est votre âge ?"))
if age >18:
    print("Niveau adulte !")
elif age >= 13:
    print("Niveau scolaire !")
else:
    print("Niveau enfant")

# Entrepreneur ou débutant 
text = ("Quel est votre année d'expérience ?")
experience = int(input(text))
if experience >= 10:
    print("Expert !")
elif experience >= 5:
        print("Intermédiare")
else:  
    print("Débutant !")

# Défis bonus

age = int(input("quel est votre âge ?"))
if age >= 60:
    print("senior")
elif age >= 18:
    print("Adulte")
elif age >= 13:
    print("Adolescent")
else:
    print("Débutant")


    
