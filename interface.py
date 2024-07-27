from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Your vocabulory')
mainframe = ttk.Frame(root, padding='3 3 3 3',width=200,height=200)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S))
feet_entry = ttk.Entry(mainframe, width=5,textvariable='Some text')
feet_entry.grid(column=0,row=1, sticky=(W,E))
word = ttk.Label(mainframe, text='English word')
word.grid(column=0,row=0,sticky=(N, W),padx=5,pady=5)
word_meaning = ttk.Label(mainframe, text='Word meaning')
word_meaning.grid(column=1,row=0,padx=5,pady=5)
word_translation = ttk.Label(mainframe, text='Word translation')
word_translation.grid(column=4,row=0,sticky=(N,E),padx=5,pady=5)
root.mainloop()