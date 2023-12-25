import matplotlib.pyplot as plt
import math
import numpy as np

flag = True
while flag:
    try:
        a = int(input("Enter a: "))
        flag = False
    except ValueError:
        print("Введите число")

flag = True
while flag:
    try:
        b = int(input("Enter b: "))
        n = 1 / b
        flag = False
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

fig, axs = plt.subplots(nrows= 1, ncols= 1)
x = np.linspace(-7, 7, 10000)
yblue = 2*np.sqrt((-abs(abs(x)-1))*abs(3-abs(x))/((abs(x)-1)*(3-abs(x))))*(1+abs(abs(x)-3)/(abs(x)-3))*np.sqrt(1-(x/7)**2)+(5+0.97*(abs(x-0.5)+abs(x+0.5))-3*(abs(x-0.75)+abs(x+0.75)))*(1+abs(1-abs(x))/(1-abs(x)))
#print(yblue)
ygreen = (2.71052+1.5-0.5*np.abs(x)-1.35526*np.sqrt(4-(np.abs(x)-1)**2))*np.sqrt(abs(abs(x)-1)/(abs(x)-1))+0.9
#print(ygreen)
yred = (-3)*np.sqrt(1-(x/7)**2)*np.sqrt(abs(abs(x)-4)/(abs(x)-4))
#print(yred)
yorange = np.abs(x/2)-0.0913722*x**2-3+np.sqrt(1-(np.abs(abs(x)-2)-1)**2)
#print(yorange)
plt.plot(x, yblue, color='blue')
plt.plot(x, ygreen, color='green')
plt.plot(x, yred, color='red')
plt.plot(x, yorange, color='orange')
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.show()


