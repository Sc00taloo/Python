def special(x):
    sum = 0
    x1 = abs(x)
    while x1 > 0:
        sum = sum +(x1 % 3)
        x1 = x1 / 3
    return sum

f = open("10a.txt","r")
f2 = open("10b.txt","r")
n = int(f.read(3))
k = int(f.read(3))
d = int(f.read(3))
n1 = int(f2.read(6))
k1 = int(f2.read(3))
d1 = int(f2.read(4))
print(n,k,d)
print(n1,k1,d1)
f.read(1)
maax = -100000000
a = []
a1 = []
for i in f:
    a.append(int(i))
a.append(0)
i = 0
for i in f2:
    a1.append(int(i))
a1.append(0)

f.close()
f2.close()

i = 0
for i in range(n):
    count = 1
    countSpecial = 0
    if special(a[i]) == 12 and a[i] < 0:
        countSpecial = countSpecial + 1
    sum = a[i]
    for j in range(n):
        count = count + 1
        sum = sum + a[j + 1]
        if special(a[j + 1]) == 12 and a[j + 1] < 0:
            countSpecial = countSpecial + 1
        if countSpecial % k == 0 and count % d == 0:
            maax = max(maax,sum)
print(maax)
maax = -100000000
for i in range(n1):
    count = 1
    countSpecial = 0
    if special(a1[i]) == 12 and a1[i] < 0:
        countSpecial = countSpecial + 1
    sum = a1[i]
    for j in range(n1):
        count = count + 1
        sum = sum + a1[j + 1]
        if special(a1[j + 1]) == 12 and a1[j + 1] < 0:
            countSpecial = countSpecial + 1
        if countSpecial % k1 == 0 and count % d1 == 0:
            maax = max(maax,sum)
print(maax)