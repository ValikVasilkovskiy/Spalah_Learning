from datetime import datetime
from time import sleep
class Human():
    def __init__(self, first_name, last_name, age, middle_name=""):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.age = age
        self.created = datetime.now()

    def get_full_name(self):
        if self.middle_name:
            return "{} {} {}".format(self.first_name, self.middle_name, self.last_name)
        return "{} {}".format(self.first_name, self.last_name)

    def info(self):
        return "{} {} {}".format(self.get_full_name(), self.age, self.created)


h1 = Human("Alex", "Sazanov", 26)
print(h1.first_name, h1.last_name)
print(h1.created)
print(h1.info())

sleep(3)

h2 = Human(first_name='Dima', last_name='K', age=26, middle_name="Man")
print(h2.age)
print(h2.created)


