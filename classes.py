import random as ra

class rand:

    def __init__(self,st,en):
        self.st = st
        self.en = en

    def rand8bit(self):
        i_a,i_b = int(self.st,base=16),int(self.en,base=16)
        adhani = ra.randint(i_a,i_b)
        cdhani = ra.randint(0,255)
        adh = hex(adhani)
        cdh = hex(cdhani)
        return adh[2:] +" "+cdh[2:].zfill(8)

    def rand16bit(self):
        i_a,i_b = int(self.st,base=16),int(self.en,base=16)
        adhani = ra.randint(i_a,i_b)
        cdhani = ra.randint(0,65535)
        adh = hex(adhani)
        cdh = hex(cdhani)
        return adh[2:] +" "+cdh[2:].zfill(8)

    def rand32bit(self):
        i_a,i_b = int(self.st,base=16),int(self.en,base=16)
        adhani = ra.randint(i_a,i_b)
        cdhani = ra.randint(0,4294967295)
        adh = hex(adhani)
        cdh = hex(cdhani)
        return adh[2:] +" "+cdh[2:].zfill(8)