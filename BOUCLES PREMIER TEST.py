# Afficher les nombres de 0 à 4
for i in range(5):
    print(i)


# range 
print("range(5) :",  range(5))
print("range(1, 5) :", range(1, 5)  )
print("range(1,10, 2):", range(1, 10, 2)  )








# list
print("range(5) : ",  list(range(5)))
print("range(1, 5) :", list(range(1, 5)))
print("range(1,10, 2) :", list(range(1,10, 2)))


#EXERCICE 1
for i in range(1, 11):
    print(i)

#EXERCICE 2
for i in range(0,21, 2):
    print(i)

#EXERCICE 3
nombre = int(input("Table de multiplication de ?"))
for i in range(1, 11):
    print(nombre, "x", i, "=", nombre*i)

#EXERCICE 4
nombre = -1
while nombre != 0:
    nombre = int(input("Tape un nombre(0pour quitter):"))
    print("Tu as tappé, nombre")
    
