height = int(input("Enter your height :"))
if height >= 3:
    print("You can ride")
    age = int(input("What is your age ?:"))
    if age <= 18:
        print("pay 250 Rs")
    elif age > 18:
        print("pay 500 Rs")
else:
    print("you can not ride")
