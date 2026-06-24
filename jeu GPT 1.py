## Description de l'Algorythme
# 1. Créer les variables.
# 2. Afficher les règles du jeu.
# 3. Demander une proposition.
# 4. Vérifier que la proposition est dans l'intervalle.
 #5. Comparer la proposition au nombre secret.

  #  - Si trop petit → afficher "Plus haut !" et recommencer.
   # - Si trop grand → afficher "Plus bas !" et recommencer.
    #- Si trouvé → afficher "Trouvé !" et arrêter. 
     

# Etape 1 : créer les variables
borne_min = 1
borne_max = 20

nombre_secret = 14

# Etape 2 : Informer le joueur
print("je pense à un nombre entre", borne_min, "et", borne_max)

# Etape 3: Demander une proposition au joueur
proposition = -1 
while proposition != nombre_secret:

    proposition = int(input("Devine un nombre : "))
    if proposition > 20 or proposition < 1: 
        print("veuillez entrer un nombre entre 1 et 20")

    elif proposition == nombre_secret:
        print("Trouvé, bravo !")

    elif proposition < nombre_secret:
        print("Plus haut, encore un essais !")
    
    else:
        print("Plus bas, encore un essais !")












        
    







