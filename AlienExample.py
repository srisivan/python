from tkinter import *
window = Tk()
window.title('Alien')
c = Canvas(window, height = 400, width = 500)
c.pack()

body = c.create_oval( 100, 150, 300, 250, fill = 'green')
eye = c.create_oval(170, 70, 230, 130, fill = 'white')
eyeball = c.create_oval(190, 90, 210, 110, fill = 'black')
neck = c.create_line(200, 150, 200, 130)
mouth = c.create_oval(150, 220, 250, 240, fill = 'red')
hat = c.create_polygon(180, 75, 220, 75, 200, 20, fill = 'blue')


def mouth_open(event):
    c.itemconfig(mouth, fill = 'white')

def mouth_close(event):
    c.itemconfig(mouth, fill = 'red')

c.bind_all('<KeyPress-m>', mouth_open)
c.bind_all('<KeyPress-a>', mouth_close)



window.attributes('-topmost', 1)

def blink(event):
    c.itemconfig(eye, fill = 'green')
    c.itemconfig(eyeball, state = HIDDEN)

def unblink(event):
    c.itemconfig(eye, fill = 'white')
    c.itemconfig(eyeball, state = NORMAL)

c.bind_all('<KeyPress-b>', blink)
c.bind_all('<KeyPress-o>', unblink)

def eye_control(event):
    key = event.keysym
    if key == "Up":
        c.move(eyeball, 0, -1)
    if key == "Down":
        c.move(eyeball, 0, 1)
    if key == "Left":
        c.move(eyeball, -1, 0)
    if key == "Right":
        c.move(eyeball, 1, 0)

c.bind_all('<Key>', eye_control)


