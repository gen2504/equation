import random
inp = int(input('How much arguments do you want to input?(0,1 or 2)\n'))
if inp == 0:
    a = random.randint(1,100)
    b = random.randint(1,100)
elif inp == 1:
    a = int(input('Enter argument: '))
    b = random.randint(1,100)
elif inp == 2:
    a = int(input('Enter first argument: '))
    b = int(input('Enter second argument: '))
xpos = int(input('Where do you want x to be(enter pos 1, 2 or 3):\n')

print('a = ' + str(a) + ', b = ' + str(b))
char = random.randint(0,1)
if char == '1':
        if xpos == '1':
            x = b-a
            print('x' + a +'=' + b)
        if xpos == '2':
            x = b-a
            print('a' + 'x' +'=' + b)
        elif xpos == '3':
            x = b+a
            print(a + '+' + b + '=' + 'x')
             
    print(str(a) + '+' + str(b) + '=' + str(c))
else:
    c = a-b
    print(str(a) + '-' + str(b) + '=' + str(c))

