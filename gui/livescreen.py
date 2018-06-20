import Tkinter as tk
from threading import Thread
import Queue
from PIL import ImageTk, Image
import io

class LiveScreen(object):
    def __init__(self, window, instr):
        self.window = window
        self.instr = instr
        self.frames = Queue.Queue()

        self.panel = tk.Label(self.window)
        self.panel.pack(side = "bottom", fill = "both", expand = "yes")

        self.poller = Thread(target=self._poll_images)
        self.alive = True
        self.poller.start()

    def update_image(self):
        try:
            frame = ImageTk.PhotoImage(self.frames.get_nowait())
            self.panel.configure(image=frame)
            self.panel.image = frame
        except Queue.Empty:
            pass
        finally:
            self.panel.after(50, self.update_image)

    def destroy(self):
        self.alive = False

    def _poll_images(self):
        while self.alive:
            img = Image.open(io.BytesIO(self.instr.read_image()))
            self.frames.put(img)