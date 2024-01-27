num = input("Enter your numbers separated by space:")
num_list = num.split()
count = 0;
# finding the length of the list
for i in num_list:
    count += 1
# converted into integer list
for i in range(0, count):
    num_list[i] = int(num_list[i])

# finding the maximum number in the list
maximum = num_list[0]
for maxi in num_list:
    if maxi > maximum:
        maximum = maxi
print(f"The maximum number in the given list is :{maximum}")
