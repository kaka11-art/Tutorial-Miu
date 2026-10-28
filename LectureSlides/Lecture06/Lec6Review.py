# def factorial(n):
#     """
#     Factorial: n * (n - 1) * (n - 2) * ... * 2 * 1
#     e.g., factorial(3) = 3 * 2 * 1
#           factorial(6) = 6 * 5 * 4 * 3 * 2 * 1
#     """
#     ans = 1
#     for i in range(1, n + 1):
#         ans *= i 
#     return ans 

# # print(factorial(1))
# # print(factorial(5))

# # 6! = 6 * 5!
# # n! = n * (n - 1)!
# def factorial_recursion(n):
#     if (n == 1) or (n == 0):
#         return 1
#     return n * factorial_recursion(n - 1)

# factorial_recursion(3)
# = 3 * factorial_recursion(2)
# = 3 * 2 * factorial_recursion(1)
# = 3 * 2 * 1

# proof: base case (e.g., 1)
# proof: if n is correct, then we need to show that n + 1 is correct


# # Fibbonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21,...
# # The nth term is the sum of (n - 1)th term and (n - 2)th
# def fib_recursion(n):
#     if (n == 1) or (n == 2):
#         return 1 
#     return fib_recursion(n - 1) + fib_recursion(n - 2)

# print(fib_recursion(7))
# # fib(7) 
# # = fib(6) + fib(5)
# # = (fib(5) + fib(4)) + (fib(4) + fib(3))
# # = ...
# # = 

# print(fib_recursion(8))

# -----> -----> ---->
# [1, 2, 3, ..,  7, 8]

#           <---- <---- <----
# [1, 2 , _, _, ..., _, fib_efficient(n-2, d)]

def fib_list(n):
    if (n == 1) or (n == 2):
        return 1
    else: 
        fibs = []
        fibs.append(1)
        fibs.append(1)
        print("Initial list:", fibs)
        for i in range(2, n):
            fibs.append(fibs[i - 1] + fibs[i - 2])
            print(fibs)
        return fibs[n - 1]

print(fib_list(5))

# def fib_memorization(n):
#     return fib_mem(n, 1, 1)

# # Helper function
# def fib_mem(n, a, b):
#     if (n == 1) or (n == 2):
#         return a
#     else:
#         return fib_mem(n - 1, a + b, a)

# print(fib_memorization(5))

#   fib_mem(5, 1, 1)
# = fib_mem(4, 2, 1)
# = fib_mem(3, 3, 2)
# = fib_mem(2, 5, 3)

# def mult(a, b):
#     ans = 0
#     for i in range(1, b + 1):
#         ans += a 
#     return ans

# # Memorization. 
# def fib(n):
#     return go(n, 0, 1)

# # x is the first term; y is second term
# # n is the counter
# def go(n, x, y):
#     # Base case
#     if n == 0:
#         return x 
#     return go(n - 1, y, x + y)

# # (x, y), x + y 
# # x, (y, x + y)


# # Dictionary Examples. 

# # Key -> value (dictionary)
# Alice_Info = { 
#     "Subject": "Mathematics",
#     "Math": "A+",
#     "Computer Science": "A"
# }

# Alice = {
#     "Age": 18,
#     "Gender": "Female",
#     "Grades": Alice_Info
# }

# Bob_Info = { 
#     "Subject": "Biology",
#     "Math": "A+",
#     "Biology": "A"
# }

# Bob = {
#     "Age": 20,
#     "Gender": "Male",
#     "Grades": Bob_Info,
#     "Salary": 1000,
# }

# students = [Alice, Bob]

# print(students[0])


grades = {
    'Ana':'B', 
    'John':'A+', 
    'Denise':'A', 
    'Katy':'A',
    'Sylvan': 'A'
}

def del_value(dict, value):
    keys = []
    for i in dict:
        if dict[i] == value:
            keys.append(i)
    for j in keys:
        del(dict[j])
    return dict

del_value(grades, "A")
print(grades)