import random
 

guess_count = 0
print("Hi welcome to the number guess game")
Name = input("Name:")

num = random.randint(0,50)
guess  = int(input("Enter the guess number between 1 to 50: "))

while guess_count < 4: 
    guess_count+= 1
    if num < guess:
        print("your guess number is  higer")
        guess  = int(input("Enter the guess number between 1 to 50: "))
    elif num > guess:
        print("your guess number is lower")
        guess  = int(input("Enter the guess number between 1 to 50: "))
    elif num == guess :
        break

if guess == num:
    print(Name,"guessed number is correct : ",num ,"And guess count :",guess_count)
if guess != num:
    print("Game is end")
    print("The correct number is :",num)    

    




