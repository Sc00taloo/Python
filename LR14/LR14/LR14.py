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
