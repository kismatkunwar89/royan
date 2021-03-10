from tkinter import*
from tkinter import ttk, messagebox
import dashboard

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN PAGE")
        self.root.geometry("1350x700+0+0")
        

        frame1= Frame(self.root, bg="gray")
        frame1.place(x=480, y = 100,width=400 ,height=300)
        
        title=Label(frame1,text="LOGIN to SOFTWARICA HOTEL",font=("new times roman",19,"italic"),bg="gray",fg="black").place(x=50,y=30)

        username= Label(frame1,text="Username:", font=("New times roman", 16,"bold"),fg="green",bg="gray").place (x=50,y=100)
        self.txt_username= Entry(frame1,font=("times new roman", 16),bg="white")
        self.txt_username.place(x=50,y=130,width = 350)
        password= Label(frame1,text="Password:", font=("New times roman", 16,"bold"),fg="green",bg="gray").place (x=50,y=170)
        self.txt_password= Entry(frame1,font=("times new roman", 15),bg="white")
        self.txt_password.place(x=50,y=200,width = 350)
        #------------Buttons department--------------#
        btn_login= Button(frame1,text="Login",font=("New times roman",15,"bold"),bg="gray",fg="black",cursor="hand2",command=lambda: self.login_data(self.txt_username.get(), self.txt_password.get())).place(x=50,y=240, width = 300)

        btn_exit= Button(frame1,text="Exit",font=("New times roman",15,"bold"),bg="gray",fg="red",cursor="hand2").place(x=50,y=340, width = 300)


    def login_data(self,username,password):
        if len(username) != 0 and len(password) != 0:
            if username == "admin" and password == "admin":
                messagebox.showinfo('Success', 'Congratulations!! login successfull')
                self.root.destroy()
                tk = Tk()
                dashboard.Hotel(tk)
                tk.mainloop()
            else:
                messagebox.showerror('Error', 'Invalid username and password')
                self.txt_password.focus()
                return
        elif (len(username) == 0):
            messagebox.showerror("Please enter username!")
            self.txt_username.focus()
            return
        else:
            messagebox.showerror("hotel Login", "Please enter password!")
            self.ent_password.focus()
            return

        

root=Tk()
obj = login(root)
root= mainloop()