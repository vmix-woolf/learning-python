import re

text = "Рік 2023 був складнішим, ніж 2022"
pattern = r"\d+"
matches = re.findall(pattern, text)

print(matches)

text = "Python - це проста, але потужна мова програмування."
pattern = r"\w+"
matches = re.findall(pattern, text)

print(matches)  # Виведе список всіх слів у рядку

text = "Контакти: example1@example.com, example2@sample.org"
pattern = r"\w+@\w+\.\w+"
matches = re.findall(pattern, text)

print(matches)  # Виведе всі знайдені електронні адреси

file_name = "Мій документ Python.txt"
pattern = r"\s"
replacement = "_"
formatted_name = re.sub(pattern, replacement, file_name)

print(formatted_name)  


