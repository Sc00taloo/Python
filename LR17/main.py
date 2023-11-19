import matplotlib.pyplot as plt
import math

flag = False
while flag == False:
    try:
        a = int(input("Enter a: "))
        flag = True
    except ValueError:
        print("Введите число")

flag = False
while flag == False:
    try:
        b = int(input("Enter b: "))
        n = 1 / b
        flag = True
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except ValueError:
        print("Введите число")

x = []
y = []
i = 0.25
while i <= 2:
    x.append(i)
    i = i + 0.05

minNum = a * math.sin(x[0]/b)
maxNum = a * math.sin(x[0]/b)
j = 1
x0, xn = 0.25, 0
for j in range(len(x)):
    y.append(a * math.sin(x[j]/b))
    if minNum > y[j]:
        minNum = y[j]
        x0 = x[j]
    if maxNum < y[j]:
        maxNum = y[j]
        xn = x[j]

#print(minNum, maxNum)
#print(x0, xn)
X0 = [x0, x0]
Y0 = [0, minNum]
XN = [xn, xn]
YN = [0, maxNum]
X00 = [0, x0]
Y00 = [minNum, minNum]
X11 = [0, xn]
Y11 = [maxNum, maxNum]
plt.plot(x,y)
plt.plot(X0, Y0, "--", color='green')
plt.plot(XN, YN, "--", color='green')
plt.plot(X00, Y00, "--", color='yellow')
plt.plot(X11, Y11, "--", color='yellow')
plt.show()

