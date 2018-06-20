import Tkinter as tk
import ttk

class InstrInfo(object):
    def __init__(self, window, instr):
        self.window = window
        self.instr = instr
        w = tk.Label(self.window, text=self.instr.idn)
        w.pack()
