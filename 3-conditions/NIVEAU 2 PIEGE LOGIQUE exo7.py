#EXERCICE 7
#Contrôle d'abonnement

mois = ("Nombre de mois d'abonnement :")
abonnement = int(input(mois))
if abonnement == 0:
    print("Aucun abonnement")
elif abonnement < 0:
    print("valeur invalide")
elif abonnement >= 24:
    print("Client VIP")
elif abonnement >= 12:
    print("Cleint fidèle")
else :
    print("Cllient actif")
