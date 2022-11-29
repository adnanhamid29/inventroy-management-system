from tkinter import*
#from PIL import Image,ImageTk #pipinstall pillow
from tkinter import ttk,messagebox
import sqlite3
class coustomerClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("inventroy Management System |developed by Adnan , Moein and Shahnawaz")
        self.root.config(bg="white")
        self.root.focus_force()
#=========all variables===========
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_coust_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_adress=StringVar()
        self.var_password=StringVar()
        #self.var_utype=StringVar()
#========================search frame=============
        SearchFrame=LabelFrame(self.root,text="Search Coustomer",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

#===============options=========
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)
        
#========title========
        title=Label(self.root,text="Coustomer Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)
#==========content===============
#===row1=====
        lbl_coustid=Label(self.root,text="Cust id",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)

        txt_coustid=Entry(self.root,textvariable=self.var_coust_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
        
        #txt_gender=Entry(self.root,textvariable=self.var_coust_id,font=("goudy old style",15),bg="lightyellow").place(x=500,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","male","female",),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180) 
#====================row2============
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_adress=Label(self.root,text="Adress",font=("goudy old style",15),bg="white").place(x=350,y=190)
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=750,y=190)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
        self.txt_adress=Entry(self.root,textvariable=self.var_adress,font=("goudy old style",15),bg="lightyellow")
        self.txt_adress.place(x=500,y=190,width=180)
        
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)
#========== row 3========================
        #lbl_utype=Label(self.root,text="User type",font=("goudy old style",15),bg="white").place(x=50,y=230)
       # cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("admin","coustomer"),state='readonly',justify=CENTER,font=("goudy old style",15))
        #cmb_utype.place(x=150,y=230,width=180)
       # cmb_utype.current(0)

#====buttons====
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)

#=========Coustomer details==============
        coust_frame=Frame(self.root,bd=3,relief=RIDGE)
        coust_frame.place(x=0,y=350,relwidth=1,height=150)
        scrolly=Scrollbar(coust_frame,orient=VERTICAL)
        scrollx=Scrollbar(coust_frame,orient=HORIZONTAL)

        self.CoustomerTable=ttk.Treeview(coust_frame,columns=("c_ID","name","email","gender","contact","adress","utype"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CoustomerTable.yview)
        scrollx.config(command=self.CoustomerTable.xview)

        self.CoustomerTable.heading("c_ID",text="cust ID")
        self.CoustomerTable.heading("name",text="name")
        self.CoustomerTable.heading("email",text="email")
        self.CoustomerTable.heading("gender",text="gender")
        self.CoustomerTable.heading("contact",text="contact")
        self.CoustomerTable.heading("adress",text="adress")
       # self.CoustomerTable.heading("utype",text="utype")
        self.CoustomerTable["show"]="headings"

        self.CoustomerTable.column("c_ID",width=90)
        self.CoustomerTable.column("name",width=150)
        self.CoustomerTable.column("email",width=150)
        self.CoustomerTable.column("gender",width=150)
        self.CoustomerTable.column("contact",width=150)
        self.CoustomerTable.column("adress",width=150)
        #self.CoustomerTable.column("utype",width=100)
        self.CoustomerTable.pack(fill=BOTH,expand=1)

        self.CoustomerTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
#==========================================================================


    
    def add(self):  
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_coust_id.get()=="":  
                messagebox.showerror("Error","Coustmer ID Must be Required",parrent=self.root)
            else:
                cur.execute("Select * from coustomer where c_ID=?",(self.var_coust_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This coustomer id already assigned, try different",parent=self.root)
                else:
                    cur.execute("insert into coustomer(c_ID,name,email,gender,contact,adress) values(?,?,?,?,?,?)",(
                                        self.var_coust_id.get(),
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),
                                        self.txt_adress.get(),
                                        #self.var_utype.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess","Coustomer added Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {(ex)}",parent=self.root)     

    def show(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("select * from coustomer") 
                rows=cur.fetchall()
                self.CoustomerTable.delete(*self.CoustomerTable.get_children())
                for row in rows:
                        self.CoustomerTable.insert('',END,values=row)

            except Exception as ex:
                 messagebox.showerror("Error",f"Error due to : {(ex)}",parent=self.root)     
    def get_data(self,ev):
        f=self.CoustomerTable.focus()
        content=(self.CoustomerTable.item(f))
        row=content['values']
        
        
        self.var_coust_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        #self.txt_adress.delete('1.0',END),
        self.txt_adress.insert(END,row[5])
        #self.var_utype.set(row[6])


    def update(self):  
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_coust_id.get()=="":  
                messagebox.showerror("Error","Coustmer ID Must be Required",parrent=self.root)
            else:
                cur.execute("Select * from coustomer where c_ID=?",(self.var_coust_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","invalid coustomer ID",parent=self.root)
                else:
                    cur.execute("Update coustomer set name=?,email=?,gender=?,contact=?,adress=? where c_ID=?",(
                                       
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),
                                        self.txt_adress.get(),
                                       # self.var_utype.get(),
                                        self.var_coust_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess","Coustomer updated Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {(ex)}",parent=self.root)   




    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()

        try:
            if self.var_coust_id.get()=="":  
                messagebox.showerror("Error","Coustmer ID Must be Required",parrent=self.root)
            else:
                cur.execute("Select * from coustomer where c_ID=?",(self.var_coust_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","invalid coustomer ID",parent=self.root)
                else:
                   op=messagebox.askyesno("Confirm","do you realy want to delete")
                   if op==True:     
                        cur.execute("delete from coustomer where c_ID=?",(self.var_coust_id.get(),))
                        con.commit()
                        messagebox.showinfo("delete","coustomer deleted Sucessfully",parent=self.root)
                        self.show()

                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {(ex)}",parent=self.root)   



    def clear(self): 
        self.var_coust_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("select"),
        self.var_contact.set(""),
        #self.txt_adress.delete('1.0',END),
        self.var_adress.set("")
        #self.var_utype.set("admin")
        self.var_searchtxt.set("")
        self.show()   
        
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
               if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search by option",parent=self.root)
               elif self.var_searchtxt.get()=="":
                    messagebox.showerror("Error","Search should be required",parent=self.root)

               else:
                        cur.execute("select * from coustomer where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'") 
                        rows=cur.fetchall()
                        if len(rows)!=0:

                                self.CoustomerTable.delete(*self.CoustomerTable.get_children())
                                for row in rows:
                                      self.CoustomerTable.insert('',END,values=row)
                        else:
                                messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
                 messagebox.showerror("Error",f"Error due to : {(ex)}",parent=self.root)   
   
if __name__=="__main__":

    root=Tk()
    obj=coustomerClass(root)
    root.mainloop()
        