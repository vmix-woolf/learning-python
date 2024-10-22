import pickle

class Human:
    def __init__(self, name):
        self.name = name

bob = Human("Bob")
with open("instance.pickle", "wb") as file:
    pickle.dump(bob, file)

with open("instance.pickle", "rb") as file:
    loaded_instance = pickle.load(file)

print(loaded_instance.name)
