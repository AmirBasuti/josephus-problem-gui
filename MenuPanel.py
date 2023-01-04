from tkinter import *
from tkinter import messagebox
import webbrowser
from Draw import start


def on_enter_num(e):
    PeopleNum.delete(0, 'end')


def on_leave_num(e):
    num1 = PeopleNum.get()
    if (num1 == ''):
        PeopleNum.insert(0, 'Enter number of people')


def on_enter(e):
    KNum.delete(0, 'end')


def on_leave(e):
    K1 = KNum.get()
    if (K1 == ""):
        KNum.insert(0, 'Enter K')


def link():
    webbrowser.open_new(r"https://www.geeksforgeeks.org")


def Get_Entry():
    Num = int(PeopleNum.get())
    K = int(KNum.get())
    if (K <= 0 or Num <= 0):
        messagebox.showerror(
            'Josephus Problem', 'Error: K and Number of people must be a positive number.')

    elif (K > Num):
        messagebox.showerror(
            'Josephus Problem', 'Error: K should not be bigger than the number of people, please enter again.')

    elif (K <= Num):
        start(window, K, Num)


window = Tk()
window.title("Josephus Problem")
window.geometry('400x400')
window.config(bg="#fff")
window.resizable(False, False)
icon = PhotoImage(file='image/3097037.png')
window.iconphoto(True, icon)


frame = Frame(window, width=350, height=350, bg="white")
frame.place(x=25, y=25)

heading = Label(frame, text="Enter Numbers", fg="#57a1f8",
                bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=25, y=15)

PeopleNum = Entry(frame, width=25, fg='black', border=0,
                  bg='white', font=('Microsoft YaHei UI Light', 11))
PeopleNum.place(x=30, y=80)
PeopleNum.insert(0, 'Enter number of people')
PeopleNum.bind('<FocusIn>', on_enter_num)
PeopleNum.bind('<FocusOut>', on_leave_num)

Frame(frame, width=295, height=2, bg="#57a1f8").place(x=25, y=107)

KNum = Entry(frame, width=25, fg='black', border=0,
             bg='white', font=('Microsoft YaHei UI Light', 11))
KNum.place(x=30, y=150)
KNum.insert(0, 'Enter K')
KNum.bind('<FocusIn>', on_enter)
KNum.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="#57a1f8").place(x=25, y=177)

Button(frame, width=30, pady=7, text="Start XD", bg="#57a1f8",
       fg='white', border=0, command=Get_Entry).place(x=65, y=230)
label = Label(frame, text="Information about Josephus Problem ",
              fg='black', bg='white', font=('Microsoft YaHei UI Light', 11))
label.place(x=1, y=329)

information = Button(frame, width=8, text="click here", border=0, bg='white', cursor='hand2',
                     fg="#57a1f8", activebackground='white', activeforeground="#57a1f8", command=link)
information.place(x=252, y=333)


window.mainloop()
