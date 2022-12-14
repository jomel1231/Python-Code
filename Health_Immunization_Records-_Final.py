from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql
import random 

class MemberConnect:
    def __init__(self,root):
        self.root = root
        blank_space = " "
        self.root.title(202 * blank_space + "Health Records")
        self.root.geometry("1345x608+0+0")

        RecID = StringVar()
        Childname = StringVar()
        Age = StringVar()
        Vaccinetype = StringVar()
        Vaccinedose = StringVar()
        Checkfindings = StringVar()
        Checkremarks = StringVar()
        Doctor = StringVar()
        Location = StringVar()
        Search = StringVar()
        RecIDBar = StringVar()
        #=============================================================================================
        MainFrame = Frame(self.root, bd=10, width = 683, height = 700, relief = RIDGE, bg="forestgreen")
        MainFrame.grid()

        TitleFrames = Frame(MainFrame, bd=5, width = 800, height=100, relief=RIDGE)
        TitleFrames.grid(row =0, column =0)

        SearchFrame = Frame(MainFrame, bd=5, padx = 5, width = 1000, height = 50, relief = RIDGE)
        SearchFrame.grid(row = 1, column = 0)

        MidFrame = Frame(MainFrame, bd=5, width = 800, height = 500, relief = RIDGE)
        MidFrame.grid(row = 2, column = 0)

        MemberDetailsFrm = Frame(MidFrame, bd=5, width = 800, height = 180, padx = 6, pady =4,  relief = RIDGE)
        MemberDetailsFrm.grid(row = 0, column = 0)

        TreeviewFrm = Frame(MidFrame, bd=5, width = 800, height = 400, padx =2, relief = RIDGE)
        TreeviewFrm.grid(row = 1, column =0)

        ButtonFrame = Frame(MidFrame, bd=7, width =800, height = 50, bg="forestgreen", relief = RIDGE)
        ButtonFrame.grid(row =2, column = 0)
        #============================================================================================
        self.lbTitle = Label(TitleFrames, font = ('arial', 30, 'bold'), text = "Infant Immunization Records Database", bd=10)
        self.lbTitle.grid(row = 0, column = 0, padx=100)
        #============================================================================================
        self.lblrecordID = Label(MemberDetailsFrm, font = ('arial', 12, 'bold'), text = "Record ID", bd=7, anchor ='w', justify= LEFT)
        self.lblrecordID.grid(row = 0, column =0, sticky=W, padx=5)

        self.txtrecordID = Entry(MemberDetailsFrm, font = ('arial', 12, 'bold'), bd=5, width = 29, justify = LEFT, textvariable=RecID)
        self.txtrecordID.grid(row = 0, column = 1)

        self.lblChildname = Label(MemberDetailsFrm, font = ('arial', 12, 'bold'), text = "Child Name", bd=7, anchor ='w', justify=LEFT)
        self.lblChildname.grid(row= 1, column = 0, sticky = W, padx=5)

        self.txtChildname = Entry(MemberDetailsFrm, font=('arial', 12, 'bold'), bd=5, width = 29, justify = LEFT, textvariable = Childname)
        self.txtChildname.grid(row = 1, column = 1)

        self.lblChildname = Label(MemberDetailsFrm, font = ('arial', 12, 'bold'), text = "Age", bd=7, anchor ='w', justify=LEFT)
        self.lblChildname.grid(row= 2, column = 0, sticky = W, padx=5)

        self.txtAge = Entry(MemberDetailsFrm, font=('arial', 12, 'bold'), bd=5, width = 29, justify = LEFT, textvariable = Age)
        self.txtAge.grid(row = 2, column = 1)
        #============================================================================================
        self.lblVaccinetype = Label(MemberDetailsFrm, font = ('arial', 12, 'bold'), text = "Vaccine Type", bd=7)
        self.lblVaccinetype.grid(row = 0, column =2, sticky=W, padx=5)

        self.txtVaccinetype = Entry(MemberDetailsFrm, font = ('arial', 12, 'bold'), bd=5, width = 29, justify = LEFT, textvariable=Vaccinetype)
        self.txtVaccinetype.grid(row = 0, column = 3)

        self.lblVaccinedose = Label(MemberDetailsFrm, font = ('arial', 12, 'bold'), text = "Vaccine Dose", bd=5)
        self.lblVaccinedose.grid(row= 1, column = 2, sticky = W, padx=5)

        self.cboVaccinedose = ttk.Combobox(MemberDetailsFrm, font=('arial', 12, 'bold'), width = 28, state = 'readonly', textvariable =Vaccinedose)
        self.cboVaccinedose['values'] = ('','1 Dose', '2 Doses', '3 Doses')
        self.cboVaccinedose.current(0)
        self.cboVaccinedose.grid(row = 1, column = 3) 

        self.lblCheckfindings = Label(MemberDetailsFrm, font = ('arial', 12, 'bold'), text = "Check Up Findings", bd=5)
        self.lblCheckfindings.grid(row= 2, column = 2, sticky = W, padx=5)

        self.txtCheckfindings = Entry(MemberDetailsFrm, font=('arial', 12, 'bold'), bd=5, width = 29, textvariable = Checkfindings)
        self.txtCheckfindings.grid(row = 2, column = 3)
        #============================================================================================
        self.lblCheckremarks = Label(MemberDetailsFrm, font = ('arial', 12, 'bold'), text = "Check Up Remarks", bd=7)
        self.lblCheckremarks .grid(row = 0, column =4, sticky=W, padx=5)

        self.txtCheckremarks  =Entry(MemberDetailsFrm, font = ('arial', 12, 'bold'), bd=5, width = 25, justify = LEFT, textvariable=Checkremarks)
        self.txtCheckremarks .grid(row = 0, column = 5)

        self.lblDoctor = Label(MemberDetailsFrm, font = ('arial', 12, 'bold'), text = "Doctor", bd=5)
        self.lblDoctor.grid(row= 1, column = 4, sticky = W, padx=5)

        self.txtDoctor = Entry(MemberDetailsFrm, font=('arial', 12, 'bold'), bd=5, width = 25, textvariable = Doctor)
        self.txtDoctor.grid(row = 1, column = 5)

        self.lblLocation = Label(MemberDetailsFrm, font = ('arial', 12, 'bold'), text = "Location", bd=5)
        self.lblLocation.grid(row= 2, column = 4, sticky = W, padx=5)

        self.txtLocation  =Entry(MemberDetailsFrm, font = ('arial', 12, 'bold'), bd=5, width = 25, justify = LEFT, textvariable=Location)
        self.txtLocation .grid(row = 2, column = 5)
        #==========================================Functions=========================================   
        def addNew():
            RecRef()
            if RecID.get() =="" or Childname.get()=="" or Age.get()=="":
                tkinter.messagebox.showerror("Error check input", "Enter correct member details")
            else:
                sqlCon =pymysql.connect(host="localhost", user="root", password="CBWa3o7&hK4m", database="records")
                cur =sqlCon.cursor()
                cur.execute("insert into records values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    

                RecID.get(),
                Childname.get(),
                Age.get(),
                Vaccinetype.get(),
                Vaccinedose.get(),
                Checkfindings.get(),
                Checkremarks.get(),
                Doctor.get(),
                Location.get(),
                ))
                
                sqlCon.commit()
                ShowRecord()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form", "Recored Entered Succesfully")

        def ShowRecord():
            sqlCon =pymysql.connect(host="localhost", user="root", password="CBWa3o7&hK4m", database="records")
            cur = sqlCon.cursor()
            cur.execute("select * from records")
            result = cur.fetchall()
            if len(result)!= 0:
                self.member_records.delete(*self.member_records.get_children())
                for row in result:
                        self.member_records.insert('', END, values = row)
                        sqlCon.commit() 
                sqlCon.close()

        def MembersInfo(ev):
            viewInfo = self.member_records.focus()
            learnerData = self.member_records.item(viewInfo)
            row = learnerData['values']

            RecID.set(row[0])
            Childname.set(row[1])
            Age.set(row[2])
            Vaccinetype.set(row[3])
            Vaccinedose.set(row[4])
            Checkfindings.set(row[5])
            Checkremarks.set(row[6])
            Doctor.set(row[7])
            Location.set(row[8])

        def update():
            sqlCon = pymysql.connect(host="localhost", user="root", password="CBWa3o7&hK4m", database="records")
            cur =sqlCon.cursor()
            cur.execute("Update records set childname=%s, age=%s, vaccinetype=%s, vaccinedose=%s, checkfindings=%s,""checkremarks=%s, doctor=%s, location=%s where recid=%s", (

           
            Childname.get(),
            Age.get(),
            Vaccinetype.get(),
            Vaccinedose.get(),
            Checkfindings.get(),
            Checkremarks.get(),
            Doctor.get(),
            Location.get(),
            RecID.get(),
            ))

            sqlCon.commit()
            ShowRecord()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Succesfully Updated")

        def DeleteDB():
            sqlCon = pymysql.connect(host="localhost", user="root", password="CBWa3o7&hK4m", database="records")
            cur =sqlCon.cursor()
            cur.execute("delete from records where recid=%s", RecID.get())

            sqlCon.commit()
            ShowRecord()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Succesfully Deleted")

        def Reset():
            RecID.set("")
            Childname.set("")
            Age.set("")
            Vaccinetype.set("")
            Vaccinedose.set("")
            Checkfindings.set("")
            Checkremarks.set("")
            Doctor.set("")
            Location.set("")
            Search.set("")
            RecIDBar.set("")

        def iExit():
            iExit = tkinter.messagebox.askyesno("Data Entry Form", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy() 
                return

        def searchDG():
            try:
                sqlCon = pymysql.connect(host="localhost", user="root", password="CBWa3o7&hK4m", database="records")
                cur =sqlCon.cursor()
                cur.execute("select * from records where recid='%s'"%Search.get())

                row = cur.fetchone()
                
                RecID.set(row[0])
                Childname.set(row[1])
                Age.set(row[2])
                Vaccinetype.set(row[3])
                Vaccinedose.set(row[4])
                Checkfindings.set(row[5])
                Checkremarks.set(row[6])
                Doctor.set(row[7])
                Location.set(row[8])

                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("Data Entry Form", "No Such Record")
                Search.set("")

            sqlCon.close

        def RecRef():
            RefNo = random.randint(12489, 987899)
            RefBar = (str(RefNo))
            RecID.set(RefBar)
            RefBC = ("Membership Number" + str(RefNo))
            RecIDBar.set(RefBC)       
        #============================================================================================
        scroll_y=Scrollbar(TreeviewFrm, orient = VERTICAL)

        self.member_records=ttk.Treeview(TreeviewFrm, height= 12, columns = ("recid", "childname", "age", "vaccinetype", "vaccinedose", "checkfindings", "checkremarks", "doctor", "location"),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill = Y)

        self.member_records.heading("recid", text = "Record ID")
        self.member_records.heading("childname", text = "Child Name")
        self.member_records.heading("age", text = "Age")
        self.member_records.heading("vaccinetype", text = "Vaccine Type")
        self.member_records.heading("vaccinedose", text = "Vaccine Dose")
        self.member_records.heading("checkfindings", text = "Findings")
        self.member_records.heading("checkremarks", text = "Remarks")
        self.member_records.heading("doctor", text = "Doctor")
        self.member_records.heading("location", text = "Location")

        self.member_records['show']='headings'

        self.member_records.column("recid", width = 100)
        self.member_records.column("childname", width = 165)
        self.member_records.column("age", width = 50)
        self.member_records.column("vaccinetype", width = 120)
        self.member_records.column("vaccinedose", width = 120)
        self.member_records.column("checkfindings", width = 200)
        self.member_records.column("checkremarks", width = 200)
        self.member_records.column("doctor", width = 165)
        self.member_records.column("location", width = 165)

        self.member_records.pack(fill =BOTH, expand=1)
        self.member_records.bind("<ButtonRelease-1>", MembersInfo)
        ShowRecord()
        #============================================================================================
        self.txtSearch = Entry(SearchFrame, font = ('arial' , 16, 'bold'), width =33, justify ='right', textvariable=Search)
        self.txtSearch.grid(row = 0, column = 2)

        self.btnSearch = Button(SearchFrame, pady=1, padx=10, bd=4, font = ('arial', 16, 'bold'), width=9, height = 1, text ="Search", bg= "forestgreen", command=searchDG).grid(row = 0, column = 3,padx=1)
        #============================================================================================
        self.btnAddNew = Button(ButtonFrame, pady=1, bd=4, fg="black", font = ('arial', 16, 'bold'), padx=28, width=12, height = 1, text ="AddNew", command=addNew).grid(row = 0, column = 0,padx=2)
        self.btnShowRecord = Button(ButtonFrame, pady=1, bd=4, fg="black", font = ('arial', 16, 'bold'), padx=29, width=12, height = 1, text ="Show Record", command=ShowRecord).grid(row = 0, column = 1,padx=1)
        self.btnUpdate = Button(ButtonFrame, pady=1, bd=4, fg="black", font = ('arial', 16, 'bold'),padx=29, width=11, height = 1, text ="Update", command=update).grid(row = 0, column = 2,padx=2)
        self.btnDelete = Button(ButtonFrame, pady=1, bd=4, fg="black", font = ('arial', 16, 'bold'),padx=29, width=11, height = 1, text ="Delete", command=DeleteDB).grid(row = 0, column = 3,padx=1)
        self.btnReset = Button(ButtonFrame, pady=1, bd=4, fg="black", font = ('arial', 16, 'bold'),padx=29, width=11, height = 1, text ="Reset", command=Reset).grid(row = 0, column = 5,padx=2)
        self.btnExit = Button(ButtonFrame, pady=1, bd=4, fg="black", font = ('arial', 16, 'bold'),padx=29, width=11, height = 1, text ="Exit", command=iExit).grid(row = 0, column = 6,padx=2)
        #============================================================================================

                            
if __name__=='__main__':
    root = Tk()
    application = MemberConnect(root)
    root.mainloop

