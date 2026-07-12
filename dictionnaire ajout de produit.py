stock = []
option = 0

while option != 3:
    print("=== Gestion de Stock ====")
    print("1- Ajoutez un produit au stock")
    print("2- Afficher le stock")
    print("3- Quittez le programme")

    option = int(input("Choisissez une option entre 1 et 3 : "))

    if option == 1:
        nom = input("Nom : ")
        prix = int(input("Prix : "))
        quantite = int(input("Quantité : "))
        produit = {
            "Nom": nom,
            "Quantité": quantite,
            "Prix": prix,
        }
        stock.append(produit)
        print("Produit ajouté au stock.")

    elif option == 2:
        if not stock:
            print("Votre stock est vide")
        else:
            print("Stock actuel :")
            for numero, produit in enumerate(stock, start=1):
                print(numero, "-", produit)

    elif option == 3:
        print("Fermeture du gestionnaire de stock")

    else:
        print("Choisissez un nombre valide")








     
    