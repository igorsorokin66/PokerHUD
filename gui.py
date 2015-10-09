__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = ''

import Tkinter
top = Tkinter.Tk()
# Code to add widgets will go here...
B = Tkinter.Button(top, text ="Hello")
#B.pack()
B.grid(row=3,column=2)
top.minsize(width=700, height=500)
top.mainloop()