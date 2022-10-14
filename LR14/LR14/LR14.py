#5
import tkinter
import math

def calc():
    b = txt1.get()
    if b.isdigit():
        b = int(txt1.get())
        numb.set(4/3 * math.pi * b * b * b)
    else:
        numb.set('Ошибка!')

def click():
    a = txt2.get()
    if variable.get() == 'txt':
        label3.config(text = "Сохранено")
        f = open('TextTXT.txt','w+')
        f.write(a)
        f.close()
    elif variable.get() == 'HTML':
        label3.config(text = "Сохранено")
        f = open('TextHTML.html','w+')
        f.write(a)
        f.close()
    else:
        label3.config(text = "Выберите формат!")

OptionList = ["Выпадающий список","txt","HTML"]

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

variable = tkinter.StringVar(frame)
variable.set(OptionList[0])

opt = tkinter.OptionMenu(frame, variable, *OptionList)

numb = tkinter.IntVar()
label1 = tkinter.Label(frame, text = 'Введите радиус:')
label2 = tkinter.Label(frame, text = 'Результат вычислений:')
label3 = tkinter.Label(frame)
label4 = tkinter.Label(frame)
label5 = tkinter.Label(frame)
txt1 = tkinter.Entry(frame)
txt2 = tkinter.Entry(frame, textvariable = numb)
button1 = tkinter.Button(frame, text = 'Вычислить', command = calc)
button2 = tkinter.Button(frame, text = 'Сохранить', command = click)

label1.grid(row=0,column=1)
txt1.grid(row=0,column=2)
label2.grid(row=1,column=1)
txt2.grid(row=1,column=2)
label4.grid(row=2,column=2)
label5.grid(row=3,column=2)
button1.place(x=115,y=50)
button2.grid(row=4,column=1)
opt.grid(row=4,column=2)

window.mainloop()

#3
import tkinter

def click():
    a = txt.get()
    if variable.get() == 'txt':
        label2.config(text = "Сохранено")
        f = open('TextTXT.txt','w+')
        f.write(a)
        f.close()
    elif variable.get() == 'HTML':
        label2.config(text = "Сохранено")
        f = open('TextHTML.html','w+')
        f.write(a)
        f.close()
    else:
        label2.config(text = "Выберите формат!")

OptionList = ["Выпадающий список","txt","HTML"]

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

variable = tkinter.StringVar(frame)
variable.set(OptionList[0])

opt = tkinter.OptionMenu(frame, variable, *OptionList)

label1 = tkinter.Label(frame, text = 'Введите текст:')
label2 = tkinter.Label(frame)
txt = tkinter.Entry(frame)
button = tkinter.Button(frame, text='Сохранить', command = click)

label1.pack()
txt.pack()
label2.pack()
button.pack(side = 'left')
opt.pack(side = 'right')

window.mainloop()

#2
import tkinter
import random

def random_word():
    word = random.choice(list(dict.keys()))
    label2.config(text=word)
    label3.config(text='')
    return word

def click():
    a = txt.get()
    if dict[label2.cget('text')] == a:
        result='Верно'
        word=random.choice(list(dict.keys()))
        label2.config(text=word)
    else:
        result = 'Непраильно'
        click.invocations-=1
        label4.config(text = f'Попыток: {click.invocations}.')
        if click.invocations==0:
            result = 'Мда'
            window.quit()
    label3.configure(text = result)

dict = {'Гуль':'ghoul', 'Печенье':'cookie', 'Яблоко':'apple', 'Лемон':'lemon', 'Поезд':'train', 'Тетрадь':'notebook', 'Кубай':'kubai'}
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
label1 = tkinter.Label(frame, text = 'Переведите слово:')
label2 = tkinter.Label(frame)
label3 = tkinter.Label(frame)
label4 = tkinter.Label(frame)
txt = tkinter.Entry(frame)

random_word()
 
label1.pack()
label2.pack()
txt.pack()
label3.pack()
label4.config(text = 'Попыток: 3')
label4.pack()
 
click.invocations=3
 
button1 = tkinter.Button(frame, text = "Ввести", command = click)
button1.pack()
button2 = tkinter.Button(frame, text = "Другое слово", command = random_word)
button2.pack()
window.mainloop()

#1
import tkinter

def click():
   forengeit.set(((5/9 * (float(entry.get())-32))))

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
test = tkinter.Label(frame, text='Перевод температуры из Форенгейтп в Цельсию')
test.pack()
forengeit = tkinter.IntVar()
entry = tkinter.Entry(frame)
entry.pack()
label = tkinter.Label(frame, textvariable=forengeit)
label.pack()
button = tkinter.Button(frame, text='Convert', command=click)
button.pack()
window.mainloop()
