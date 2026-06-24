# EXERCICE 5
# ELIGIBILITE A UN PRET 

eligibilite = int(input("quel est votre revenu mensuel ?"))
if eligibilite < 100000:
    print("Prêt refusé")
elif eligibilite > 300000:
    print("Prêt approuvé")
else : 
    print("Prêt en étude")
