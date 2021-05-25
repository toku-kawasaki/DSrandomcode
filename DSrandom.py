import pyperclip as pc
import classes as cl

DSc = cl.randode()
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





    