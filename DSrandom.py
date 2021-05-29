import pyperclip as pc
import classes as cl
import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
root.title("DSランダムコード生成")
hantei_1 = tk.BooleanVar()
hantei_1.set(False)

def butclick():
    inp_st_hex = "0x"+inp_st.get()
    inp_en_hex = "0x"+inp_en.get()
    DSc = cl.rand(inp_st_hex,inp_en_hex)
    lis = []
    inp_cnt_sei = int(inp_cnt.get())
    inp_str = inp_bit.get()
    if hantei_1.get():
        if inp_str == "2":
            for _ in range(inp_cnt_sei):
                lis.append(inp_str + DSc.rand8bit())
            lis.sort()
            c_text = "\n".join(lis)
            pc.copy(c_text)
        elif inp_str == "1":
            for _ in range(inp_cnt_sei):
                lis.append(inp_str + DSc.rand16bit())
            lis.sort()
            c_text = "\n".join(lis)
            pc.copy(c_text)
        else:
            for _ in range(inp_cnt_sei):
                lis.append(inp_str + DSc.rand32bit())
            lis.sort()
            c_text = "\n".join(lis)
            pc.copy(c_text)
    else:
        if inp_str == "2":
            for _ in range(inp_cnt_sei):
                lis.append(inp_str + DSc.rand8bit())
            lis.sort()
            c_text = "\n".join(lis)
            pc.copy(c_text)
        elif inp_str == "1":
            for _ in range(inp_cnt_sei):
                lis.append(inp_str + DSc.rand16bit())
            lis.sort()
            c_text = "\n".join(lis)
            pc.copy(c_text)
        else:
            for _ in range(inp_cnt_sei):
                lis.append(inp_str + DSc.rand32bit())
            lis.sort()
            c_text = "\n".join(lis)
            pc.copy(c_text)

#bit
exp_1 = tk.Label(root,text="コードのビットを入力してください(2=8bit,1=16bit,0=32bit)")
exp_1.grid(row=0,column=0)
inp_bit = tk.Entry(width=1)
inp_bit.grid(row=1,column=0)
#count
exp_2 = tk.Label(root,text="コードの個数を入力してください")
exp_2.grid(row=2,column=0)
inp_cnt = tk.Entry(width=3)
inp_cnt.grid(row=3,column=0)
#addresschange
exp_3 = tk.Label(root,text="アドレス開始範囲")
exp_3.grid(row=5,column=0)
inp_st = tk.Entry(width=7)
inp_st.insert(tk.END,"2000000")
inp_st.grid(row=6,column=0)
exp_4 = tk.Label(root,text="アドレス終了範囲")
exp_4.grid(row=7,column=0)
inp_en = tk.Entry(width=7)
inp_en.insert(tk.END,"23FFFFF")
inp_en.grid(row=8,column=0)
#seisei
but = tk.Button(root,text="コード生成",command=butclick)
but.grid(row=9,column=0)
root.mainloop()




    