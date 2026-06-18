#EXERCICE 5
# Evaluation d'un vendeur

vente = int(input("Vente :"))
if vente >= 100:
    print("Excellent vendeur")
elif vente >= 50:
    print("Bon vendeur")
elif vente >= 10:
    print("vendeur débutant")
else :
    print("Formation nécéssaire")
