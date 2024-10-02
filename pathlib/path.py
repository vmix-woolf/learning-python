from pathlib import Path, PurePath
import shutil, time

p = Path("example.txt")
p.write_text("Hello, world!")
print(p.read_text()) 
print("Exists:", p.exists()) 

# Для Unix/Linux
path_unix = Path("/usr/bin/python3")
# Для Windows
path_windows = Path("C:/Users/Username/Documents/file.txt")
print(path_windows, path_unix)
# Початковий шлях
base_path = Path("/usr/bin")
# Додавання додаткових частин до шляху
full_path = base_path / "subdir" / "script.py"
print(full_path)  # Виведе: /usr/bin/subdir/script.py

# Перетворення відносного шляху в абсолютний
relative_path = Path("documents/example.txt")
absolute_path = relative_path.absolute()
print(absolute_path)

# Початковий шлях до файлу
original_path = Path("documents/example.txt")
# Зміна імені файлу
new_path = original_path.with_name("report.txt")
# Зміна імені файлу
new_path = new_path.with_suffix(".md")
print(original_path)
print(new_path)

# Створення об'єкту Path для файлу
file_path = Path("example.txt")
# Запис тексту у файл
file_path.write_text("Привіт світ!", encoding="utf-8")
text = file_path.read_text(encoding="utf-8")
print(text)

file_path = Path("example.bin")
# Бінарні дані для запису
data = b"Python is great!"
# Запис байтів у файл
file_path.write_bytes(data)
binary_data = file_path.read_bytes()
print(binary_data)

# Створення об'єкту Path для директорії
directory = Path("./files")
# Виведення переліку всіх файлів та піддиректорій
for path in directory.iterdir():
    print(path)

path = Path("./built-in functions")

# Перевірка існування
if path.exists():
    print(f"{path} існує")
# Перевірка, чи це директорія
if path.is_dir():
    print(f"{path} є директорією")
# Перевірка, чи це файл
if path.is_file():
    print(f"{path} є файлом")

# Вихідний і цільовий файли
source = Path('example.txt')
destination = Path('pathlib/report.txt')
# Копіювання файла
shutil.copy(source, destination)
shutil.move(destination, source)

file_path = Path("./files/byte-string.py")
# Отримання розміру файла
size = file_path.stat().st_size
# Час створення та модифікації
creation_time = file_path.stat().st_ctime
modification_time = file_path.stat().st_mtime
print(f"Час створення: {time.ctime(creation_time)}")
print(f"Час модифікації: {time.ctime(modification_time)}")
print(f"Розмір файла: {size} байтів")