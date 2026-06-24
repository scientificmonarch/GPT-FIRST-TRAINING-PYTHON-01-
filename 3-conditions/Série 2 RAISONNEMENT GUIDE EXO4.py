# EXERCICE 4
#classement sportif 

score = int(input("quelle est le score ?"))
if score < 50:
    print("Débutant")
elif score <= 69:
    print("Moyen")
elif score <= 89:
    print("Très bon")
else :
    print("Champion")
