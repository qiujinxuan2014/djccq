import tkinter
import json
import time
from tkinter import ttk
from tkinter import messagebox
import random
import pygame
achievement1=0
achievement2=0
achievement3=0
achievement4=0
achievement5=0
backpack=[]
money=16
level=["","普通","罕见","稀有","史诗","传奇","神话","究极","超级"]
err=["没有该等级","背包里无该等级的物品","合成禁止使用超级"]
fun0=0
fun1=0
def f0(event):
    l0.destroy()
    l1=tkinter.Label(tk,text="大甲虫传奇",font=("",30))
    l1.pack()
    b0=tkinter.ttk.Button(tk,text="商店",command=f8)
    b0.pack()
    b1=tkinter.ttk.Button(tk,text="图鉴",command=f6)
    b1.pack()
    b3=tkinter.ttk.Button(tk,text="成就",command=f1)
    b3.pack()
    b4=tkinter.ttk.Button(tk,text="合成",command=f5)
    b4.pack()
    b5=tkinter.ttk.Button(tk,text="新手教程",command=f2)
    b5.pack()
    b6=tkinter.ttk.Button(tk,text="背包",command=f7)
    b6.pack()
    b26=tkinter.ttk.Button(tk,text="抽奖",command=f26)
    b26.pack()
    tk.geometry("500x500")
def f1():
    ctk1=tkinter.Toplevel(tk)
    ctk1.title("成就 - 大甲虫传奇")
    l2=tkinter.Label(ctk1,text="不错！学会了吧\n获得方式：完成新手教程",bg="lightgreen",font=("",15),width=50)
    l2.pack()
    l3=tkinter.Label(ctk1,text="孵蛋能手\n获得方式：孵化普通等级的蛋",bg="lightgreen",font=("",15),width=50)
    l3.pack()
    l4=tkinter.Label(ctk1,text="孵蛋能手\n获得方式：孵化罕见等级的蛋",bg="yellow",font=("",15),width=50)
    l4.pack()
    l9=tkinter.Label(ctk1,text="手欠\n获得方式：？？？",bg="yellow",font=("",15),width=50)
    l9.pack()
    l16=tkinter.Label(ctk1,text="我怎么没想到\n获得方式：找到系统的 Bug",bg="blue",font=("",15),width=50)
    l16.pack()
    l7=tkinter.Label(ctk1,text="已获得",font=("",15))
    l7.pack()
    global achievement1,achievement2,achievement3
    if achievement1:
        l8=tkinter.Label(ctk1,text="不错！学会了吧\n获得方式：完成新手教程 已获得",bg="gray",font=("",15),width=50)
        l8.pack()
    if achievement2:
        l10=tkinter.Label(ctk1,text="手欠\n获得方式：在新手教程中再点一下蛋 已获得",bg="gray",font=("",15),width=50)
        l10.pack()
    if achievement3:
        l17=tkinter.Label(ctk1,text="我怎么没想到\n获得方式：找到系统的 Bug 已获得",bg="gray",font=("",15),width=50)
        l17.pack()
    if achievement4:
        l19=tkinter.Label(ctk1,text="孵蛋能手\n获得方式：孵化普通等级的蛋 已获得",bg="gray",font=("",15),width=50)
        l19.pack()
    if achievement5:
        l20=tkinter.Label(ctk1,text="孵蛋能手\n获得方式：孵化罕见等级的蛋 已获得",bg="gray",font=("",15),width=50)
        l20.pack()
def f2():
    ctk2=tkinter.Toplevel(tk)
    ctk2.title("新手教程 - 大甲虫传奇")
    global i1
    i1=tkinter.PhotoImage(file=".\\homebeettle.png")
    global l5,l6
    l5=tkinter.Label(ctk2,image=i1)
    l5.pack()
    l5.bind("<Button-1>",f3)
    l6=tkinter.Label(ctk2,text="点击下甲虫可以生蛋")
    l6.pack()
def f3(event):
    global l5,i2,l6
    l6.config(text="已完成")
    i2=tkinter.PhotoImage(file=".\\illustration\\egg1.png")
    l5.config(image=i2)
    global achievement1,backpack
    if not achievement1:
        backpack.append("egg1")
        achievement1=True
        tkinter.messagebox.showinfo("获得成就","获得成就 不错！学会了吧")
    l5.bind("<Button-1>",f4)
def f4(event):
    global achievement2
    if not achievement2:
        achievement2=1
        tkinter.messagebox.showinfo("获得成就","获得成就 手欠")
def f5():
    global e1,cv1,r0,r1,ctk3
    ctk3=tkinter.Toplevel(tk)
    ctk3.title("合成 - 大甲虫传奇")
    ctk3.geometry("500x300")
    cv1=tkinter.Canvas(ctk3,width=500,height=300,bg="orange")
    r0=cv1.create_rectangle(50,20,133,103,fill="white")
    r1=cv1.create_rectangle(150,20,233,103,fill="white")
    cv1.create_rectangle(370,70,430,40,fill="green")
    cv1.create_text(400,50,text="合成")
    cv1.place(x=0,y=0)
    l16=tkinter.Label(ctk3,text="请输入等级：",bg="orange")
    l16.place(x=10,y=170)
    e1=tkinter.ttk.Entry(ctk3,width=20)
    e1.place(x=90,y=170)
    cv1.bind("<Button-1>",f15)
def f6():
    ctk4=tkinter.Toplevel(tk)
    ctk4.title("图鉴 - 大甲虫传奇")
    global img3
    img3=[]
    for i in range(1,8):
        img3.append(tkinter.PhotoImage(file=".\\illustration\\egg"+str(i)+".png"))
        tmpl=tkinter.Label(ctk4,image=img3[i-1])
        tmpl.grid(row=i-1,column=0)
        tmpl2=tkinter.Label(ctk4,text="黄甲虫蛋 等级："+level[i])
        tmpl2.grid(row=i-1,column=1)
    for i in range(1,7):
        img3.append(tkinter.PhotoImage(file=".\\illustration\\bettle"+str(i)+".png"))
        tmpl=tkinter.Label(ctk4,image=img3[i+6])
        tmpl.grid(row=i-1,column=2)
        tmpl2=tkinter.Label(ctk4,text="紫甲虫 等级："+level[i])
        tmpl2.grid(row=i-1,column=3)
    for i in range(1,7):
        img3.append(tkinter.PhotoImage(file=".\\illustration\\ybettle"+str(i)+".png"))
        tmpl=tkinter.Label(ctk4,image=img3[i+12])
        tmpl.grid(row=i-1,column=4)
        tmpl2=tkinter.Label(ctk4,text="黄甲虫 等级："+level[i])
        tmpl2.grid(row=i-1,column=5)
def f7():
    ctk5=tkinter.Toplevel(tk)
    ctk5.title("背包 - 大甲虫传奇")
    l11=tkinter.Label(ctk5,text="背包：")
    l11.grid(row=0,column=0)
    global img
    img=[]
    for i in range(0,len(backpack)):
        img.append(tkinter.PhotoImage(file=".\\illustration\\"+backpack[i]+".png"))
        tmpl=tkinter.Label(ctk5,image=img[i])
        tmpl.grid(row=int(i/3+1),column=i%3)
def f8():
    global ctk6
    ctk6=tkinter.Toplevel(tk)
    ctk6.title("商店 - 大甲虫传奇")
    ctk6.geometry("1080x592")
    global i3
    i3=tkinter.PhotoImage(file=".\\sd.png")
    l12=tkinter.Label(ctk6,image=i3)
    l12.place(x=0,y=0)
    
    b7=tkinter.ttk.Button(ctk6,text="切换",command=f9)
    b7.place(x=1000,y=492)
    b15=tkinter.ttk.Button(ctk6,text="打开背包",command=f7)
    b15.place(x=900,y=492)
    b18=tkinter.ttk.Button(ctk6,text="卖蛋",command=f13)
    b18.place(x=800,y=492)
    b20=tkinter.ttk.Button(ctk6,text="卖甲虫",command=f17)
    b20.place(x=700,y=492)
    b21=tkinter.ttk.Button(ctk6,text="生蛋器",command=f19)
    b21.place(x=600,y=492)
    b24=tkinter.ttk.Button(ctk6,text="孵蛋器",command=f22)
    b24.place(x=500,y=492)
def f9():
    global ctk6,l12,money,ctk7
    ctk6.destroy()
    ctk7=tkinter.Toplevel(tk)
    ctk7.title("商店 - 大甲虫传奇")
    l12=tkinter.Label(ctk7,text="剩余钱数："+str(money))
    l12.grid(row=0,column=0)
    global img2
    img2=[]
    for i in range(1,8):
        img2.append(tkinter.PhotoImage(file=".\\illustration\\egg"+str(i)+".png"))
        tmpl=tkinter.Label(ctk7,image=img2[i-1])
        tmpl.grid(row=i,column=0)
        tmpl2=tkinter.Label(ctk7,text="甲虫蛋 等级："+level[i]+"\n价格"+str(pow(2,i+1)))
        tmpl2.grid(row=i,column=1)
    b8=tkinter.ttk.Button(ctk7,text="购买",command=lambda:f10(1))
    b8.grid(row=1,column=2)
    b9=tkinter.ttk.Button(ctk7,text="购买",command=lambda:f10(2))
    b9.grid(row=2,column=2)
    b10=tkinter.ttk.Button(ctk7,text="购买",command=lambda:f10(3))
    b10.grid(row=3,column=2)
    b11=tkinter.ttk.Button(ctk7,text="购买",command=lambda:f10(4))
    b11.grid(row=4,column=2)
    b12=tkinter.ttk.Button(ctk7,text="购买",command=lambda:f10(5))
    b12.grid(row=5,column=2)
    b13=tkinter.ttk.Button(ctk7,text="购买",command=lambda:f10(6))
    b13.grid(row=6,column=2)
    b14=tkinter.ttk.Button(ctk7,text="购买",command=lambda:f10(7))
    b14.grid(row=7,column=2)
    global i4
    i4=tkinter.PhotoImage(file=".\\illustration\\bettle1.png")
    l13=tkinter.Label(ctk7,image=i4)
    l13.grid(row=8,column=0)
    l14=tkinter.Label(ctk7,text="紫甲虫 等级："+level[1]+"\n价格6")
    l14.grid(row=8,column=1)
    b17=tkinter.ttk.Button(ctk7,text="购买",command=f12)
    b17.grid(row=8,column=2)
    b16=tkinter.ttk.Button(ctk7,text="切换",command=f11)
    b16.grid(row=9,column=2)
def f10(lv):
    global money
    if money<pow(2,lv+1):
        tkinter.messagebox.showinfo("购买提示","余额不足！")
    else:
        money-=pow(2,lv+1)
        backpack.append("egg"+str(lv))
        tkinter.messagebox.showinfo("购买提示","购买成功！")
def f11():
    global ctk7
    ctk7.destroy()
    f8()
def f12():
    global money
    if money<6:
        tkinter.messagebox.showinfo("购买提示","余额不足！")
    else:
        money-=6
        backpack.append("bettle1")
        tkinter.messagebox.showinfo("购买提示","购买成功！")
def f13():
    global ctk8,e0
    ctk8=tkinter.Toplevel(tk)
    ctk8.title("卖蛋 - 商店 - 大甲虫传奇")
    l15=tkinter.Label(ctk8,text="请输入等级（文字）：")
    l15.grid(row=0,column=0)
    e0=tkinter.ttk.Entry(ctk8,width=20)
    e0.grid(row=0,column=1)
    b19=tkinter.ttk.Button(ctk8,text="卖蛋",command=f14)
    b19.grid(row=0,column=2)
def f14():
    global e0,money
    try:
        lv=level.index(e0.get())
    except:
        tkinter.messagebox.showerror("运行时错误","错误信息："+err[0])
        return
    if lv==0:
        global achievement3
        tkinter.messagebox.showerror("运行时错误","错误信息：暂无")
        achievement3=1
        tkinter.messagebox.showinfo("获得成就","获得成就 我怎么没想到")
        return
    try:
        index=backpack.index("egg"+str(lv))
    except:
        tkinter.messagebox.showerror("运行时错误","错误信息："+err[1])
        return
    if tkinter.messagebox.askyesno("卖出提示","你可以卖出此物品来获得"+str(pow(2,lv))+"元，确定卖出？"):
        del backpack[index]
        money+=pow(2,lv)
        tkinter.messagebox.showinfo("卖出提示","卖出成功！")
        global ctk8
        ctk8.destroy()
def f15(event):
    if event.x<=430 and event.y<=70 and event.x>=370 and event.y>=40:
        f16()
def f16():
    global e1,cv1,ctk3
    try:
        lv=level.index(e1.get())
    except:
        tkinter.messagebox.showerror("运行时错误","错误信息："+err[0])
        return
    if lv==0:
        global achievement3
        tkinter.messagebox.showerror("运行时错误","错误信息：暂无")
        achievement3=1
        tkinter.messagebox.showinfo("获得成就","获得成就 我怎么没想到")
        return
    if lv==8:
        tkinter.messagebox.showerror("运行时错误","错误信息："+err[2])
        return
    try:
        index=backpack.index("egg"+str(lv))
    except:
        tkinter.messagebox.showerror("运行时错误","错误信息："+err[1])
        return
    if backpack.count("egg"+str(lv))<2:
        tkinter.messagebox.showerror("运行时错误","错误信息："+err[1])
        return
    if tkinter.messagebox.askyesno("合成提示","你合成成功的概率为"+str(pow(2,7-lv))+"%，确定合成？")==True:
        global img4,r0,r1
        img4=tkinter.PhotoImage(file=".\\illustration\\egg"+str(lv)+".png")
        r3=cv1.create_image(50,20,anchor="nw",image=img4)
        r4=cv1.create_image(150,20,anchor="nw",image=img4)
        cv1.delete(r0)
        cv1.delete(r1)
        cv1.update()
        for i in range(0,10):
            cv1.move(r3,5,0)
            cv1.move(r4,-5,0)
            cv1.update()
            time.sleep(0.05)
        if random.randint(1,100)<=pow(2,7-lv):
            backpack[index]="egg"+str(lv+1)
            index2=backpack.index("egg"+str(lv))
            del backpack[index2]
            tkinter.messagebox.showinfo("合成提示","合成成功")
            ctk3.destroy()
        else:
            del backpack[index]
            index2=backpack.index("egg"+str(lv))
            del backpack[index2]
            tkinter.messagebox.showinfo("合成提示","合成失败")
def f17():
    global ctk9,e2
    ctk9=tkinter.Toplevel(tk)
    ctk9.title("卖甲虫 - 商店 - 大甲虫传奇")
    l17=tkinter.Label(ctk9,text="请输入等级（文字）：")
    l17.grid(row=0,column=0)
    e2=tkinter.ttk.Entry(ctk9,width=20)
    e2.grid(row=0,column=1)
    b22=tkinter.ttk.Button(ctk9,text="卖甲虫",command=f18)
    b22.grid(row=0,column=2)
def f18():
    global e2,money
    try:
        lv=level.index(e2.get())
    except:
        tkinter.messagebox.showerror("运行时错误","错误信息："+err[0])
        return
    if lv==0:
        global achievement3
        tkinter.messagebox.showerror("运行时错误","错误信息：暂无")
        achievement3=1
        tkinter.messagebox.showinfo("获得成就","获得成就 我怎么没想到")
        return
    yellow=tkinter.messagebox.askyesno("卖出提示","请问卖紫甲虫还是黄甲虫？（Yes=黄，No=紫）")
    try:
        if yellow:
            index=backpack.index("ybettle"+str(lv))
        else:
            index=backpack.index("bettle"+str(lv))
    except:
        tkinter.messagebox.showerror("运行时错误","错误信息："+err[1])
        return
    if tkinter.messagebox.askyesno("卖出提示","你可以卖出此物品来获得"+str(pow(2,lv+1))+"元，确定卖出？"):
        del backpack[index]
        money+=pow(2,lv)
        tkinter.messagebox.showinfo("卖出提示","卖出成功！")
        global ctk9
        ctk9.destroy()
def f19():
    global fun0,money
    if fun0 or tkinter.messagebox.askyesno("购买提示","这个东西可以让你的甲虫生蛋，你需要花费一元来买"):
        if not fun0:
            if money<1:
                tkinter.messagebox.showinfo("购买提示","余额不足！")
                return
            fun0=1
            money-=1
        f20()
def f20():
    global ctk10,e3
    ctk10=tkinter.Toplevel(tk)
    ctk10.title("生蛋器 - 商店 - 大甲虫传奇")
    l18=tkinter.Label(ctk10,text="请输入要生蛋的甲虫等级（文字）：")
    l18.grid(row=0,column=0)
    e3=tkinter.ttk.Entry(ctk10,width=20)
    e3.grid(row=0,column=1)
    b23=tkinter.ttk.Button(ctk10,text="生蛋",command=f21)
    b23.grid(row=0,column=2)
def f21():
    global e3
    try:
        lv=level.index(e3.get())
    except:
        tkinter.messagebox.showerror("运行时错误","错误信息："+err[0])
        return
    if lv==0:
        global achievement3
        tkinter.messagebox.showerror("运行时错误","错误信息：暂无")
        achievement3=1
        tkinter.messagebox.showinfo("获得成就","获得成就 我怎么没想到")
        return
    try:
        index=backpack.index("bettle"+str(lv))
    except:
        tkinter.messagebox.showerror("运行时错误","错误信息："+err[1])
        return
    if tkinter.messagebox.askyesno("生蛋提示","该甲虫可以生四个蛋,确定生蛋？"):
        del backpack[index]
        backpack.append("egg"+str(lv))
        backpack.append("egg"+str(lv))
        backpack.append("egg"+str(lv))
        backpack.append("egg"+str(lv))
        tkinter.messagebox.showinfo("生蛋提示","生蛋成功！")
        global ctk10
        ctk10.destroy()
def f22():
    global fun1,money
    if fun1 or tkinter.messagebox.askyesno("购买提示","这个东西可以让你的蛋孵化，你需要花费一元来买"):
        if not fun1:
            if money<1:
                tkinter.messagebox.showinfo("购买提示","余额不足！")
                return
            fun1=1
            money-=1
        f23()
def f23():
    global ctk11,e4
    ctk11=tkinter.Toplevel(tk)
    ctk11.title("孵蛋器 - 商店 - 大甲虫传奇")
    l18=tkinter.Label(ctk11,text="请输入蛋的等级（文字）：")
    l18.grid(row=0,column=0)
    e4=tkinter.ttk.Entry(ctk11,width=20)
    e4.grid(row=0,column=1)
    b25=tkinter.ttk.Button(ctk11,text="孵化",command=f24)
    b25.grid(row=0,column=2)
def f24():
    global e4,achievement4,achievement5
    try:
        lv=level.index(e4.get())
    except:
        tkinter.messagebox.showerror("运行时错误","错误信息："+err[0])
        return
    if lv==0:
        global achievement3
        tkinter.messagebox.showerror("运行时错误","错误信息：暂无")
        achievement3=1
        tkinter.messagebox.showinfo("获得成就","获得成就 我怎么没想到")
        return
    try:
        index=backpack.index("egg"+str(lv))
    except:
        tkinter.messagebox.showerror("运行时错误","错误信息："+err[1])
        return
    if tkinter.messagebox.askyesno("孵蛋提示","确定孵蛋？"):
        del backpack[index]
        if random.randint(1,100)<=15:
            if lv<=6:
                backpack.append("bettle"+str(lv))
            else:
                if lv==7:
                    backpack.append("bettle6")
                    backpack.append("bettle6")
                else:
                    backpack.append("bettle6")
                    backpack.append("bettle6")
                    backpack.append("bettle6")
                    backpack.append("bettle6")
        else:
            if lv<=6:
                backpack.append("ybettle"+str(lv))
            else:
                if lv==7:
                    backpack.append("ybettle6")
                    backpack.append("ybettle6")
                else:
                    backpack.append("ybettle6")
                    backpack.append("ybettle6")
                    backpack.append("ybettle6")
                    backpack.append("ybettle6")
        if lv==1 and not achievement4:
            tkinter.messagebox.showinfo("获得成就","获得成就 孵蛋能手")
            achievement4=1
        if lv==2 and not achievement5:
            tkinter.messagebox.showinfo("获得成就","获得成就 孵蛋能手")
            achievement5=1
        tkinter.messagebox.showinfo("孵蛋提示","孵蛋成功！")
        global ctk11
        ctk11.destroy()
def f25():
    cookie={}
    with open(".\\cookie.json","r",encoding='utf-8') as f:
        cookie=json.load(f)
    if cookie["player_id"]==-1:
        if tkinter.messagebox.askyesno("账号提醒","你目前为访客，关闭窗口后将会清空所有数据，暂无存档功能，是否注册账号？"):
            pass
        else:
            tk.destroy()
    else:
        tk.destroy()
def f26():
    ctk12=tkinter.Toplevel(tk)
    ctk12.title("抽奖 - 大甲虫传奇")
    l21=tkinter.Label(ctk12,text="说明：\n1.每抽一次花费 1 元。\n2.每抽一次，有 40% 没抽中，30% 普通蛋，15% 普通紫甲虫，15% 罕见蛋")
    l21.pack()
    b27=tkinter.ttk.Button(ctk12,text="每日签到",command=f27)
    b27.pack()
def f27():
    pass
tk=tkinter.Tk()
tk.title("大甲虫传奇")
tk.resizable(0,0)
i0=tkinter.PhotoImage(file=".\\djccq.png")
l0=tkinter.Label(tk,image=i0)
l0.bind("<Button-1>",f0)
l0.pack()
pygame.mixer.init()
pygame.mixer.music.load(".\\music.mp3")
pygame.mixer.music.set_endevent(pygame.USEREVENT)
pygame.mixer.music.play(-1)
tk.protocol("WM_DELETE_WINDOW",f25)
tk.mainloop()
