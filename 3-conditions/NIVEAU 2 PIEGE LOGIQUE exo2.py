#EXERCICE 2
# categorie d'un employé

salaire = int(input("Salaire :"))
if salaire >= 1000000:
    print("Cadre supérieur")
elif salaire >= 500000:
    print("cadre")
elif salaire >= 200000:
    print("Employé")
else : 
    print("Stagiaire")


