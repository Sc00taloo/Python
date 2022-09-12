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
