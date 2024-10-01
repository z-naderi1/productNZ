from barghii import Barghii

class Mobile():
    def __init__(self,name, price, voltage, pagesize):
        self.name = name
        self.price = price
        self.voltage = voltage
        self.pagesize = pagesize
@property
def pagesize(self):
    return self.__pagesize
@pagesize.setter
def pagesize(self,pagesize):
    self.__pagesize = pagesize


