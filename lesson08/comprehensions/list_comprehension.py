sq = [x**2 for x in range(1, 6)]
print(sq)

even_squares = [x**2 for x in range(1, 10) if x % 2 == 0]
print(even_squares)

# normal style
even_squares = []
for x in range(1, 10):
    if x % 2 == 0:
        even_squares.append(x**2)

print(even_squares)  # Виведе [4, 16, 36, 64]
