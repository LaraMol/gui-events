from glob import glob
import tkinter

root = tkinter.Tk()
root.title("Hello")
root.geometry("200x300")
root["background"] = 'pink'
Numbers = 0
Is_up = None 

def on_enter(e):
    root['background'] = 'yellow'

def on_leave(e):
    if Numbers > 0:
        root["background"] = 'green'
    elif Numbers < 0:
        root["background"] = 'red'
    else:
        root["background"] = 'pink'


root.bind("<Enter>", on_enter)
root.bind("<Leave>", on_leave)

def Upbutton(event):
    global Numbers
    global Is_up
    Is_up = True 
    Numbers += 1
    counter['text'] = Numbers
    if Numbers > 0:
        root["background"] = 'green'
    elif Numbers < 0:
        root["background"] = 'red'
    else:
        root["background"] = 'pink'


def Downbutton(event):
    global DOWN
    global Numbers
    global Is_up
    Is_up = False
    Numbers -= 1
    counter['text'] = Numbers
    if Numbers >0:
        root["background"] = 'green'
    elif Numbers <0:
        root["background"] = 'red'
    else:
        root["background"] = 'pink'



def Spacelabel(event):
    global Clickerlabel
    global Numbers
    global DOWNN
    global UP
    global Is_up
    if Is_up == True: 
        Numbers = Numbers * 3
    else: 
        Numbers = Numbers / 3
        Numbers = round((Numbers/3),2)
    counter['text'] = Numbers


def UP():
    global Numbers
    global Is_up
    Is_up = True 
    Numbers += 1
    counter['text'] = Numbers
    if Numbers > 0:
        root["background"] = 'green'
    elif Numbers < 0:
        root["background"] = 'red'
    else:
        root["background"] = 'pink'

def DOWN():
    global Numbers
    global Is_up
    Is_up = False
    Numbers -= 1
    counter['text'] = Numbers
    if Numbers >0:
        root["background"] = 'green'
    elif Numbers <0:
        root["background"] = 'red'
    else:
        root["background"] = 'pink'

def Clickerlabel(event):
    global Numbers
    global DOWNN
    global UP
    global Is_up
    print('event: ' + str(event))
    if Is_up == True: 
        Numbers = Numbers * 3
    else: 
        Numbers = Numbers / 3
        Numbers = round((Numbers/3),2)
    counter['text'] = Numbers




button = tkinter.Button(root)
button.configure(text="UP",command=UP)
button.pack(padx=80, pady=20, expand=True)

button = tkinter.Button(root)
button.configure(text="DOWN",command=DOWN)
button.pack(padx=80, pady=20, expand=True)



counter= tkinter.Label(
    root,
    text= Numbers,
    bg="white",
    fg="black"
    
)


counter.pack(
    ipadx=100,
    ipady=10,
    expand=True,
)

counter.bind('<Double-Button>',Clickerlabel)
root.bind('+', Upbutton)
root.bind('-', Downbutton)
root.bind('<space>', Spacelabel )

root.mainloop()