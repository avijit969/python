year = int(input("Enter your year"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("it is not a leap year")
    else:
        print("It is a leap year")
else:
    print("it is not a leap year")
