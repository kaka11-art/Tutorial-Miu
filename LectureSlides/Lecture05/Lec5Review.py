# # Construction Tuples
# Alice = (20, "Computer science", "Imperial")
# Bob = (18, "Biology")

# # Index to get the position value
# print(Alice[1])

# # Concat
# people = Alice + Bob 
# print(people)

# # Length gives the number of element 
# print(len(people))

# # Immutable: cannot change the value (string & tuples)
# # Alice[1] = "Mathematics"

# def quotient_and_remainder(x, y):
#     q = x // y 
#     r = x % y
#     # Return a tuple
#     return (q, r)

# (quot, rem) = quotient_and_remainder(13, 3)
# print(quot)
# print(rem)

# aTuple = ((3, "abc"), (4, "bc"), (6, "abc"), (13, "cd"))

# def get_data(aTuple):
#     nums = ()
#     words = ()
#     for t in aTuple:
#         print("Current element is:", t)
#         nums = nums + (t[0],)
#         if t[1] not in words:
#             # t[1] = "cd"
#             # words = ("abc", "bc", ...)
#             words = words + (t[1],)
#     min_n = min(nums)
#     max_n = max(nums)
#     unique_words = len(words)
#     return (min_n, max_n, unique_words)

# (mininum_n, maximum_n, num_words) = get_data(aTuple)

# # List Construction
# L1 = [2, 'a', 4, [1,2]]

# # Length of a List
# print(len(L1))
# print(len(L1[3]))

# # List is mutable
# L1[0] += 1 
# L1[1] = "You are a list"
# print(L1)

# nums = [3, 5, 1, 2, 6]

# total1 = 0 
# for i in range(len(nums)):
#     print("In index iteration, i =", i)
#     total1 += nums[i]
# print(total1)

# total2 = 0 
# for i in nums:
#     print("In element iteration, i=", i)
#     total2 += i 
# print(total2)

# L = [2, 1, 3]
# a = L.append(5)
# b = L.extend([6,0])

# print(a, b)

# # No duplication element in set
# def set_append(set, element):
#     if element not in set:
#         set.append(element)
#     return set 

# set = []
# set_append(set, 3)
# print(set)
# set_append(set, 4)
# print(set)
# set_append(set, 5)
# print(set)
# set_append(set, 3)
# print(set)
# set_append(set, 4)
# print(set)

# L = [2, 1, 3, 6, 3, 7, 0, 3]
# # # del(L[4]) # acting with index

# # L.remove(3) # acting with element
# # print(L)
# # L.remove(3)
# # print(L)

# a1 = L.pop()
# print(L, a1)
# a1 = L.pop()
# print(L, a1)
# a1 = L.pop()
# print(L, a1)
# a1 = L.pop()
# print(L, a1)


# L = [3, 5, 1, 2]
# a = L.remove(3)
# print(a)
# print(L)

# b = L.append(3)
# print(b)


# L = [3, 5, 1, 2]
# a = L.pop()
# print("L is", L)
# print("pop() is", a)


# # From smaller to bigger
# def bubble_sort(L):
#     for j in range(len(L)):
#         for i in range(len(L) - 1 - j):
#             if L[i] > L[i + 1]:
#                 # tmp = L[i + 1]
#                 # L[i + 1] = L[i]
#                 # L[i] = tmp
#                 L[i], L[i + 1] = L[i + 1], L[i] 
#                 print(L)
#     return L

# L = [9, 5, 6, 0, 4, 1, 3, 2]
# print(bubble_sort(L))


a = 1 
b = a 
a = 2
print(a, b)