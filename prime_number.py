import math



def prime(number):
    flag = 0
    if number == 1:
        flag = 1
    for i in range(2, math.ceil(math.sqrt(number))):
        if number % i == 0:
            flag = 1
    if flag == 0:
        print(f"{number} is a prime number")
    else:
        print(F"{number} is not a prime number")

number = int(input("Enter your number to check weather it is prime or not:\n"))
prime(number)
