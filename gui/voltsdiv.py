import Tkinter as tk
import ttk

class VoltsDiv(object):
    def __init__(self, window, instr):
        self.window = window
        self.instr = instr
        values = (0.2, 0.5, 1, 2, 5, 10, 20, 50)
        self.combobox = ttk.Combobox(self.window, values=values)
        self.combobox.pack()
        self.combobox.bind('<<ComboboxSelected>>', self.on_select)

    def on_select(self, event):
        selection = self.combobox.get()
        self.instr.set_vdiv(1, float(selection), 10)