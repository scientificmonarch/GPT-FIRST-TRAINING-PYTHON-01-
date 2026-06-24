# Mention scolaire 
Question = ("quel est ta note ?")
Mention = float(input(Question))
if  Mention >= 16:
    print("Excellent")
elif Mention >= 14:
    print("Très bien")
elif Mention >= 12 :
    print ("Bien")
elif Mention >= 10:
    print ("Passable")
else :
    print("Insufisant")
