import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS coustomer(c_ID INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,adress text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS catagory(cat_id INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS product(p_ID INTEGER PRIMARY KEY AUTOINCREMENT,Catagory text,Supplier text,Name text,Price text,Qty text,Status text)")
    con.commit()
    con.execute(" CREATE TABLE IF NOT EXISTS login(user INTEGER PRIMARY KEY,pass text)")
    con.commit()

create_db()