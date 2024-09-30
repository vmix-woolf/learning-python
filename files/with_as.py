file_name = "./files/test.txt"

with open(file_name, 'r') as fh:
    for line in fh:
        line = line.strip()

        print(line)