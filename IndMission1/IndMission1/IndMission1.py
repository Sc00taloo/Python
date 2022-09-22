f = open("10a.txt","r")
f2 = open("10b.txt","r")
#n = int(f.read(3))
#k = int(f.read(3))
#d = int(f.read(3))
n = int(f2.read(6))
k = int(f2.read(3))
d = int(f2.read(4))
f.read(1)
print(n,k,d)
test =[]
test1 =[]
for numbers in f2:
    test.append(int(numbers))

count = -1
for num in test:
    count+=1
    if num < 0:
        num1 = num * -1
        numb = 0
        while num1 > 0:
            numb += (num1 % 3)
            num1//=3
        if numb == 12:
            test1.append(count)
test1.append(count)

if (len(test1) % k != 0):
    j = 0
    suma = 0
    count = 0
    suma_max = []
    for num5 in test:
        count += 1
        suma += num5
        if test.index(num5) == test1[j]:
            suma += num5
            count -= 1
            if (count % d == 0):
                suma_max.append(suma)
            count = 0
            j += 1
            suma = 0
else:
    j = 0
    suma = 0
    count = 0
    suma_max = []
    for num5 in test:
        if test.index(num5) != test1[-1]:
            count += 1
            suma += num5
        else:
            break

print(suma)

f.close()
f2.close()