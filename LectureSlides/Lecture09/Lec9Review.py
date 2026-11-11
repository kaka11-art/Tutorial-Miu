class people(object):

    def __init__(self, salary, interest, rate, age):
        self.salary = salary
        self.interest = interest
        self.rate = rate
        self.age = age

    # API (interface)
    def get_annual(self):
        return self.salary * self.interest * self.rate

    def get_age(self):
        return str(self.age % 10)

Alice = people(10000, 0.1, 0.05)

Alice.salary
print(Alice.get_annual())
# print(Alice.annual)


class Animial(object):
    def __init__(self, age):
        self.age = self.age 
        self.name = None

    def __str__(self):
        return str("Animial" + self.age)

class Rabbit(Animial):
    tag = 1

    def __init__(self, age):
        super().__init__(age)
        tag += 1

    def __str__(self):
        return str("Rabbit" + self.age)

    def rabbit_num(self):
        return Rabbit.tag

r1 = Rabbit(age=5)
n1 = r1.rabbit_num()

r2 = Rabbit(age=3)
n2 = r2.rabbit_num()

r3 = Rabbit(age=2)
n3 = r3.rabbit_num()

r4 = r1 + r2 