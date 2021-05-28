from tkinter import *
 
from tkinter import messagebox
 
window = Tk()
 
window.title("gt ban than")
 
window.geometry('350x200')
 
def clicked():
 
    messagebox.showinfo('Thong tin', 'Tên: Tran Duc Luong\nMssv: 19575202160020\nĐịa Chỉ: Kỳ tân,Tân kỳ, NA')
 
btn = Button(window,text='Click de xem thong tin', command=clicked)
 
btn.grid(column=0,row=0)
 
window.mainloop()