from barghii import Barghii

class labtop():
    def __init__(self, name, price, voltage, cpu, ram):
        self.name = name
        self.price = price
        self.voltage = voltage
        self.cpu = cpu
        self.ram = ram

@property
def cpu(self):
    return self._cpu
@cpu.setter
def cpu(self,cpu):
    self._cpu=cpu
@property
def ram(self):
    return self._ram
@ram.setter
def ram(self,ram):
    self._ram=ram


