import tkinter

widget = tkinter.Tk()

def hello(event):
    print ('Double Click to exit')

def quit(event):       
    print ('You double clicked...')     
    import sys; sys.exit() 


button = tkinter.Button(widget)
button.configure(text="Hello event world",)
button.pack(padx=80, pady=20, expand=True)
widget.bind('<Button-1>', hello)             
widget.bind('<Double-1>', quit)              
widget.mainloop()