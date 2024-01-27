import random

print("0.rock\n1.paper\n2.scissor")
user = int(input("chose any one of these"))
if user>=3 or user<0:
    print("Please select valid number")
else:
    boot = random.randint(0, 2)
    print(f"boot chose {boot}")
    if boot == user:
        print("match is draw try again")
    elif user == 0 and boot == 2:
        print("you are the winner")
    elif user == 2 and boot == 0:
        print("boot is winner")
    elif boot < user:
        print("you are the winner")
    elif boot > user:
        print("Boot is winner")
