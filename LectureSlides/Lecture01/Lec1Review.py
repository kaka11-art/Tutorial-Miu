import math

print("代码已启动")
g=float( input("Please input a number: ") )
g_square=g**2 # 4
x=10
count=0
threshold=0.005

# print(((g_square-x)>threshold) or ((g_square-x)<-threshold))

while (((g_square-x)>threshold) or ((g_square-x)<-threshold)):

    print("The current iteration number is: ", count)
    g=(g+x/g)/2
    g_square=g**2
    count = count + 1

    if (((g_square-x)>threshold) or ((g_square-x)<-threshold)):
        print("It is still beyond error:", g)
    else:
        print("Final result:", g)


# while (math.fabs(g_square-x)>threshold):
#     g=(g+x/g)/2
#     g_square=g**2
#     print(g)

# x = x +/-/*// 1
# x += 1
# x -= 1
# x *= 1
# x /= 1