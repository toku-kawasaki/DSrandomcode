import random as ra
import pyperclip as pc

class randode:
    a = "0x2000000"
    b = "0x23FFFFF"
    def rand8bit(self):
        i_a,i_b = int(self.a,base=16),int(self.b,base=16)
        adhani = ra.randint(i_a,i_b)
        cdhani = ra.randint(0,255)
        adh = hex(adhani)
        cdh = hex(cdhani)
        return adh[2:] +" "+cdh[2:].zfill(8)

    def rand16bit(self):
        i_a,i_b = int(self.a,base=16),int(self.b,base=16)
        adhani = ra.randint(i_a,i_b)
        cdhani = ra.randint(0,65535)
        adh = hex(adhani)
        cdh = hex(cdhani)
        return adh[2:] +" "+cdh[2:].zfill(8)

    def rand32bit(self):
        i_a,i_b = int(self.a,base=16),int(self.b,base=16)
        adhani = ra.randint(i_a,i_b)
        cdhani = ra.randint(0,4294967295)
        adh = hex(adhani)
        cdh = hex(cdhani)
        return adh[2:] +" "+cdh[2:].zfill(8)

DSc = randode()
lis = []
inp_bit = input("コードのビットを入力してください(2=8bit,1=16bit,0=32bit)：")
inp_cnt = int(input("コードの範囲を入力してください："))

if inp_bit == "2":
    for _ in range(inp_cnt):
        lis.append(inp_bit + DSc.rand8bit())
    lis.sort()
    c_text = "\n".join(lis)
    pc.copy(c_text)
elif inp_bit == "1":
    for _ in range(inp_cnt):
        lis.append(inp_bit + DSc.rand16bit())
    lis.sort()
    c_text = "\n".join(lis)
    pc.copy(c_text)
else:
    for _ in range(inp_cnt):
        lis.append(inp_bit + DSc.rand32bit())
    lis.sort()
    c_text = "\n".join(lis)
    pc.copy(c_text)





    