N = int(input("give me a integer:"))
count = 0
high = 1000
low = 0
answer = (high+low) / 2
while answer != N:
    count += 1
    if answer > N:
        high = answer
    else:
        low = answer
    answer = (high + low) / 2
print(answer)
print(count) 
