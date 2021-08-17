number = int(input('How many parts do you want your snake shape to be ? '))
for i in range(number):
    if i % 2==1:
        print('#',end='')
    else:
        print('*',end='')