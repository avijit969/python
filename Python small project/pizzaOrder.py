print("pizza size and price\n1.small pizza=100\n2.medium pizza=200\n3.large pizza=300")
pizza = int(input("Select any one of these(1,2 and 3)"))
bill = 0
if pizza == 1:
    bill = 100
elif pizza == 2:
    bill = 200
elif pizza == 3:
    bill = 300
else:
    print("please select valid number")

add_pepperoni = input("Do you want pepperoni (Y/N)")
if add_pepperoni == 'y' or add_pepperoni == 'Y':
    if pizza == 1:
        bill += 30
    else:
        bill += 50
extra_cheese = input("Do you want extra cheese (Y/N)")
if extra_cheese == 'y' or extra_cheese == 'Y':
    bill += 20

print(f"your total bill is {bill}")
