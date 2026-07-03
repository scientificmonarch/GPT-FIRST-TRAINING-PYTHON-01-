courses = []

choix = [1, 2, 3, 4, 5]
print("===== GESTIONNAIRE DE COURSES =====")
print("1-Afficher la liste")
print("2-Ajouter un produit")
print("3-Supprimer un produit")
print("4-Tirer la liste")
print("5-Quitter")

choix = int(input("Choisissez une option (1-5) : ")) 
if choix == 1:
    print(courses)
elif choix == 2:
    print("Entrez le produit : ")
elif choix == 3:
    print("Entrez le produit : ")
elif choix == 4:
    courses.sort()
else : 
    print("Quittez")
    