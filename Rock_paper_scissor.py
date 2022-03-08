import random 

lst = ['r','p','s']

computer_point = 0
human_point = 0
chances = 5
no_of_chances = 0

print("\t \t \t \t  Welcome to Rock Paper Scissor Game " )
print("Rock for r \nScissor for s \nPaper for p " )
print("\n")

while no_of_chances < chances :
    user_input  = input("Enter your guess :").lower()
    random_input = random.choice(lst)
    if user_input == random_input:
        print("game tie Both or Equal 0 points")
        print(f"computer guess : {random_input}\nyour guess is : {user_input}")
    elif user_input == 'r' and  random_input == 'p':
        computer_point = computer_point +5
        print("Computer is win ")
        print(f"computer guess : {random_input}\nyour guess is : {user_input}")
        print(f"computer point is : {computer_point} ,human_point is : {human_point}")
    elif user_input == 'r' and random_input == 's':
        human_point = human_point + 5
        print("Human is win")
        print(f"computer guess : {random_input}\nyour guess is : {user_input}")
        print(f"computer point is : {computer_point},human_point is : {human_point}")
    elif user_input == 's' and random_input == 'r':
        computer_point = computer_point +5
        print("computer is win")
        print(f"computer guess : {random_input}\nyour guess is : {user_input}")
        print(f"computer point is : {computer_point} ,human_point is : {human_point}")
    elif user_input == 's' and random_input == 'p':
        human_point = human_point + 5
        print("Human is win")
        print(f"computer guess : {random_input}\nyour guess is : {user_input}")
        print(f"computer point is : {computer_point}, human_point is : {human_point}")
    elif user_input == 'p' and random_input == 'r':
        human_point = human_point + 5
        print("Human is win")
        print(f"computer guess : {random_input}\nyour guess is : {user_input}")
        print(f"computer point is : {computer_point} ,human_point is : {human_point}")
    elif user_input == 'p' and random_input == 's':
        computer_point = computer_point +5
        print("computer is win")
        print(f"computer guess : {random_input}\nyour guess is :{ user_input}")
        print(f"computer point is : {computer_point}, human_point is : {human_point}")
    else:
        print('invalid letter')
    no_of_chances = no_of_chances + 1
    print(f"Total chances {chances}\nRemianing chances {chances-no_of_chances}\n")
if computer_point == human_point:
    print("Game is tie")
    print(f"computer point is : { computer_point}, human_point is : { human_point}")
elif computer_point > human_point:
    print("computer is win")
    print(f"computer point is : { computer_point}, human_point is : { human_point}")
else:
    print("Human is win")
    print(f"computer point is : { computer_point}, human_point is : { human_point}")





        



            




    


