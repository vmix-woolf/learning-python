numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i ** 2 for i in numbers}
print(sq)

odd_squares = {x**2 for x in range(1, 10) if x % 2 != 0}
print(odd_squares)
