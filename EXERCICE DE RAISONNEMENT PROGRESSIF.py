# REGLE DE CINEMA
# Demande des informations à l'utilisateur
age = int(input("Entrez l'âge de la personne : "))
est_etudiant = input("La personne est-elle étudiante ? (oui/non) : ").strip().lower()

# 1. Détermination du prix de base selon l'âge
if age < 12:
    prix = 5
elif 12 <= age <= 17:
    prix = 8
else:
    prix = 12

# 2. Application de la réduction étudiante
if est_etudiant == "oui":
    prix = prix - 2

# 3. Application du prix plancher (minimum 3 €)
if prix < 3:
    prix = 3

# Affichage du résultat final
print(f"Prix du billet : {prix} €")
