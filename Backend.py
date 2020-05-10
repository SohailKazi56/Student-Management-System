import sqlite3

def connect():
    conn=sqlite3.connect('studsys.db')
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS studsys(id INTEGER PRIMARY KEY,name text, rollno integer, branch text, grade text, contact integer, emailid text,address text)")
    conn.commit()
    conn.close()

def insert(name,rollno,branch,grade,contact,emailid,address):
    conn = sqlite3.connect('studsys.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO studsys VALUES(NULL,?,?,?,?,?,?,?)",(name,rollno,branch,grade,contact,emailid,address))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('studsys.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM studsys")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name="", rollno="",branch="",grade="",contact="",emailid="",address=""):
    conn = sqlite3.connect('studsys.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM studsys WHERE name=? OR rollno=? OR branch=? OR grade=? OR contact=? OR emailid=? OR address=?",(name,rollno,branch,grade,contact,emailid,address))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('studsys.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM studsys WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name,rollno,branch,grade,contact,emailid,address):
    conn = sqlite3.connect('studsys.db')
    cur = conn.cursor()
    cur.execute("UPDATE studsys SET name=?, rollno=?, branch=?, grade=?, contact=?, emailid=?, address=?  WHERE id=?", (name,rollno,branch,grade,contact,emailid,address,id))
    conn.commit()
    conn.close()


connect()
#insert("the success story 3 ","sk",2020,9988776655)
#delete(3)
#update(4,"fuck buddy","unknown",2017,112122312)
#print(view())
#print(search(author="sohail "))