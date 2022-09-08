#1
a = int(input('Enter 1st groups: '))
b = int(input('Enter 2st gropus: '))
c = int(input('Enter 3st groups: '))

print(f'Need table for 1st class {int(a / 2)}')
print(f'Need table for 2st class {int(b / 2)}')
print(f'Need table for 3st class {int(c / 2)}')

#2
x = int(input('Enter 1st position: '))
y = int(input('Enter 2st position: '))

if x > 0 and x < 9 and y > 0 and y < 9:
    print(f'Ladiya here {x},{y} ')

    print('Enter pls')
    x2 = int(input('Enter 1st move position: '))
    y2 = int(input('Enter 3st move position: '))

    if x2 > 0 and x2 < 9 and y2 > 0 and y2 < 9:
        if x2 == x or y2 == y:
            print('YES')
        else:
            print('NO')
    else:
        print('Error')
else:
    print('Error')
