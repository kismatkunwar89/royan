from tkinter import *
from tkinter import font
from tkinter import messagebox
import dashboard


class Login_Page:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg='black')
        self.root.title('Login Page')
        self.root.geometry('450x400')
        self.root.resizable(0, 0)

        f = font.Font(size=15, slant='italic', underline=TRUE, family='arial')

        lbl_header = Label(self.root, text='Login Page:', font=('arial', 20, 'bold'), \
                           bg='yellow', fg='red')
        lbl_header.pack(side=TOP, fill=X)

        main_frame = Frame(self.root, bg='black', bd=5, relief=RAISED)
        main_frame.place(x=20, y=70, width=400, height=200)

        lbl_username = Label(main_frame, text='User Name:', font=('arial', 15, 'bold'), \
                             fg='Black', bg='deep sky blue')
        lbl_username.grid(row=0, column=0, padx=10, pady=10)

        self.ent_username = Entry(main_frame, font=('arial', 15, 'bold'))
        self.ent_username.grid(row=0, column=1)
        self.ent_username.focus_set()

        lbl_password = Label(main_frame, text='Password:', font=('arial', 15, 'bold'), \
                             fg='Black', bg='orange')
        lbl_password.grid(row=1, column=0, padx=10, pady=10)

        self.ent_password = Entry(main_frame, font=('arial', 15, 'bold'))
        self.ent_password.grid(row=1, column=1)
        def login(self):
            pass
        btn_login = Button(main_frame, text='Login', font=('arial', 15, 'bold'),command=lambda: self.login_data(self.ent_username.get(), self.ent_password.get()),bd=5, relief=RAISED)
        btn_login.place(x=150, y=120)

        btn_reset = Button(main_frame, text='Reset', font=('arial', 15, 'bold'), \
                           command=self.btn_reset_click, bd=5, relief=RAISED)
        btn_reset.place(x=250, y=120)

    def btn_reset_click(self):
        pass

    def login_data(self, username, password):
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




tk = Tk()
Login_Page(tk)
tk.mainloop()