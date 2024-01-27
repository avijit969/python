def add(a, b):
    c = a + b
    print(f"sum is {c}")


# calling the add function
add(1, 3)


# types of argument
def greet(name, subject, dept="sc"):
    print(f"hello {name}")
    print(f"Are you from {dept} department ?")
    print(f"and your subject is {subject}")


# calling greet function with keyword argument
# greet("avi", dept="cse")
# default argument
greet("disha", "python")
def add(*numbers): # tupple(5,7,9) arbitary argument
    c=0
    for i in numbers:
        c=c+i
    print(F"sum is {c}")

add(1,2,3,4,5)
add(1,2)