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