soiree_pass = ["clarisse019", "fredo027", "Albert162", "jacques051"]
# index :           0             1           2           3
print("Bienvenue à la soirée !!!")
admin = "stephane52"

# vérification de pass
while True:
    invite = input("Votre passe : ")
    if invite == admin or invite in soiree_pass:
        print("Acces autorisé !")
        break
    else:
        print("Acces refusé !")
 
    
