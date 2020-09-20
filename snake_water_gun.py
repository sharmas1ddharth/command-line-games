import random

# list of elements
lst = ["s", "w", "g"]

# points and chances to play
user_point = 0
computer_point = 0
chance = 10
no_of_chance = 0

# loop if chance is less than total chances
while chance > no_of_chance:
    user_choice = input("Enter s/w/g : ")
    computer_choice = random.choice(lst)

    # if user and computer both input same character
    if user_choice == computer_choice:
        print("Draw no point")

    # if user enter s

    elif user_choice == "s" and computer_choice == "w":
        user_point = user_point + 1
        print(
            f"your guess is {user_choice} and computer guess is {computer_choice}\n")
        print("you win")
        print(
            f"your score = {user_point} and computer score = {computer_point}")

    elif user_choice == "s" and computer_choice == "g":
        computer_point = computer_point + 1
        print(
            f"your guess is {user_choice} and computer guess is {computer_choice}\n")
        print("you lose")
        print(
            f"your score = {user_point} and computer score = {computer_point}")

    # if user enter w

    elif user_choice == "w" and computer_choice == "s":
        computer_point = computer_point + 1
        print(
            f"your guess is {user_choice} and computer guess is {computer_choice}\n")
        print("you lose")
        print(
            f"your score = {user_point} and computer score = {computer_point}")

    elif user_choice == "w" and computer_choice == "g":
        user_point += 1
        print(
            f"your guess is {user_choice} and computer guess is {computer_choice}\n")
        print("you win")
        print(
            f"your score = {user_point} and computer score = {computer_point}")

    # if user enter g

    elif user_choice == "g" and computer_choice == "s":
        user_point += 1
        print(
            f"your guess is {user_choice} and computer guess is {computer_choice}\n")
        print("you win")
        print(
            f"your score = {user_point} and computer score = {computer_point}")

    elif user_choice == "g" and computer_choice == "w":
        computer_point = computer_point + 1
        print(
            f"your guess is {user_choice} and computer guess is {computer_choice}\n")
        print("you lose")
        print(
            f"your score = {user_point} and computer score = {computer_point}")

    else:
        print("Enter correct value")

    no_of_chance += 1
    print(f"{chance - no_of_chance} chance is left")

print("game over")

# if computer point is greater than human point
if user_point < computer_point:
    print("Score is\n")
    print('')
    print(
        f"human point is {user_point} and computer point is {computer_point}")
    print("computer wins")

# if human point is greater than computer point
elif user_point > computer_point:
    print("Score is\n")
    print('')
    print(
        f"human point is {user_point} and computer point is {computer_point}")
    print("human wins")
