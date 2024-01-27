set1 = {'ram', 'avi', 'avijit'}
set2 = {'disha', 'riya', 'simmy', 'avi'}
set3 = {'bishal', 'avishek'}
"""print(set1.union(set2))
print(set1 | set2)  # union of set
print(set1.union(set2,set3))
set1.update(set2)
print(set1)
set1.update(['jenny','raja'])
print(set1)

set1 |= set2  # setupadate
print(set1)

print(set1.intersection(set2))
print(set1 & set2)  # intersection
print(set1.intersection(['avijit', 'ram']))  # we can also pass list
set1.intersection_update(set2) # update set1 through intersection
print(set1)
"""
"""
difference between sets
print(set1.difference(set2))
print(set2.difference(set1))
print(set1-set2)

set1.difference_update(set2)
print(set1)
"""
print(set1.symmetric_difference(set2))  # it takes only one argument
print(set1^set2)
set2.symmetric_difference_update(set1) # update through symmetric difference
print(set2)
