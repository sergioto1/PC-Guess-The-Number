import random

def pcGuessNumber (x):
    low = 1
    high = x
    feedback = ""
    while (feedback != "c"):
        if (low != high):
            number = random.randint(low, high) #Lanza error si los dos limites son iguales
        else: 
            number = high #Tambien puede ser low, ambos valores son iguales
        print(f"The chosen number is {number}")
        feedback = input(f"Is the chosen number ({number}) (H) too High, \
            \n(L) too Low or is (C) The correct one??\n").lower()
        if (feedback == "h"):
            high = number - 1
        elif (feedback == "l"):
            low = number + 1
    print(f"The PC has guessed the number ({number}) succesfully!")

# Prueba
pcGuessNumber(15)
