try:
  from tkinter import *
except:
  from Tkinter import *

import pyperclip as pc

clipboard = []

def copyFromClipboard(txt):
  pc.copy(txt)

def copyToClipboard():
  txt = pc.paste()
  if txt not in clipboard:
    clipboard.insert(0, txt)

def updateClip(frame):
  widgets = frame.winfo_children()

  copyToClipboard()

  diff = len(clipboard) - len(widgets)

  for i in range(diff):
    label = Label(frame,padx=5,pady=10,background="white",text=clipboard[i],relief=RAISED, anchor="w",)
    label.bind("<Button-1>", lambda e, txt = label["text"]: copyFromClipboard(txt))
    label.pack(fill=X)
    frame.pack()
    
  root.after(500, updateClip, frame)