"""tupple = (1, 2, 3, 4, 5)
for i in tupple:
    print(i)
    if i == 3:
        break
else:
    print("it completed")
"""
numbers = [1, 3, 5, 7, 9]
for num in numbers:
    if num % 2 == 0:
        print("Found an even number:", num)
        break
else:
    print("No even number found")

