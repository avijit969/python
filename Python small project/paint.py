import math

height_weidth = input("enter height and weidth separated by comma :")
list1 = height_weidth.split(",")
per_can_paint = 7
for i in range(len(list1)):
    list1[i]=int(list1[i])


def how_many_cans(height, weight, percan):
    no_of_cans = (height * weight) / percan
    return math.ceil(no_of_cans)


no_of_cans = how_many_cans(list1[0], list1[1], per_can_paint)
print(f"{no_of_cans} numbers of cans are required to paint the {(list1[0] *list1[1])} square meter of wall")
