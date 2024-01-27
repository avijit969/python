import random

names = input("Enter your all friends name by separated comma :")
names_split = names.split(",")
print(names_split)
random_index = random.randint(0, len(names_split)-1)
# print(f"{random.choice(names_split)} will pay the bill")
print(f"{names_split[random_index]} will pay the bill")

