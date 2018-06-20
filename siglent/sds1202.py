from threading import Lock
import vxi11

from scope import BaseScope

class SDS1202(BaseScope):
    def __init__(self, uri):
        self.instr = vxi11.Instrument(uri)
        self.idn = self.instr.ask("*IDN?")
        self.mutex = Lock()
        pass

    def read_image(self):
        self.mutex.acquire()
        self.instr.write("SCDP")
        img = self.instr.read_raw()
        self.mutex.release()
        return img

    def set_vdiv(self, channel, vdiv, probe):
        self.mutex.acquire()
        vdiv = vdiv / float(probe)
        self.instr.write("C{0}:Volt_DIV {1:.2f}V".format(channel, vdiv))
        self.mutex.release()