fh = open('./files/test.txt', 'w')
symbols_written = fh.write('hello!')
print(symbols_written)
fh.close()