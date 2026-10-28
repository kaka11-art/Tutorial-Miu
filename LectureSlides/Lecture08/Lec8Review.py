class Coordinate(object):
    
    # Construction
    def __init__(self, x, y):
        # Attributes
        self.x = x 
        self.y = y 

    # System output (IO)
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __lt__(self, other):
        if (self.x < other.x) or ((self.x == other.x) and (self.y < other.y)):
            return True
        else:
            return False

    def __len__(self):
        return self.distance(Coordinate(0.0, 0.0))

    # Method
    def distance(self, other):
        x_diff = self.x - other.x 
        y_diff = self.y - other.y
        return (x_diff**2 + y_diff**2)**0.5 

c = Coordinate(3.0, 4.0)
d = Coordinate(2, 5)
origin = Coordinate(0, 0)

e = c + d 
f = c - d 

c2 = Coordinate(3, 4)
# print(c == c2)

print(len(c))

# print(c)

# print(c.distance(origin))
# print(Coordinate.distance(c, origin))


# ==============
# Library System
# ==============

class Student(object):

    # Step 1. Construction
    def __init__(self, name, age, gender, subject, id):
        # Student attributes
        self.name = name
        self.age = age 
        self.gender = gender
        self.subject = subject
        self.id = id

    # Step 2. System output
    def __str__(self):
        title = "----------"
        return title + "\nName:" + str(self.name) + "\nAge:" + str(self.age) + "\nGender:" + str(self.gender) + "\nSubject:" + str(self.subject) + "\n" + title

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.age < other.age

# Instances
Alice = Student("Alice", 18, "Female", "Mathematics", 1)
Bob = Student("Bob", 20, "Male", "Computer Science", 2)

# print(Alice)
# print(Bob)