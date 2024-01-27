import random

length = int(input("Enter the target sum: "))
# Generate three random numbers
num1 = random.randint(0, length)
print(num1)
num2 = random.randint(0, length - num1)
print(num2)
num3 = length - (num1 + num2)
print(num3)
