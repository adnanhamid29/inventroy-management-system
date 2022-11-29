from tkinter import*
#from PIL import Image, ImageTk #pipinstall pillow
from tkinter import ttk,messagebox
import sqlite3
class catagoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("inventroy Management System |developed by Adnan , Moein and Shahnawaz")
        self.root.config(bg="white")
        self.root.focus_force()
        #####++++Variables++++++++++
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        #========title=========
        lbl_title=Label(self.root,text="Manage Product Catagory",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)

        lbl_name=Label(self.root,text="Enter Catagory Name",font=("goudy old style",30),bg="white").place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",18),bg="light yellow").place(x=50,y=170,width=300)
        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",18,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("goudy old style",18,"bold"),bg="red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)
        #==========CATAGORY DETAILS================


        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=100)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.catagoryTable=ttk.Treeview(cat_frame,columns=("cat_id","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=Y)
        scrolly.pack(side=RIGHT,fill=X)
        scrollx.config(command=self.catagoryTable.xview)
        scrolly.config(command=self.catagoryTable.yview)

        self.catagoryTable.heading("cat_id",text="C ID")
        self.catagoryTable.heading("name",text="name")
  
        self.catagoryTable["show"]="headings"
       
        self.catagoryTable.column("cat_id",width=90)
        self.catagoryTable.column("name",width=100)
        
       
        self.catagoryTable.pack(fill=BOTH,expand=1)

        self.catagoryTable.bind("<ButtonRelease-1>",self.get_data)

       #===========images=====
        #self.im1=Image.open("images/cat.jpg")
        #self.im1=self.im1.resize((500,250),Image.ANTIALIAS)
        #self.im1=ImageTk.PhotoImage(self.im1)

        #self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        #self.lbl_im1.place(x=50,y=220)
        #self.im2=Image.open("images/category.jpg")
        #self.im2=self.im2.resize((500,250),Image.ANTIALIAS)
        #self.im2=ImageTk.PhotoImage(self.im2)

        #self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        #self.lbl_im2.place(x=580,y=220)

        self.show()
        ###===============functions============
          
    def add(self):  
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if  self.var_name.get()=="":
                     messagebox.showerror("Error","Catagory Name Must be Required",parent=self.root)
            else:
                cur.execute("select * from catagory where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Catagory  already assigned, try different",parent=self.root)
                else:
                    cur.execute("insert into catagory (name) values(?)",(self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Sucess","Catagory added Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {(ex)}",parent=self.root)   

    def show(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("select * from catagory") 
                rows=cur.fetchall()
                self.catagoryTable.delete(*self.catagoryTable.get_children())
                for row in rows:
                    self.catagoryTable.insert('',END,values=row)

            except Exception as ex:
                 messagebox.showerror("Error",f"Error due to : {(ex)}",parent=self.root)    

    def get_data(self,ev):
        f=self.catagoryTable.focus()
        content=(self.catagoryTable.item(f))
        row=content['values']
        
        
        self.var_cat_id.set(row[0]),
        self.var_name.set(row[1]),

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()

        try:
            if self.var_cat_id.get()=="":  
                messagebox.showerror("Error","Catagory Must be Required",parrent=self.root)
            else:
                cur.execute("Select * from catagory where cat_id=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","invalid Catagory",parent=self.root)
                else:
                   op=messagebox.askyesno("Confirm","do you realy want to delete")
                   if op==True:     
                        cur.execute("delete from catagory where cat_id=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("delete","catagory deleted Sucessfully",parent=self.root)
                        self.show()
                        self.var_cat_id.set("1.0",END)
                        self.var_name.set("")
                        
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {(ex)}",parent=self.root)   

       


if __name__=="__main__":

    root=Tk()
    obj=catagoryClass(root)
    root.mainloop()
        