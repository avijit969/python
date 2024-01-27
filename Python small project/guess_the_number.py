import random
import patten

EASY_DIFFICULTY_LEVEL = 10
HARD_DIFFICULTY_LEVEL = 5
chosen_number = random.randint(1, 50)


def difficulty_level(level):
    if level == 'easy':
        return EASY_DIFFICULTY_LEVEL
    elif level=='hard':
        return HARD_DIFFICULTY_LEVEL


def answer(times):
    for i in range(times, -1, -1):
        if i == 0:
            print(patten.loss)
            break
        print(f"You have {i} attempts remaining to the guess the number: ")
        num = int(input("gauss the number:"))
        if chosen_number == num:
            print(f"You guess right number {chosen_number} you are the winner !")
            print(patten.winner)
            break
        elif chosen_number < num:
            print("Your gauss is too high")
        elif chosen_number > num:
            print("Your gauss is too low")


print(patten.logo)
print("Let me thing a number between 1 to 50:\n")
#print(chosen_number)
level = input("Choose your difficulty level type.. easy or hard :")
difficulty = difficulty_level(level)
if difficulty == 10:
    answer(difficulty)
else:
    answer(difficulty)
