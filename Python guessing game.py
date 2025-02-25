import random 
randnumber = random.randint(1 , 100)
userguess = None 
guesses = 0 

while userguess != randnumber :
    userguess = int(input("Enter the number between 1 and 100  : "))
    if userguess == randnumber :
        print("You guessed the right number ")
    else :
        if userguess > randnumber :
            print("You guessed a higher number ")
        else :
            print("You guessed a smaller number ")
guesses += 1 
print(f"The number of guesses it took you to guess in {guesses} times . ")

