courses = []


while True:
    print("===== GESTIONNAIRE DE COURSES =====")
    print("1-Afficher la liste")
    print("2-Ajouter un produit")
    print("3-Supprimer un produit")
    print("4-Tirer la liste")
    print("5-Quitter")
    choix = int(input("Choisissez une option (1-5) : ")) 
    if choix == 1:
        if len(courses) == 0:
            print("La liste est vide.")
        else:
            print(courses)
    elif choix == 2:
        produit = input("Saisissez le produit à ajouter : ")
        courses.append(produit)
        print("Produit ajouté !")
    elif choix == 3:
        if len(courses) == 0:
            print("La liste est vide.")
        else:
            produit = input("Entrez le produit à supprimer : ")
            if produit in courses:
                courses.remove(produit)
                print("Produit supprimé !")
            else:
                print("Le produit", produit, "n'est pas dans la liste.")
    elif choix == 4:
        if len(courses) == 0:
            print("La liste est vide.")
        else:
            courses.sort()
            print(courses)
            print("Liste triée !")
    elif choix == 5:
        print("Quittez")
        break
    else:
        print("Choix invalide.")
