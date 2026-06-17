# EXERCICE 3
# Couleur du feu

text = ("Quelle est la couleur du feu ?")
couleur = input(text)
if couleur == "vert":
    print("Tu peux passer")
elif couleur == "orange":
    print("Ralentis")
elif couleur == "rouge":
    print("Arrête-toi")
else : 
    print("Couleur inconnue")
