from tkinter import *
def motion (event): # a method describing what to do when an event happens
    label1['text']="HH"

WIDTH=200
HEIGHT=100
frame_root=Tk() #create an object of tk frame

canvas=Canvas(frame_root,width=WIDTH, height=HEIGHT) # pass the parameter frame_root into Canvas constructor, meaning putting canvas into frame_root
# canvas are usually used to indicates the size of window, usually not put other widget into it
canvas.pack()

frame=Frame(frame_root, bg='black', )
button1 = Button(frame, text="Hello World!", bg='gray', fg='red') # pass parameter frame in,
# set title, background and forground color (purple words are arguments equivalents to MATLAB's "LineWidth")
button1.bind('<Button-1>', motion) # add event left-click ('<Button-1>') and consequence motion to button1,
button1.pack(side=LEFT) # need to pack the object to make it on the frame

label1=Label(frame, text="Hello")
label1.pack(side=RIGHT)

frame.pack()
frame_root.mainloop()



