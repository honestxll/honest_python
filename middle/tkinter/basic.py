import tkinter as tk

window = tk.Tk()
window.update()
window.title('My Python GUI')
window.geometry('768x1024')

hit_times = 0
var = tk.StringVar()
var.set('当前点击了 ' + str(hit_times) + ' 次')

label = tk.Label(window, textvariable=var, bg='grey',
                 font=('Arial', 14), width=window.winfo_width(), height=2)
label.pack()

def hit_me():
  global hit_times
  hit_times += 1
  var.set('当前点击了 ' + str(hit_times) + ' 次')

button = tk.Button(window, text='点我看看：）', width=15, height=10, command=hit_me)
button.pack()

window.mainloop()
