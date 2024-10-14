class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog:
    def __init__(self, animal):
        self.animal = animal

    def say(self):
        return self.animal.say()
    

cat_dog = CatDog(Cat('murz', 4))
print(cat_dog.say())    
