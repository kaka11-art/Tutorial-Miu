class people(object):

    def __init__(self, salary, interest, rate):
        self.salary = salary
        self.interest = interest
        self.rate = rate

    def get_annual(self):
        return self.salary * self.interest * self.rate

Alice = people(10000, 0.1, 0.05)

Alice.salary
print(Alice.get_annual())
# print(Alice.annual)