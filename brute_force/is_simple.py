def is_simple_number(num):
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            return False
        divisor += 1
    return True

print(is_simple_number(4))
print(is_simple_number(20))
print(is_simple_number(37))
print(is_simple_number(11))