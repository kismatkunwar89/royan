from tkinter import*
from tkinter import ttk, messagebox

class Register:
    def __init__ (self,root):
        self.root=root
        self.root.title("REGISTRATION WINDOW")
        self.root.geometry("1350x700+0+0")
       
        frame1=Frame(self.root,bg="gray")
        frame1.place(x=480,y=100,width=700,height=500)
        
        title= Label(frame1,text="------------------REGISTER TO Softwarica Hotel:-------------------", font=("New times roman", 20,"italic"),fg="black",bg="gray").place (x=50,y=30)

        #---------------Row1-----------#
        self.var_fname=StringVar()
        f_name= Label(frame1,text="First name:", font=("New times roman", 15,"bold"),fg="black",bg="gray").place (x=50,y=100)
        txt_fname= Entry(frame1,font=("times new roman", 15),bg="dark gray",textvariable= self.var_fname).place(x=50,y=130,width = 250)

        l_name= Label(frame1,text="Last name:", font=("New times roman", 15,"bold"),fg="black",bg="gray").place (x=370,y=100)
        self.txt_lname= Entry(frame1,font=("times new roman", 15),bg="dark gray")
        self.txt_lname.place(x=370,y=130,width = 250)
        #---------------Row2-----------#
        Address= Label(frame1,text="Address:", font=("New times roman", 15,"bold"),fg="black",bg="gray").place (x=50,y=170)
        self.txt_address= Entry(frame1,font=("times new roman", 15),bg="dark gray")
        self.txt_address.place(x=50,y=200,width = 250)

        Age= Label(frame1,text="Age:", font=("New times roman", 15,"bold"),fg="black",bg="gray").place (x=370,y=170)
        self.txt_Age= Entry(frame1,font=("times new roman", 15),bg="dark gray")
        self.txt_Age.place(x=370,y=200,width = 250)
        #------------ Row-------------#
        username= Label(frame1,text="Username:", font=("New times roman", 15,"bold"),fg="black",bg="gray").place (x=50,y=240)
        self.txt_username= Entry(frame1,font=("times new roman", 15),bg="dark gray")
        self.txt_username.place(x=50,y=270,width = 250)
        password= Label(frame1,text="Password:", font=("New times roman", 15,"bold"),fg="black",bg="gray").place (x=370,y=240)
        self.txt_password= Entry(frame1,font=("times new roman", 15),bg="dark gray")
        self.txt_password.place(x=370,y=270,width = 250)
       
        email= Label(frame1,text="E-mail:", font=("New times roman", 15,"bold"),fg="black",bg="gray").place (x=50,y=310)
        self.txt_email= Entry(frame1,font=("times new roman", 15),bg="dark gray")
        self.txt_email.place(x=50,y=350,width = 250)

        confirm_password= Label(frame1,text="Confirm password:", font=("New times roman", 15,"bold"),fg="black",bg="gray").place (x=370,y=310)
        self.txt_cpassword= Entry(frame1,font=("times new roman", 15),bg="dark gray")
        self.txt_cpassword.place(x=370,y=350,width = 250)
        #---------------------------------------------------------------------------------------------#
        self.var_chk = IntVar()
        chk=Checkbutton(frame1,text="I agree to the terms and conditions.",variable=self.var_chk,onvalue=1,offvalue=0,font=("ariel",14,"italic"),bg="gray").place(x=50,y=380)

        btn_register= Button(frame1,text="Register",font=("New times roman",15,"bold"),bg="gray",fg="blue",cursor="hand2", command = self.register_data).place(x=50,y=420, width = 300)

        btn_signin= Button(frame1,text="Sign in",font=("New times roman",15,"bold"),bg="gray",fg="red",cursor="hand2").place(x=370,y=420, width = 300)        
        #------------------------------------------------------#

    def register_data(self):
        

        
        if self.var_fname.get()=="" or self.txt_lname.get()=="" or self.txt_username.get()=="" or self.txt_cpassword.get()==""or self.txt_password.get()=="" or self.txt_Age.get()=="" or self.txt_address.get()=="" or self.txt_email.get()=="":
        
            messagebox.showerror("Error","All fields are must!",parent=self.root) 
        elif self.txt_cpassword.get()!= self.txt_password.get():
            messagebox.showerror("Wrong password ", "Both the password should match each other",parent= self.root)
        elif self.var_chk.get()== 0:
            messagebox.showerror("Error","Please agree to our terms and conditions", parent= self.root)
        else:
            try:
                con= pymysql.connect(host="localhost",user="root",password="",database="mydb")
                cur=con.cursor()
                cur.execute("insert into registeration table(fname,lname,Age,Address,email,username,password)values(%s,%s,%s,%s,%s,%s,%s)",
                      (self.txt_fname.get(),
                      self.txt_lname.get(),
                      self.txt_address.get(),
                      self.txt_Age.get(),
                      self.txt_email.get(),
                      self.txt_username.get(),
                      self.txt_password.get(),
                       ))
                con.commit()
                con.close()
                messagebox.showinfo("SUCCESS","You are successfully registered to softwarica 5-star Hotel")
        
                     
            
            except Exception as es:
                messagebox.showerror("Error",f"ERROR{str(es)}", parent= self.root)

            
           
        
        
        
         


       



root=Tk()
obj = Register(root)
root.mainloop()