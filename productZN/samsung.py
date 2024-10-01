from mobile import Mobile

class Samsung():
    def __init__(self,name, price, voltage, pagesize, fold):
        self.name = name
        self.price = price
        self.voltage = voltage
        self.pagesize = pagesize
        self.fold=fold


@property
def fold(self):
    return self._fold
@fold.setter
def folding(self,fold):
    self._fold = fold
