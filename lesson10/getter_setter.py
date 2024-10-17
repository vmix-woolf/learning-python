class Person:
    def __init__(self, value):
        self.__age = None
        self.age = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age <= 0:
            raise ValueError('Age cannot be negative')
        else:
            self.__age = age

if __name__ == "__main__":
    person = Person(10)
    print(person.age)
    person.age = 5
