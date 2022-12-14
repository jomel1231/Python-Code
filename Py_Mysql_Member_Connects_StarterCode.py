from tkinter import*
from tkinter import ttk
import tkinter.messagebox 
import pymysql
import random 

class MemberConnect:
    def __init__(self,root):
        self.root = root
        blank_space = " "
        self.root.title(202 * blank_space + "MySQL Connector")
        self.root.geometry("1360x700+0+0")

MemID = StringVar()
Firstname = StringVar()
Surname = StringVar()
Address = StringVar()
PoBox = StringVar()
Gender = StringVar()
Mtype = StringVar()
Mobile = StringVar()
Email = StringVar()
Search = StringVar()
MemIDBar = StringVar()


if __name__=='__main__':
    root = Tk()
    application = MemberConnect(root)
    root.mainloop
