print("代码已启动")
g=2
g_square=g**2
x=10
count=0
threshold=0.005
while (((g_square-x)>threshold) or ((g_square-x)<-threshold)):
    if (((g_square-x)>threshold) or ((g_square-x)<-threshold)):
        g=(g+x/g)/2
        g_square=g**2
    else:
        print(g)