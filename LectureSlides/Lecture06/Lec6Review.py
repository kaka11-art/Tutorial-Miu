def factorial(n):
    """
    Factorial: n * (n - 1) * (n - 2) * ... * 2 * 1
    e.g., factorial(3) = 3 * 2 * 1
          factorial(6) = 6 * 5 * 4 * 3 * 2 * 1
    """
    ans = 1
    for i in range(1, n + 1):
        ans *= i 
    return ans 

# print(factorial(1))
# print(factorial(5))

# 6! = 6 * 5!
# n! = n * (n - 1)!
def factorial_recursion(n):
    if (n == 1) or (n == 0):
        return 1
    return n * factorial_recursion(n - 1)

# factorial_recursion(3)
# = 3 * factorial_recursion(2)
# = 3 * 2 * factorial_recursion(1)
# = 3 * 2 * 1

# proof: base case (e.g., 1)
# proof: if n is correct, then we need to show that n + 1 is correct


# Fibbonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21,...
# The nth term is the sum of (n - 1)th term and (n - 2)th
def fib_recursion(n):
    if (n == 1) or (n == 2):
        return 1 
    return fib_recursion(n - 1) + fib_recursion(n - 2)

print(fib_recursion(7))
# fib(7) 
# = fib(6) + fib(5)
# = (fib(5) + fib(4)) + (fib(4) + fib(3))
# = ...
# = 

print(fib_recursion(8))


def mult(a, b):
    ans = 0
    for i in range(1, b + 1):
        ans += a 
    return ans