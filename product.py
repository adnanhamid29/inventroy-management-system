
from tkinter import*
from typing import cast
#from PIL import Image,ImageTk #pipinstall pillow
from tkinter import ttk,messagebox
import sqlite3
class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("inventroy Management System |developed by Adnan , Moein and Shahnawaz")
        self.root.config(bg="white")
        self.root.focus_force()


        #==========================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_p_ID=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        

        #======frame================
        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)
        #========column1========
        title=Label(product_Frame,text="Product Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)
        lbl_catagory=Label(product_Frame,text="Catagory",font=("goudy old style",15),bg="white").place(x=30,y=60)
        lbl_supplier=Label(product_Frame,text="Supplier",font=("goudy old style",15),bg="white").place(x=30,y=110)
        lbl__name=Label(product_Frame,text="Name",font=("goudy old style",15),bg="white").place(x=30,y=160)
        lbl_price=Label(product_Frame,text="Price",font=("goudy old style",15),bg="white").place(x=30,y=210)
        lbl_quantity=Label(product_Frame,text="Quantity",font=("goudy old style",15),bg="white").place(x=30,y=260)
        lbl_status=Label(product_Frame,text="Status",font=("goudy old style",15),bg="white").place(x=30,y=310)


       
        #=======column2============
        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)
        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_sup.place(x=150,y=110,width=200)
        cmb_sup.current(0)
        txt_name=Entry(product_Frame,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=160,width=200)
        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow").place(x=150,y=210,width=200)
        txt_quantity=Entry(product_Frame,textvariable=self.var_qty,font=("goudy old style",15),bg="lightyellow").place(x=150,y=260,width=200)
        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)

        #=========buttons===========
        btn_add=Button(product_Frame,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_Frame,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_Frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_Frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)




#========================search frame=============
        SearchFrame=LabelFrame(self.root,text="Search Coustomer",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)

#===============options=========
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Catagory","Supplier","Name"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)
#=========Product Details==============
        
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)
        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.product_table=ttk.Treeview(p_frame,columns=("p_ID","Catagory","Supplier","Name","Price","Qty","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.yview)
        scrollx.config(command=self.product_table.xview)

        self.product_table.heading("p_ID",text="P_ID")
        self.product_table.heading("Catagory",text="Catagory")
        self.product_table.heading("Supplier",text="Supplier")
        self.product_table.heading("Name",text="Name")
        self.product_table.heading("Price",text="Price")
        self.product_table.heading("Qty",text="Qty")
        self.product_table.heading("Status",text="Status")
        self.product_table["show"]="headings"

        self.product_table.column("p_ID",width=90)
        self.product_table.column("Catagory",width=100)
        self.product_table.column("Supplier",width=100)
        self.product_table.column("Name",width=100)
        self.product_table.column("Price",width=100)
        self.product_table.column("Qty",width=100)
        self.product_table.column("Status",width=100)
        self.product_table.pack(fill=BOTH,expand=1)

        self.product_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()
        self.fetch_cat_sup()
        #=========================================
    def fetch_cat_sup(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:  
            cur.execute("Select name from catagory")
            cat=cur.fetchall()
            self.cat_list.append("Empty")
            self.sup_list.append("Empty")
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            
            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            if len (sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
                

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {(ex)}",parent=self.root)     


    
    def add(self):  
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or self.var_name.get()=="":  
                messagebox.showerror("Error","All fields are Required",parrent=self.root)
            else:
                cur.execute("Select * from product where Name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This product is already present, try different",parent=self.root)
                else:
                    cur.execute("insert into product (Catagory,Supplier,Name,Price,Qty,Status) values(?,?,?,?,?,?)",(
                                        self.var_cat.get(),
                                        self.var_sup.get(),
                                        self.var_name.get(),
                                        self.var_price.get(),
                                        self.var_qty.get(),
                                        self.var_status.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess","Product added Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {(ex)}",parent=self.root)     

    def show(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("select * from product") 
                rows=cur.fetchall()
                self.product_table.delete(*self.product_table.get_children())
                for row in rows:
                        self.product_table.insert('',END,values=row)

            except Exception as ex:
                 messagebox.showerror("Error",f"Error due to : {(ex)}",parent=self.root)     
    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.var_p_ID.set(row[0]),
        self.var_cat.set(row[1]),
        self.var_sup.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_status.set(row[6])                                 
        
        

    def update(self):  
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_p_ID.get()=="":  
                messagebox.showerror("Error","Please select productg from list",parrent=self.root)
            else:
                cur.execute("Select * from product where p_ID=?",(self.var_p_ID.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","invalid product ",parent=self.root)
                else:
                    cur.execute("Update product set Catagory=?,Supplier=?,Name=?,Price=?,Qty=?,Status=? where p_ID=?",(
                                       
                                        self.var_cat.get(),
                                        self.var_sup.get(),
                                        self.var_name.get(),
                                        self.var_price.get(),
                                        self.var_qty.get(),
                                        self.var_status.get(),
                                        self.var_p_ID.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess","Product updated Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {(ex)}",parent=self.root)   




    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()

        try:
            if self.var_p_ID.get()=="":  
                messagebox.showerror("Error","Select product from the list",parrent=self.root)
            else:
                cur.execute("Select * from product where p_ID=?",(self.var_p_ID.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid product",parent=self.root)
                else:
                   op=messagebox.askyesno("Confirm","Do you realy want to delete")
                   if op==True:     
                        cur.execute("delete from product where p_ID=?",(self.var_p_ID.get(),))
                        con.commit()
                        messagebox.showinfo("delete","Product deleted Sucessfully",parent=self.root)
                        self.show()

                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {(ex)}",parent=self.root)   



    def clear(self): 
        
        self.var_cat.set("Select"),
        self.var_sup.set("Select"),
        self.var_name.set(" "),
        self.var_price.set(" "),
        self.var_qty.set(" "),
        self.var_status.set("Active"),
        self.var_p_ID.set(" "),
       
        self.var_searchtxt.set("")
        self.var_searchtxt.set("Select")
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
                        cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'") 
                        rows=cur.fetchall()
                        if len(rows)!=0:

                                self.product_table.delete(*self.product_table.get_children())
                                for row in rows:
                                      self.product_table.insert('',END,values=row)
                        else:
                                messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
                 messagebox.showerror("Error",f"Error due to : {(ex)}",parent=self.root)   
   
        





        
        
if __name__=="__main__":

    root=Tk()
    obj=productClass(root)
    root.mainloop()