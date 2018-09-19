import tkinter as tk

window = tk.Tk()
window.title('获取输入框的内容')
window.geometry('1024x768')

e = tk.Entry(window, show='*')
e.pack()


def insert():
    var = e.get()
    text.insert('insert', var)


def end():
    var = e.get()
    text.insert('end', var)


def clear():
    text.delete(0.0, tk.END)


text = tk.Text(window)
insertButton = tk.Button(window, text='insert point', command=insert)
endButton = tk.Button(window, text='end point', command=end)
clearButton = tk.Button(window, text='clear point', command=clear)

text.pack()
insertButton.pack()
endButton.pack()
clearButton.pack()


window.mainloop()
