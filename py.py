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
xpos = int(input('Where do you want x to be(enter pos 1, 2 or 3):\n'))

print('a = ' + str(a) + ', b = ' + str(b))
char = random.randint(0,1)
if char == '1':
    if str(xpos) == '1':
        x = int(b)-int(a)
        print('x' +'+'+ str(a) +'=' + str(b))
        print('x' + '=' + str(b) + '-' + str(a))
        print('x' + '=' + str(x))
    elif str(xpos) == '2':
        x = int(b)-int(a)
        print(str(a) +'+x' +'=' + str(b))
        print('x' + '=' + str(b) + '-' + str(a))
        print('x' + '=' + str(x))
    elif str(xpos) == '3':
        x = int(a) + int(b)
        print(str(a) + '+' + str(b) + '=' + 'x')
        print('x' + '=' + str(x))
            
else:
    if str(xpos) == '1':
        x = a+b
        print('x' +'-'+ str(a) +'=' + str(b))
        print('x' + '=' + str(b) + '+' + str(a))
        print('x' + '=' + str(x))
    elif str(xpos)== '2':
        x = -(int(b)-int(a))
        print(str(a) +'-x' +'=' + str(b))
        print('-x' + '=' + str(b) + '-' + str(a))
        print('x' + '=' + str(x))
    elif str(xpos)== '3':
        x = int(a) - int(b)
        print(str(a) + '-' + str(b) + '=' + 'x')
        print('x' + '=' + str(x))

