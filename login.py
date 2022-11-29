from tkinter import*
from tkinter import messagebox
from PIL import ImageTk #install pillow
import sqlite3
import os
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System | Developed By Adenan Hamid Sheikh")
        self.root.geometry ("1350x700+0+0")
        self.root.config(bg="#fafafa")
#=====image===========
        self.phone_image=ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)

#======Login_Frame=================
        self.coustomer_id=StringVar()
        self.password=StringVar()

        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)

        title=Label(login_frame,text="Inventroy Management\n System",font=("Elephant",15,"bold"),bg="white").place(x=0,y=30,relwidth=1)
        lbl_user=Label(login_frame,text="Coustomer ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
       
        txt_coustomer_id=Entry(login_frame,textvariable=self.coustomer_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)
        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=190)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)

        btn_login=Button(login_frame,text="Log In",command=self.login,font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)
        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",10,"bold")).place(x=150,y=360,)
        btn_forget=Button(login_frame,text="Forget Password",font=("Arial Rounded MT Bold",10),bg="white",activebackground="#00759E",fg="#00759E",activeforeground="white",cursor="hand2").place(x=50,y=400)

#=========frame 2==================
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)
        lbl_reg=Label(register_frame,text="SUBSCRIBE  | LIKE | SHARE ",font=("times new roman",13),bg="white").place(x=0,y=19,relwidth=1)
        #p=========animation===========
        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2=ImageTk.PhotoImage(file="images/im2.png")
        self.im3=ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)
        self.animate()
   
   
    def animate(self):
            self.im=self.im1
            self.im1=self.im2
            self.im2=self.im3
            self.im3=self.im
            self.lbl_change_image.config(image=self.im)
            self.lbl_change_image.after(2000,self.animate)


    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
                if self.coustomer_id.get()=="" or self.password.get()=="":
                        messagebox.showerror("Error","All Fields are required",parrent=self.root)
                else:

                        cur.execute("select * from login where user=? AND pass=?",(self.coustomer_id.get(),self.password.get()))
                        user=cur.fetchall()
                        if user==None:
                                 messagebox.showerror("Error","Invalid USERNAME|PASSWORD",parrent=self.root)
                        
                        else:
                                self.root.destroy()
                                os.system("python dashboard.py")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parrent=self.root)
            

        
             #def forget(self):
 
     
root=Tk()
obj=Login_System(root)
root.mainloop()
