print("Welcome to Treasure Island!\nYour missionis to find the treasure")
user_input1 = input("you are at a crossroad, Where do you want to go?\nType left or right\n")
if user_input1 == "left" or user_input1 == "Left":
    user_input2 = input("What do you want to do now?\nType swim or wait\n")
    if user_input2 == "wait" or user_input2 == "Wait":
        user_input3 = input("Which door?\nType red or blue or yellow\n")
        if user_input3 == "yellow" or user_input3 == "Yellow":
            print("You win!")
        else:
            print("You lose!")
    else:
        print("You lose!")
else:
    print("You lose!")


