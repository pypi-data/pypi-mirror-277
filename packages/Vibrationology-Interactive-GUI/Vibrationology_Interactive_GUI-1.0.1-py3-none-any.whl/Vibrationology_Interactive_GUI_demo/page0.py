from matplotlib import rcParams
rcParams['font.family'] = 'Microsoft YaHei'
from tkinter import *


# 主界面
class page_0(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("振动模拟")
        self.createWidget()

    def createWidget(self):
        from . import page1,page2,page3,page4
        lab = Label(self, text="请选择您要进行的模拟", font=("Consolas", 20))
        lab.place(relx=0.28, rely=0.1)
        btn_1 = Button(text="简谐振动", font=("Consolas", 18), width=30,
                       command=lambda: self.master.switch_frame(page1.page_1))
        btn_1.place(relx=0.18, rely=0.24)
        btn_2 = Button(text="非简谐振动", font=("Consolas", 18), width=30,
                       command=lambda: self.master.switch_frame(page2.page_2))
        btn_2.place(relx=0.18, rely=0.38)
        btn_3 = Button(text="傅里叶变换", font=("Consolas", 18), width=30,
                       command=lambda: self.master.switch_frame(page3.page_3))
        btn_3.place(relx=0.18, rely=0.66)
        btn_4 = Button(text="单摆与混沌运动", font=("Consolas", 18), width=30,
                       command=lambda: self.master.switch_frame(page4.page_4))
        btn_4.place(relx=0.18, rely=0.52)
        quitBtn = Button(text="退出", font=("Consolas", 16), command=lambda: self.master.destroy(), width=15)
        quitBtn.place(relx=0.35, rely=0.8)
