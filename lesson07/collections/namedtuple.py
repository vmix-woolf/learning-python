import collections

# Створення іменованого кортежу
Point = collections.namedtuple('Point', ['x', 'y'])
# Створення екземпляра Point
p = Point(x=11, y=22)

# Доступ до елементів
print(p.x)  # 11
print(p.y)  # 22

# Створення іменованого кортежу Person
Person = collections.namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

# Створення екземпляра Person
person = Person('Mick', 'Nitch', 35, 'Boston', '01146')

# Виведення різних атрибутів іменованого кортежу
print(person.first_name)       
print(person.post_index) 
print(person.age)        
print(person[3])         
