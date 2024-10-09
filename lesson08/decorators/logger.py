def complicated(x: int, y: int) -> int:
    return x + y

def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

complicated = logger(complicated)
print(complicated(2, 3))
