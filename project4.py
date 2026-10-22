import random

hidden_number = random.randint (1, 100)

# A for loop starts here. it repeats lines 8 to 15 
for i in range(2):
#print (hidden_number)
    number = int(input("Pick a number 1-50"))
    if number == hidden_number:
        print (f"you guessed correct")

    if number < hidden_number:
        print ("you guessed to low")

    elif number > hidden_number:
        print ("you guessed to high")     
