my_str = input('Let\'s talk :')
result = ''
for i in range(0,len(my_str)):
    if i % 2 == 0:
        result += my_str[i]
print(result) 
