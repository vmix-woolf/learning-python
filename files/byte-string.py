byte_string = b'Hello world!'
print(byte_string)

byte_str = 'some text'.encode()
print(byte_str)

# Перетворення списку чисел у байт-рядок
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)  # Виведе байтове представлення чисел
for num in [127, 255, 156]:
  print(hex(num))

s = "Привіт!"
utf8 = s.encode()
print(f"UTF-8: {utf8}")
utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")
cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")
s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)

byte_array = bytearray(b"Hello")
byte_array.append(ord("!"))  
print(byte_array)

text = "Python Programming"
print(text.casefold())

german_word = 'straße'  # В нижньому регістрі
search_word = 'STRASSE'  # В верхньому регістрі
# Порівняння за допомогою lower()
lower_comparison = german_word.lower() == search_word.lower()
# Порівняння за допомогою casefold()
casefold_comparison = german_word.casefold() == search_word.casefold()
print(f"Порівняння з lower(): {lower_comparison}")
print(f"Порівняння з casefold(): {casefold_comparison}")
