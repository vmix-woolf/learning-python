import re

text = "Python - це проста, але потужна мова програмування."
pattern = r"\s+"
words = re.split(pattern, text)

print(words)  # Виведе список слів у рядку

text = "Python - потужна; проста, універсальна: мова!"
pattern = r"[;,\-:!\s]+"
elements = re.split(pattern, text)

print(elements)  # Виведе список частин, розділених пунктуацією

text = "apple#banana!mango@orange;kiwi"
pattern = r"[#@;!]"
fruits = re.split(pattern, text)

print(fruits)
