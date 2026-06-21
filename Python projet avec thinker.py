import random
import tkinter as tk

# 1. Le cœur du jeu (La logique)
nombre_secret = random.randint(1, 100)

def verifier_proposition():
    # On récupère ce que le joueur a tapé et on le transforme en nombre (int)
    proposition = int(boite_saisie.get())
    
    # On vérifie comme dans ton code d'origine
    if proposition < nombre_secret:
        texte_resultat.config(text="C'est plus haut ! ⬆️")
    elif proposition > nombre_secret:
        texte_resultat.config(text="C'est plus bas ! ⬇️")
    else:
        texte_resultat.config(text="Bravo ! C'est gagné ! 🎉")

# 2. La construction de la fenêtre (Les Legos)
fenetre = tk.Tk()
fenetre.title("Mon Premier Jeu de Devinette")
fenetre.geometry("300x200") # La taille de la fenêtre

# Une étiquette pour donner la consigne
consigne = tk.Label(fenetre, text="Devine le nombre entre 1 et 100 :")
consigne.pack(pady=10) # .pack() sert à poser le bloc dans la fenêtre

# Une boîte pour que le joueur écrive son nombre
boite_saisie = tk.Entry(fenetre)
boite_saisie.pack(pady=10)

# Le bouton qui lance la vérification quand on clique dessus
bouton_valider = tk.Button(fenetre, text="Valider", command=verifier_proposition)
bouton_valider.pack(pady=10)

# Une étiquette vide qui affichera les indices (Plus haut / Plus bas)
texte_resultat = tk.Label(fenetre, text="")
texte_resultat.pack(pady=10)

# 3. On allume le moteur !
fenetre.mainloop()