import re

text = "Вивчення Python\n може бути веселим."
pattern = "\s"
match = re.search(pattern, text)

if match:
    print("Знайдено:", match.groupdict())
else:
    print("Не знайдено.")

text = "Моя електронна адреса: example@example.com"
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)

if match:
    print("Електронна адреса:", match.group())

text = "Вивчення Python може бути веселим."
pattern = r"в\w*м"
match = re.search(pattern, text, re.IGNORECASE)

if match:
    print("Знайдено:", match.group())

email = "username@domain.com"
pattern = r"(\w+)@(\w+\.\w+)"
match = re.search(pattern, email)

if match:
    user_name = match.group(1)
    domain_name = match.group(2)
    print("Ім'я користувача:", user_name)
    print("Домен:", domain_name)
