import random
print("Welcome to random number gusser game")
print("I will guss number from 1 to 50 ")
Difficulty = str(input("What is your difficulty Easy or hard:- ")).lower()
def difficiulty(Difficulty):
    random_number = 5
    if Difficulty == "easy":
        print("you will get 10 chances")
        chances = 1
        while True:
            number_choosen = int(input("Enter the guess number between 1 to 50: "))
            if chances <= 10 :
                chances += 1
                if number_choosen < random_number:
                    print("your guess number is lower")
                 
                elif number_choosen > random_number:
                    print("your guess number is  higer")
            
                elif number_choosen == random_number:
                    print("guessed number is correct : ",number_choosen)
                    break
                    
            else :
                print("your chance is over ,correct  number is : ",random_number)
                break  
               
        if number_choosen != random_number :
            return "you lost"
    
    elif Difficulty == "hard":
        print("you will get 5 chances")
        chances = 1
        while True:
            number_choosen = int(input("Enter the guess number between 1 to 50: "))
            if chances <= 5 :
                chances += 1
                if number_choosen < random_number:
                    print("your guess number is lower")
                 
                elif number_choosen > random_number:
                    print("your guess number is  higer")
            
                elif number_choosen == random_number:
                    print("guessed number is correct : ",number_choosen)
                    break
                    
            else :
                print("your chance is over ,correct  number is : ",random_number)
                break  
               
        if number_choosen != random_number :
            return "you lost"
obj =difficiulty(Difficulty)
print(obj)
