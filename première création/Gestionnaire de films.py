#ROADMAP
#1-créer une liste vide 
#2-Demander une Option à selectionner à l'utilisateur
#3-Afficher la liste
#4-Ajouter un film
#5-Supprimer un film
#6-Trier la liste
#7-Quitter

films = []
def afficher_films():
    if len(films) == 0:
        print("La liste est vide.")
    else:
        print("==== MA LISTE ====")
        for i, film in enumerate(films, start=1):
            print(i, "-", film)

def trier_films():
    if len(films) == 0:
        print("La liste est vide.")
    else:
        films.sort()
        print("==== MA LISTE TRIÉE ====")
        for i, film in enumerate(films, start=1):
            print(i, "-", film)

while True:
    print("==== GESTIONNAIRE DE FILMS ====")
    print("1-Afficher les films")
    print("2-Ajouter un film")
    print("3-supprimer un film")
    print("4-Trier les films")
    print("5-Quitter")
    option =int(input("choisissez une option entre (1 à 5) : "))

    if option == 1:
        afficher_films()
    
    elif option == 2:
        film =input("Saisissez le film à ajouter : ")
        films.append(film)
        print("le film", film, "a été ajouté !")

    elif option ==3:
        if len (films) == 0:
            print("Aucun film à supprimer dans la liste.")
        else:
            film = input("Saisissez le film à supprimer :")
            if film in films:
                films.remove(film)
                print("le film", film, "a été supprimé !")
            else:
                print("le film", film, "n'est pas dans la liste.")      
    elif option == 4:
        trier_films()
            
    elif option == 5:
        print("Au revoir !")
        break
    else:
        print("Veuillez choisir une option entre 1 et 5.")
                  

 