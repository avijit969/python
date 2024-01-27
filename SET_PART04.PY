set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7, 8}
set3 = {1, 2}
print(set1.isdisjoint(set2))  # nothing is common
print(set3.issubset(set1))  # every element of set3 present in set1
print(set3 <= set3)  # subset operator <=
print(set1.issuperset(set3))  # reverse of subset
# set1.clear()
# del set1 # also delete the set
print(set1)
