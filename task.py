def main():
#todo = more positive or negative task

#variable to count negative or positive
    positive_count = 0
    negative_count = 0

#make a loop to get input continuously
while true : 
    number = int(input("Entrer un nombre: "))

    # add to counts for eah number
    #stop the loop if 0 is entered
    if number > 0:
        positive_count +=1
    elif number < 0:
        negative_count +=1
    else:
        break #0

if positive_count> negative_count:
    print("Positive")
elif negative_count > positive_count:
    print("Negative")
else:
    print("Equal")

main()

