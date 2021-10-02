"""RECURSION"""

# 1. Write the Fibonacci function using recursion.

# 2. Write a function to calculate the factorial of n recursively.

# 3. Write a recursive function to calculate the sum of elements of a list.

# 4. Write a recursive function to calculate the geometric sum of n, where r = 2, a = 1.


# def loop(n):
#     print(n)
#     if n == 0:
#         return
#
#     loop(n - 1)  # loop(9), n -= 1
#
# loop(10)


# def factorial(n):
#     if n == 1:
#         return 1
#
    # return n * factorial(n - 1)  # 5 * factorial(4) = 5 * 4 * factorial(3) = 5 * 4 * 3 * factorial(2) = 5 * 4 * 3 * 2 * 1 (factorial(1))
#
#
# print(factorial(5))


# def l(x: list) -> float:
#     if len(x) == 1:
#         return x[0]
#
#     return x[0] + l(x.pop(0))
#
# lst = [1, 5, 6]
# print(l(lst))


# def func(lst):
#     if len(lst) == 1:
#         return lst[0]
#
#     return lst[0] + func(lst[1:])  # 1 + func([2, 3]) = 1 + 2 + func(lst[3]) = 1 + 2 + 3
# # func([2, 3]) = 2 + func([3])
#
#
#
# def func(lst):
#     if len(lst) == 1:
#         return lst[0]
#
#     return lst[-1] + func(lst[:-1])
#
#
# print(func([1, 2, 3]))
#
#
# def gs(n: int) -> [float, int]:
#     if n == 0:
#         return 1
#
#     return 2 ** n + gs(n - 1)
#
# print(gs(5))
#
#
# def rfib(n):
#     if n == 1:
#         return 1
#     return n + n ** (n - 1)
#
#
# print(rfib(4))


# def gm_sum(n, coeff, ratio):
#     if n == 0:
#         return 1
#     else:
#         return coeff * ratio ** n + gm_sum(n - 1, coeff, ratio)
#
#
# a = 1
# r = 2
# print(gm_sum(5, a, r))


# def rfib(n):
#     if n == 0:
#         return 1
#
#     return 2 ** n + rfib(n - 1)
#
#
# print(rfib(1))
# print(rfib(2))
# print(rfib(3))
# print(rfib(4))
#


# def geo_sum(n, a, r):
#     if n == 0:
#         return a
#
#     return a * r ** n + geo_sum(n - 1, a, r)
#
# print(geo_sum(5, 1, 2))


def fibo(n: int) -> int:
    if n < 0:
        return -1

    if n < 2:
        return n

    return fibo(n - 1) + fibo(n - 2)


durations = []
for i in range(6):
    # start time
    print(fibo(i))
    # end time
    # durations.append(end time - start time)


# def fibo(n):
#     if n == 1:
#         return
#
#     return fibo(n - 1) + fibo(n - 2)
#
# print(fibo(10))