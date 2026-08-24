cube = 27
#cube = 8120601
#cube = 10000
epsilon = 0.1
guess = 0.0
increment = 0.01
num_guesses = 0
# look for close enough answer and make sure
# didn't accidentally skip the close enough bound
while abs(guess**3 - cube) >= epsilon and guess <= cube:
   guess += increment
   num_guesses += 1
print('Linear approxiation has num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
   print('Failed on cube root of', cube, "with these parameters.")
else:
   print(guess, 'is close to the cube root of', cube)

cube = 27
#cube = 8120601
# won't work with x < 1 because initial upper bound is less than ans
#cube = 0.25
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
   if guess**3 < cube:
       # look only in upper half search space
       low = guess
   else:
       # look only in lower half search space
       high = guess
   # next guess is halfway in search space
   guess = (high + low)/2.0
   num_guesses += 1
print('Bisection approxiation has num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)