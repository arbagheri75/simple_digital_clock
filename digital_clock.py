from tkinter import *
from time import strftime

def time():
    string = strftime('%H:%M:%S  %p')
    label_time.config(text=string)
    label_time.after(1000, time)
    

window = Tk()
window.title('digital clock')

label_time = Label(window, background='purple',
                   foreground='white',
                   font=('calibri', 40, 'bold'))
label_time.pack()

time()
window.mainloop()