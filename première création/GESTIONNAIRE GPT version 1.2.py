#ROAD MAP : GESTIONNAIRE DE COURSES VERSION 1.0
# Créer une liste
# Afficher la liste
# Ajouter un produit
# Supprimer un produit
# Trier la liste
# Quitter le programme

courses = []

choix = 0

    
    

def afficher_liste(liste, titre):
    if len(liste) == 0:
        print("La liste est vide.")
    else: 
        print(titre)
        for numero, element in enumerate(liste, start=1):  
            print(numero, "-", element)
                



while choix != 5:
    print("===== GESTIONNAIRE DE COURSES =====")
    print("1-Afficher la liste")
    print("2-Ajouter un produit")
    print("3-Supprimer un produit")
    print("4-Trier la liste")
    print("5-Quitter")
    choix = int(input("Choisissez une option (1-5) : "))
    
    if choix == 1:
        afficher_liste(courses, "=== MA LISTE ===")

    elif choix == 2:
        produit =input("Saisissez le produit à ajouter : ")
        courses.append(produit)
        print("Le produit", produit, "à été ajouté !") 

    elif choix == 3:
        if len(courses) == 0:
            print("La liste est vide.")
        else:
            produit = input("Entrez le produit à supprimer : ")
            if produit in courses:
                courses.remove(produit)
                print("Le produit", produit, "à été supprimé !")
            else:
                print("Le produit", produit, "n'est pas dans la liste.")

    elif choix == 4:
        courses.sort()
        afficher_liste(courses, "=== MA LISTE TRIE ===")
        
    elif choix == 5:
        print("Au revoir !")
    else :
         print("Choix invalide.")
     