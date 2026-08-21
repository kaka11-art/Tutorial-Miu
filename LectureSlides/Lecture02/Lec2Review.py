
a, b, = 0, 0

i = 0

while (a < 10):

    # i = 0

    while (b < 50):

        # i = 0 

        b += i 
        i += 1 

        if (i == 5):
            break 
            
    print("Iteration b is fiinished at i: ", i)
    print("Iteration b is fiinished at b: ", b)

    a += i 
    print("Iteration a is finished at a: ", a, "\n")

print("Iteration a is terminate at a/b: ", a, b, "\n")