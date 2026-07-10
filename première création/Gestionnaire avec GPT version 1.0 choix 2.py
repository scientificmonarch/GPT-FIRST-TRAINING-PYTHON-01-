courses = []

def afficher_produit(liste, titre):
    if len(courses) == 0:
        print("Aucun produit dans la liste")
    else:
        print(titre)
        for numero, element in enumerate(liste, start=1):
            print(numero, "-", element)

def rechercher_produit(liste, produit):
    if produit in liste :
        return produit

    return None





while True:
    print("===== GESTIONNAIRE DE COURSES =====")
    print("1-Afficher la liste")
    print("2-Ajouter un produit")
    print("3-Supprimer un produit")
    print("4-Tirer la liste")
    print("5-Rechercher produit")
    print("6-Quitter")
    choix = int(input("Choisissez une option (1-5) : ")) 
    if choix == 1:
        afficher_produit(courses, "===Ma liste===")

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

    elif choix == 6:
        recherche = input("Indiquez le produit : ")
        rechercher_produit(courses, recherche)
        if recherche in courses:
            print("Trouvé : ", recherche)
        else: 
            print("Produit introuvable")

    else:
        print("Choix invalide.")
