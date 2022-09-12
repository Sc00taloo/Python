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
X = int(input())
Y = {}
for i in range(X):
    Line = input().split()
    for Word in Line:
        Y[Word] = Y.get(Word, 0) + 1
MaxValue = max(Y.values())
Freq = [k for k, prov in Y.items() if prov == MaxValue]
print(min(Freq))
