import random

fill_percentage = random.random() * 100
print(f"Заповнення: {fill_percentage:.2f}%")

target = random.randrange(1, 10, 2)
print(f"Ціль: {target}")

fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))

items = ['яблуко', 'банан', 'вишня', 'диня']
other_items = [1, 2, 3, 4, 5, 6, 7, 8]
chosen_item_fruits = random.choices(items, k=2)
chosen_item_numbers = random.choices(other_items, k=3)
print(chosen_item_fruits) 
print(chosen_item_numbers) 

participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
team = random.sample(participants, 4)
print(f"Команда: {team}")