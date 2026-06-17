# EXERCICE 6 
# NIVEAU DE JOUEUR

TEXT = ("quel est votre niveau ?")
niveau = int(input(TEXT))
if niveau < 10:
    print("Débutant")
elif niveau <= 30:
    print("Intermédiaire")
elif niveau <= 70:
    print("Avancé")
else:
    print("Expert")
    