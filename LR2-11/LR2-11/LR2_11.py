
#9
n = int(input('Enter row column number: '))
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][n-i-1] = 1
for i in range(n):
    for j in range(n-i, n):
        a[i][j] = 2
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()


#10
n = int(input('Enter list: '))
A = set(range(1, n + 1))
TrueNumbers = A
while True:
    B = input()
    if B == 'HELP':
        break
    B = {int(x) for x in B.split()}
    if len(TrueNumbers) / 2 < len(TrueNumbers & B):
        print('YES')
        TrueNumbers &= B
    else:
        print('NO')
        TrueNumbers &= A - B        
print(' '.join([str(x) for x in sorted(TrueNumbers)]))


#11
X = int(input('Enter number words from a dictionary: '))
Y = {}
for i in range(X):
    word = input()
    test = word.lower()
    if test not in Y:
        Y[test] = set()
    Y[test].add(word)
mistake = 0
print('Enter a sentence: ')
new_word = input().split()
for word in new_word:
    test = word.lower()
    if test in Y and word not in Y[test] or len([i for i in word if i.isupper()]) != 1:
        mistake += 1
print(f'Numbers mistakes: {int(mistake)}')