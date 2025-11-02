N = int(input("give me a positive integer:"))
guess = 0
increase = 1
epsilon = 0.01
while abs(guess**3 - N) > epsilon:
    guess += increase
    if guess**3 > N:
        print(f'error,{N} is not a perfect cube')
        break
print(guess)    
         
