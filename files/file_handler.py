file_name = "./files/test.txt"

fh = open(file_name, "w")
symbols_written = fh.write("hello!")
print(symbols_written)
fh.close()

fh = open(file_name, 'w+')
fh.write('hello!')
fh.seek(0)

first_two_symbols = fh.read(2)
print(first_two_symbols)  # 'he'

fh.close()

fh = open(file_name, 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open(file_name, 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)

fh.close()

fh = open(file_name, 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open(file_name, 'r')
lines = [el.strip() for el in fh.readlines()]
print(lines)

fh.close()

fh = open(file_name, "w+")
fh.write("hello!")

position = fh.tell()
print(position)  # 6

fh.seek(1)
position = fh.tell()
print(position)  # 1

fh.read(2)
position = fh.tell()
print(position)  # 3

fh.close()
