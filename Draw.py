import tkinter
from math import sin, cos, pi
from tkinter import *
from Josephus import josephus


def start(window, K, Num):

    window.destroy()
    win = Tk()
    win.title("Josephus Problem")
    win.resizable(False, False)
    win.config(bg="white")
    canvas = Canvas(height=400, width=400)
    canvas.config(background="white")
    canvas.pack()

    k = K
    n = Num
    people = []
    deadPeople = []
    a = josephus(n, k)
    for i in range(n):
        people.append(i + 1)

    def draw():
        canvas.delete('all')
        word = people
        n = len(word)
        angle = pi * 2 / n  # need to use radian instead of degree

        if n == 1:
            x = sin(angle * 1) * 90
            y = cos(angle * 1) * 90
            # draw the character
            canvas.create_text(x + 200, y + 200, text=word[0])
            button.pack_forget()
            word = ''.join(str(x) for x in people)
            Label(canvas, width=40, height=5, text="The person at position {} won\'t be killed.".format(
                word), font=('Microsoft YaHei UI Light', 17, 'bold'), foreground="#57a1f8", background="white").pack()

        else:
            points = []  # use to store calculated points
            for i in range(n):
                x = sin(angle * i) * 90
                y = cos(angle * i) * 90
                # draw the character
                # save the points for drawing circles later
                points.append((x, y))

            # calculate the radius of the circles using the first two points
            dx, dy = points[1][0] - points[0][0], points[1][1] - points[0][1]
            r = (dx * dx + dy * dy) ** 0.5 / 2

            # draw the circles
            for x, y in points:
                canvas.create_oval(200 + x - r, 200 + y - r,
                                   200 + x + r, 200 + y + r, fill="#57a1f8")

            for i in range(n):
                x = sin(angle * i) * 90
                y = cos(angle * i) * 90
                # draw the character
                canvas.create_text(
                    x + 200, y + 200, text=word[i], font=('Microsoft YaHei UI Light', 11, 'bold'))

            if n >= 1:
                people.remove(a[0])
                deadPeople.append(a.pop(0))

    button = tkinter.Button(text='draw', height=2, width=69, background="white",
                            border=0, activebackground="white", command=draw)
    button.pack()
    canvas.mainloop()
