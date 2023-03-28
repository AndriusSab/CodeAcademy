# from collections.abc import Callable


# def say_hello(name: str) -> None:
#     print(f"hello {name}")


# def another_function(f: Callable, *args) -> None:
#     f(*args)


# another_function(say_hello, "Andrius")


# def outer():
#     print("I am function outer()!")

#     def inner():
#         print("I am function inner()!")

#     # Function outer() returns function inner()
#     return inner


# function = outer()
# print(function)
# # <function outer.<locals>.inner at 0x7f18bc85faf0>
# function()
# # I am function inner()!

# outer()()
# # I am function inner()!

from ast import Tuple


animals = ["ferret", "vole", "dog", "gecko"]


def reverse_len(string: str) -> int:
    return -len(string)


sorted(animals, key=reverse_len)
# ['ferret', 'gecko', 'vole', 'dog']

# This could be changed with lambda function:

# animals = ["ferret", "vole", "dog", "gecko"]
# sorted(animals, key=lambda s: -len(s))
# # ['ferret', 'gecko', 'vole', 'dog']


# def func(x) -> Tuple[int]:
#     return x, x**2, x**3


# print(func(2))

print((lambda s: (s, s**2, s**3))(2))
print((lambda x: {1: x, 2: x**2, 3: x**3})(2))
