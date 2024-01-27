class Instructor:
    followers = 0

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display(self, course):
        print(f"Hii , i am {self.name} and i teach {course}")


Instructor_1 = Instructor("avi", "jaleswar")
print(Instructor_1.followers)
Instructor_1.display("paython")
