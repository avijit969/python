list1 = [['😁', '😁', '😁'], ['😁', '😁', '😁'], ['😁', '😁', '😁']]
print(f"{list1[0]}\n{list1[1]}\n{list1[2]}")
position = input("Enter your position you want to hide your money")
row, col = int(position[0]), int(position[1])
list1[row - 1][col - 1] = "x"
print(f"{list1[0]}\n{list1[1]}\n{list1[2]}")
