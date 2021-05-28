import pyperclip as pc
import classes as cl
import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
root.title("DSランダムコード生成")


def butclick():
    DSc = cl.randkotei()
    lis = []
    inp_cnt_sei = int(inp_cnt.get())
    inp_str = inp_bit.get()
    if hendou.get():
        pass
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


exp_1 = tk.Label(root,text="コードのビットを入力してください(2=8bit,1=16bit,0=32bit)")
exp_1.grid(row=0,column=0)
inp_bit = tk.Entry(width=1)
inp_bit.grid(row=1,column=0)
exp_2 = tk.Label(root,text="コードの個数を入力してください")
exp_2.grid(row=2,column=0)
inp_cnt = tk.Entry(width=3)
inp_cnt.grid(row=3,column=0)
but = tk.Button(root,text="コード生成",command=butclick)
but.grid(row=4,column=0)
hendou = tk.Checkbutton(root,text="アドレス範囲変更")
hendou.grid(row=5,column=0)

root.mainloop()




    