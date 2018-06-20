import Tkinter as tk

from siglent import sds1202
from gui import livescreen
from gui import voltsdiv
from gui import instrinfo

class MainWindow(object):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.instr = sds1202.SDS1202("192.168.1.131")
        self.master.title(self.instr.idn)

        self.live_view = livescreen.LiveScreen(self.master, self.instr)
        self.live_view.update_image()

        #self.instr_info = instrinfo.InstrInfo(self.master, self.instr)
        self.volts_div = voltsdiv.VoltsDiv(self.master, self.instr)

    def on_close(self):
        self.live_view.destroy()
        self.master.destroy()


def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()

if __name__ == '__main__':
    main()