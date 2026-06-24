import random

# 1. configuration des variables 
debut = 1
fin = 100
nombre_secret = random.randint(debut, fin)
essais = 0
trouve = False

print(f"Devinez la position du nombre entre {debut} et {fin} !")

# 2. la boucle de jeu 
while not trouve:
    proposition = int(input("votre propostion :"))
    essais += 1

    #3. les conditions
    if proposition < nombre_secret:
        print("C'est plus haut !")
    elif proposition > nombre_secret:
        print("C'est plus bas !")
    else:
        print(f"Bravo ! Trouvé ")
        trouve = True 

