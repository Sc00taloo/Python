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

#3 
a = int(input('Enter number: '))
print(a % 10)

#4
a = int(input('Enter number A: '))
b = int(input('Enter number B: '))

if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)

#5
s = input('Enter word with two+ h: ')
e1 = s[:s.find('h')]
e2 = s[s.find('h'):s.rfind('h') + 1]
e3 = s[s.rfind('h') + 1:]
s = e1 + e2[::-1] + e3

print(s)

#6
n = int(input('Enter N: '))
i = 1
while (i ** 2) < n:
    print(i ** 2)
    i += 2

#8
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

a = float(input('Enter a: '))
n = int(input('Enter n: '))
print(f'a^n: {power(a, n)}')