from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}
# memo = {0: 0, 1: 1}


def fibonaci(n: int) -> int:
    if n <= 1:
        return n
    return fibonaci(n - 2) + fibonaci(n - 1)


print(fibonaci(5))


def fibonaci2(n: int) -> int:
    if n not in memo:
        memo[n] = fibonaci2(n - 2) + fibonaci2(n - 1)
    return memo[n]


print(fibonaci2(5))
print(fibonaci2(10))
print(fibonaci2(50))
