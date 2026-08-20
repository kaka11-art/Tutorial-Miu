# Comments

# Question 1: 6+4*10
# Answer 1: 46
print("answer_1: 46")

# Question 2: (6+4)*10
# Answer 2: 100
print("answer_2: 100")


#Question 3: 23.0 to the 5th power
#Answer 3: 6436343.0
third_question=float(23.0)
Third_answer=third_question**5
print("answer_3:",Third_answer)


#Question 4: Positive root of the following equation: a. 34*x^2 + 68*x - 510 
#Answer 4: 3.0
forth_a=34
forth_b=68
forth_c=-510
delta=forth_b**2-4*forth_a*forth_c
x_1=(-forth_b+delta**0.5)/(2*forth_a)
x_2=(-forth_b-delta**0.5)/(2*forth_a)
positive_roots = []
if x_1 > 0:
    positive_roots.append(x_1)
if x_2 > 0:
    positive_roots.append(x_2)
print("answer_4:", positive_roots[0] if positive_roots else "No positive roots")


#Question 5: math.cos(3.4)**2+math.sin(3.4)**2 
#Answer 5: 1.0
import math
fifth_question=math.cos(3.4)**2+math.sin(3.4)**2
print("answer_5:",fifth_question)

#Here is something for explore some of the further things for question 4
print("now please enter the a,b,c for the equation ax^2+bx+c=0")
a=float(input("enter a:"))
if a==0:
    print("a cannot be zero for a quadratic equation.Please restart the program and enter a non-zero value for a.")
    exit()
else:
    b=float(input("enter b:"))
    c=float(input("enter c:"))
    delta=b**2-4*a*c
    if delta < 0:
        print("No real roots.")
    else:
        x_1=(-b+delta**0.5)/(2*a)
        x_2=(-b-delta**0.5)/(2*a)
        positive_roots = []
        if x_1 > 0:
            positive_roots.append(x_1)
        if x_2 > 0:
            positive_roots.append(x_2)
        if positive_roots:
            print("Positive root(s):", positive_roots)
        else:
            print("No positive roots.")
