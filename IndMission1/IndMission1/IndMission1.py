f = open("10a.txt","r")
n = int(f.read(3))
k = int(f.read(3))
d = int(f.read(3))
f.read(1)
print(n,k,d)
test =[]
tes1 =[]
for numbers in f:
    test.append(int(numbers))

for num in test:
    if num < 0:
        num *= -1
        numb = ""
        while num > 0:
            numb += str(num % 3)
            num//=3
        print(numb[::-1])
        sum = 0
        mult = 1
        while int(numb) > 0:
            digit = int(numb) % 10
            sum = sum + digit
            mult = mult  * digit
            int(numb) = int(numb) // 10
        if sum == 12:
            test1.append(int(sum,3) * -1)

print(test1)

f.close()
