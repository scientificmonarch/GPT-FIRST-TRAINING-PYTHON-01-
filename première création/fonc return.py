courses = ["Riz", "Tomate", "Poisson"]

def chercher_produit(liste, produit_rechercher):
    for i in liste:
        if produit_rechercher == i:
            return produit_rechercher

    return None


recherche = input("Entrez le produit à rechercher : ")
produit = chercher_produit(courses, recherche)
print(produit)
