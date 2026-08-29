# from Lec4Tools import build_a_framework, build_a_door

# def build_a_house(tree, rocks, sands ...):
#     # Build a house whole process

#     # Build door
#     for i in range(...):
#         ...
#     # Build framework
#     while (...):
#         ... 
#     # Build windows
#     if (...):
#         ... 

# def build_a_house(tree, rocks, sands ...):
#     # Decompose:
#     build_a_door(...)
#     build_a_framework(...)

# # def build_a_door(tree, rocks, sands):
# #     ...

# # def build_a_framework(tree, rocks, sands):
# #     ...



# for i in range(...):
#     ...
#     for j in range(...):
#         ... 

# def double_loop_1():
#     for i in range(...):
#         # ...
#         inner_loop()

# def inner_loop():
#     for j in range(...):
#         ...

# def double_loop_2():
#     for i in range(...):
#         ...
#         for j in range(...):
#             ...

# inner_counter = 0
# outer_counter = 0 

# def increment(i):
#     i += 1
#     return i 

# inner_counter = increment(inner_counter)
# # outer_counter = increment(outer_counter)
# print("inner_counter: ", inner_counter)
# print("outer_counter: ", outer_counter)

# def f(x):
#     y += 1 
#     print("in f(x): y = ", y)
#     return y 


# x = 3 
# z = f(x)
# print("y = ", y) 

# print("z = ", z, "x = ", x)

# def is_even(i):
#     i % 2 == 0 

# is_even(2)
# print(is_even(2))

# # Type: Int -> (Int -> Int)
# def plus_two(x, y):
#     return x + y 

# # Type: Int -> Int
# def plue_one(5, y):
#     return 5 + y 


"""
1. Function programming
2. OOP (Object-oriented programming)
3.Imperative programming 
"""

def func_a():
    print('inside func_a')

def func_b(y):
    print('inside func_b')
    return y

def func_c(z):
    print('inside func_c')
    return z()

print(func_a())
print(5+func_b(2))
print(func_c(func_a))