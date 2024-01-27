"""
i = 0
while i <= 5:
    i += 1
    print(i)
    if i == 3:
         break
else:
    print("while is completed")
"""
number = int(input("entere a number (-1 to quit)"))
while number != -1:
    print(number)
    number = int(input("entere a number (-1 to quit)"))
else:
    print("in else block")
