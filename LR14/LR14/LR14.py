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
