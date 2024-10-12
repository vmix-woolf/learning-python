from collections import UserString

# Створення класу, який розширює UserString
class MyString(UserString):
    # Додавання методу, який перевіряє, чи рядок є паліндромом
    def is_palindrome(self):
        return self.data == self.data[::-1]

# Створення екземпляру MyString
my_string = MyString("radar")
print("Рядок:", my_string)
print("Чи є паліндромом?", my_string.is_palindrome())

# Створення іншого екземпляру MyString
another_string = MyString("hello")
print("Рядок:", another_string)
print("Чи є паліндромом?", another_string.is_palindrome())


class TruncatedString(UserString):
    MAX_LEN = 7

    def truncate(self):
        self.data = self.data[:self.MAX_LEN]

ts = TruncatedString('hello world!')
ts.truncate()
print(ts)
