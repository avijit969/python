heights = input("Enter your height separated by space")
heights_list = heights.split()
count, total = 0, 0

for person in heights_list:
    count = count + 1
    total = total + int(person)
avg = total / count
print("Average height is ", round(avg))
