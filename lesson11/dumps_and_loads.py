import pickle

# Об'єкт для серіалізації
my_data = {"key": "value", "num": 42}

# Серіалізація об'єкта в байтовий рядок
serialized_data = pickle.dumps(my_data)
# Виведе байтовий рядок
print(serialized_data)  

# Десеріалізація об'єкта з байтового рядка
deserialized_data = pickle.loads(serialized_data)
# Виведе вихідний об'єкт Python
print(deserialized_data)

# Серіалізація об'єкта в файл
my_data = {"key": "value", "num": 100}
with open("data.pickle", "wb") as file:
    pickle.dump(my_data, file)

# Десеріалізація об'єкта з файлу
with open('data.pickle', 'rb') as file:
    deserialized_data = pickle.load(file)
# Виведе вихідний об'єкт Python
print(deserialized_data)
