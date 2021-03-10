from tkinter import*
from tkinter import ttk
import random
from tkinter import messagebox
import backend.database
import model.model


class Hotel:
    def __init__ (self,root):
        self.root = root
        self.root.title("EMPLOYEE SYSTEM")
        self.root.geometry("1350x750+0+0")
        self.root.config(background="white")


#--------------------------------FRAME DEPARTMENT------------------------------#
        MainFrame = Frame(self.root)
        MainFrame.grid()

        self.db = backend.database.DBConnect()
        TopFrame = Frame(MainFrame , bd=14 , width = 1350 , height = 550, padx = 20, relief = RIDGE, bg = "maroon")
        TopFrame.pack(side = TOP)
        title=Label(TopFrame,text = " EMPLOYEE SYSTEM", font =("helvetica", 20)).place(x=4,y=3)

        LeftFrame = Frame(TopFrame, bd=10, width=450, height=700, padx=2, relief= RIDGE, bg="gray")
        LeftFrame.pack(side=LEFT)


        RightFrame = Frame(TopFrame, bd=10, width=820, height=700, padx=2, relief=RIDGE, bg="black")
        RightFrame.pack(side=RIGHT)

        BottomFrame = Frame(MainFrame,bd=10, width=1350, height=150, padx=20, relief=RIDGE, bg="black")
        BottomFrame.pack(side=BOTTOM)
        
#---------------------------------BUTTON FUNNCTION DEPARTMENT---------------------------#
        def iExit():
            iExit=messagebox.askyesno("Confirm if you want to exit!")
            if iExit>0:
                root.destroy()
                return
                    
        def Reset():
            self.Employee_Ref.set("")
            self.Name.set("")
            self.Address.set("")
            self.Mobile.set("")
            self.Gender.set("")



            
            

#---------------------------VARIABLES ----------------------#
        
        self.Employee_Ref = StringVar()
        self.Name= StringVar()
        self.Address = StringVar()
        self.Mobile= StringVar()
        self.IDtype = StringVar()
        self.Gender = StringVar()
        self.search= StringVar()
        self.searchtxt=StringVar()
        self.sort= StringVar()

        
        
       #------------------------------------LEFT FRAME--------------------------#
        self.lblEmployee_Ref = Label(LeftFrame , font=("arial", 12, "bold"), text= "Employee Ref", padx=2, pady=2 ,bg="gray")
        self.lblEmployee_Ref.grid(row=0,column=0, sticky=W)
        self.txtEmployee_Ref = Entry(LeftFrame , font=("arial", 12, "bold"), textvariable=self.Employee_Ref, width=20)
        self.txtEmployee_Ref.grid(row=0,column=1, pady=3, padx=20)
        
        self.lblName = Label(LeftFrame , font=("arial", 12, "bold"), text= "Name", padx=2,pady=2, bg="gray")
        self.lblName.grid(row=1,column=0, sticky=W)
        self.txtName = Entry(LeftFrame , font=("arial", 12, "bold"), textvariable= self.Name, width=20)
        self.txtName.grid(row=1,column=1, pady=3, padx=20)

        
       
        self.lblAddress= Label(LeftFrame , font=("arial", 12, "bold"), text= "Address", padx=2, pady= 2 ,bg="gray")
        self.lblAddress.grid(row=3,column=0, sticky=W)
        self.txtAddress = Entry(LeftFrame , font=("arial", 12, "bold"), textvariable= self.Address, width=20)
        self.txtAddress.grid(row=3,column=1, pady=3, padx=20)


        
        self.lblMobile = Label(LeftFrame , font=("arial", 12, "bold"), text= "Mobile", padx=2,pady=2 ,bg="gray")
        self.lblMobile.grid(row=5,column=0, sticky=W)
        self.txtMobile = Entry(LeftFrame , font=("arial", 12, "bold"), textvariable= self.Mobile, width=20)
        self.txtMobile.grid(row=5,column=1, pady=3, padx=20)




        self.lblGender= Label(LeftFrame , font=("arial", 12, "bold"), text= "Gender", padx=2, pady= 2 ,bg="gray")
        self.lblGender.grid(row=10,column=0, sticky=W)
        self.cboGender=ttk.Combobox(LeftFrame, textvariable= self.Gender, state="read only", font=("arial",12, "bold"),width=18)
        self.cboGender["value"]= ("", "Male", "Female", "Any Other")
        self.cboGender.current(0)
        self.cboGender.grid(row=10,column=1, pady=3, padx=20)





#---------------------------RIGHT FRAME-----------------------------------#
        self.tableframe = Frame(RightFrame, height = 350, width=900, bd= 5,bg="black")
        self.tableframe.grid(row=1, column=0,columnspan=2,padx=2,pady=3)
        Table_Frame = Frame(RightFrame, bd=4, relief=RIDGE, bg="black")
        Table_Frame.place(x=2, y=3, width=900, height=320)
        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.hotel_table = ttk.Treeview(Table_Frame,
                                        columns=("Employee ref","Name", "Address","Mobile", "Gender"),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.hotel_table.xview)
        scroll_y.config(command=self.hotel_table.yview)
        self.hotel_table.heading("Employee ref", text="Employeeref")
        self.hotel_table.heading("Name", text="Name")
        self.hotel_table.heading("Address", text="Address")
        self.hotel_table.heading("Mobile", text="Mobile")
        self.hotel_table.heading("Gender", text="Gender")


        self.hotel_table['show'] = 'headings'
        self.hotel_table.column("Employee ref", width=30)
        self.hotel_table.column("Name", width=30)
        self.hotel_table.column("Address", width=30)
        self.hotel_table.column("Mobile", width=30)
        self.hotel_table.column("Gender", width=30)

        self.hotel_table.pack(fill=BOTH, expand=0.5)
        self.fetch_data()
        self.hotel_table.bind("<ButtonRelease-1>", self.cursor)



        self.searchby = Label(RightFrame,padx=10,pady=1,bd=4,fg="black",font=("arial",10,"bold"),width=10,  height=1,bg="sky blue",cursor="hand2", text="Search By").grid(row=4,column=0,padx=5)
        self.cboSearch = ttk.Combobox(RightFrame, textvariable=self.search, state="read only", font=("arial", 12, "bold"),
                                        width=18)
        self.cboSearch["value"] = ("", " Employee_ref", "Mobile")
        self.cboSearch.current(0)
        self.cboSearch.grid(row=5, column=0, pady=3, padx=15)
        self.txtSearch = Entry(RightFrame, font=("arial", 12, "bold"), width=20,textvariable=self.searchtxt)
        self.txtSearch.grid(row=4, column=1, pady=3, padx=20)


        self.sortby = Label(RightFrame, padx=10, pady=1, bd=4, fg="black", font=("arial", 10, "bold"), width=10,
                            height=1, bg="sky blue", cursor="hand2", text="Sort By").grid(row=7, column=0, padx=5)
        self.cboSort = ttk.Combobox(RightFrame, textvariable=self.sort, state="read only", font=("arial", 12, "bold"),
                                      width=18)
        self.cboSort["value"] = ("", "Employee_Ref", "Name")
        self.cboSort.current(0)
        self.cboSort.grid(row=8, column=0, pady=3, padx=15)
        self.txtSort= Button(RightFrame,text="Show all" ,font=("arial", 12, "bold"),bg="skyblue",width=20,cursor="hand2")
        self.txtSort.grid(row=7, column=1, pady=3, padx=20)

        #---------------------------BUTTON DEPARTMENT-----------------------------#


        self.btnReset= Button(BottomFrame,padx= 16, pady= 1, bd= 4, fg= "black", font=("arial",13, "bold"), width=10, height= 2, bg= "skyblue",cursor="hand2", text= "Reset",command = Reset ). grid(row=0,column=6,padx=5)

        self.btnExit= Button(BottomFrame, padx=16, pady=1, bd=4, fg="black", font=("arial",13,"bold"),width=10, height=2,bg="skyblue",cursor="hand2", text="Exit", command= iExit).grid(row=0,column=7,padx=5)
        
        self.btnSearch= Button(BottomFrame, padx=16, pady=1, bd=4, fg="black", font=("arial",13,"bold"),width=10, height=2,bg="cadetblue",cursor="hand2", text="Search",command=self.search_data).grid(row=0,column=8,padx=5)

        self.btnSort = Button(BottomFrame, padx=16, pady=1, bd=4, fg="black", font=("arial", 13, "bold"), width=10,
                                height=2, bg="cadet blue", cursor="hand2", text="Sort",command=self.sorted).grid(
            row=0, column=9, padx=5)
        self.btnDelete = Button(TopFrame, padx=10, pady=1, bd=4, fg="black", font=("arial", 10, "bold"), width=7,
                              height=1, bg="cadet blue", cursor="hand2", text="Delete",command=self.delete).place(
            x=100, y=350)
        self.btnAdd = Button(TopFrame, padx=10, pady=1, bd=4, fg="black", font=("arial", 10, "bold"), width=7,
                              height=1, bg="cadet blue", cursor="hand2", text="Add",command=self.adddata).place(
            x=0, y=350)
        self.btnUpdate = Button(TopFrame, padx=10, pady=1, bd=4, fg="black", font=("arial", 10, "bold"), width=7,
                              height=1, bg="cadet blue", cursor="hand2", text="Update",command=self.update).place(
            x=200, y=350)


    def cursor(self, ev):
        curosor_row = self.hotel_table.focus()
        contents = self.hotel_table.item(curosor_row)
        row = contents['values']
        self.Employee_Ref.set(row[0])
        self.Name.set(row[1])
        self.Address.set(row[2])
        self.Mobile.set(row[3])
        self.Gender.set(row[4])


    def fetch_data(self):
        query = ("select * from new_table")

        rows = self.db.select(query)
        if len(rows) != 0:
            self.hotel_table.delete(*self.hotel_table.get_children())
            for row in rows:
                self.hotel_table.insert('', END, values=row)



    def clear_data(self):
        self.Employee_Ref.set("")
        self.Name.set("")
        self.Address.set("")
        self.Mobile.set("")
        self.Gender.set("")

    def update(self):
        employee_ref = self.txtEmployee_Ref.get()
        name = self.txtName.get()
        address = self.txtAddress.get()
        mobile = self.txtMobile.get()
        gender = self.cboGender.get()

        if employee_ref == '' or name == '' or address == '' or mobile == '' or gender == '':
            messagebox.showerror('Error', 'plz fill the empty field')
            return

        else:
            md = model.model.User(employee_ref,name, address,mobile,gender)
            query = "update new_table set Name=%s,Address=%s,Mobile=%s,Gender=%s  where Employeeref=%s"
            values = (md.get_username(),md.get_address(), md.get_phonenumber(), md.get_gender(),
                      md.get_employeerefrence())
            self.db.update(query, values)
            self.fetch_data()
            self.clear_data()

            messagebox.showinfo("status", "Updated Succesfuly")

    def delete(self):
        employee_ref = self.txtEmployee_Ref.get()
        if (employee_ref == ""):
            messagebox.showinfo("Delete Status", "employeref compolsary for delete")
        else:
            query = "delete from new_table where Employeeref=%s"
            value = (employee_ref,)
            self.db.delete(query, value)
            messagebox.showinfo("Status", "Deleted Succesfuly")
            self.clear_data()
            self.fetch_data()

    def binary_emp(self, list, item):
        if list == []:
            return ValueError
        self.list = list
        self.item = item
        max = len(list) - 1
        min = 0
        while min <= max:
            mid = (min + max) // 2
            if self.list[mid] == self.item:
                return mid
            elif self.list[mid] > self.item:
                max = mid - 1
            else:
                min = mid + 1
        return -1

    def search_data(self):
        if self.search.get()=="Mobile":
            query = "select * from new_table"
            rows = self.db.select(query)
            myStack = []
            for row in rows:
                myStack.append(row[0])
            self.sorted = self.mergesort(myStack)
            item = int(self.searchtxt.get())
            sorted = self.sorted
            index = self.binary_emp(sorted, item)
            for row in rows:
                if sorted[index] == row[0]:
                    self.hotel_table.delete(*self.hotel_table.get_children())
                    self.hotel_table.insert('', END, value=row)
                    self.searchtxt.set("")


    def mergesort(self, alist):
        if len(alist) > 1:
            mid = len(alist) // 2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]
            self.mergesort(lefthalf)
            self.mergesort(righthalf)
            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k] = lefthalf[i]
                    i = i + 1
                else:
                    alist[k] = righthalf[j]
                    j += 1
                k += 1
            while i < len(lefthalf):
                alist[k] = lefthalf[i]
                i += 1
                k += 1
            while j < len(righthalf):
                alist[k] = righthalf[j]
                j += 1
                k += 1
        return alist

    def sorted(self):
        query = ("select * from new_table")
        rows = self.db.select(query)
        myStack = []
        if len(rows) != 0:
            self.hotel_table.delete(*self.hotel_table.get_children())
            if self.sort.get() == "Employee_Ref":
                for row in rows:
                    myStack.append(row[0])
                self.sorted = self.mergesort(myStack)

                for i in self.sorted:
                    for row in rows:
                        if i == row[0]:
                            self.hotel_table.insert('', END, value=row)
                            rows.remove(row)
            else:
                self.hotel_table.delete(*self.hotel_table.get_children())
                if self.sort.get() == "Name":
                    for row in rows:
                        myStack.append(row[1])
                    self.sorted = self.mergesort(myStack)

                    for i in self.sorted:
                        for row in rows:
                            if i == row[1]:
                                self.hotel_table.insert('', END, value=row)
                                rows.remove(row)




    def adddata(self):
        employee_ref=self.txtEmployee_Ref.get()
        name = self.txtName.get()
        address = self.txtAddress.get()
        mobile=self.txtMobile.get()
        gender = self.cboGender.get()


        if employee_ref==''or name == '' or address == '' or mobile == '' or gender == ''  :
            messagebox.showerror('Error', 'plz fill the empty field')
            return
        md = model.model.User(employee_ref,name, address,mobile,gender)
        query = "insert into new_table(Employeeref,Name,Address,Mobile,Gender) values(%s,%s,%s,%s,%s)"
        values = (
            md.get_employeerefrence(),md.get_username(),md.get_address(), md.get_phonenumber(), md.get_gender())

        self.db.insert(query, values)

        self.fetch_data()
        self.clear_data()

        query = ("select * from new_table")

        rows = self.db.select(query)
        messagebox.showinfo("congratulations", " number added succesfully")





if __name__ =='__main__':
    root = Tk()
    application = Hotel (root)
    root.mainloop()