name1 = input("Enter your name: ")
name2 = input("Enter your partner name:")
name = (name1 + name2).lower()
t, r, u, e = name.count('t'), name.count('r'), name.count('u'), name.count('e')
l, o, v, e1 = name.count('l'), name.count('o'), name.count('v'), name.count('e')
percentage = int(str(t + r + u + e) + str(l + o + v + e1))

if percentage < 10:
    print(f"your percentage is {percentage} give time to your relationship")
elif percentage > 10 or percentage < 90:
    print(f"your percentage is {percentage} you are best couple enjoy")
else:
    print(f"your score is{percentage}")
