from tkinter import *
import Backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list.curselection()[0]
        selected_tuple=list.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
        e5.delete(0, END)
        e5.insert(END, selected_tuple[5])
        e6.delete(0, END)
        e6.insert(END, selected_tuple[6])
        e7.delete(0, END)
        e7.insert(END, selected_tuple[7])
    except IndexError:
        pass

def view_command():
    list.delete(0, END)
    for row in Backend.view():
        list.insert(END, row)

def search_command():
    list.delete(0, END)
    for row in Backend.search(Name_text.get(),RollNo_text.get(),Branch_text.get(),Grade_text.get(), ContactNo_text.get(), EmailId_text.get(), Address_text.get()):
        list.insert(END, row)

def add_command():
    Backend.insert(Name_text.get(),RollNo_text.get(),Branch_text.get(),Grade_text.get(), ContactNo_text.get(), EmailId_text.get(), Address_text.get())
    list.delete(0, END)
    list.insert(END,(Name_text.get(),RollNo_text.get(),Branch_text.get(),Grade_text.get(), ContactNo_text.get(), EmailId_text.get(), Address_text.get()))

def del_command():
    Backend.delete(selected_tuple[0])


def update_command():
    Backend.update(selected_tuple[0],Name_text.get(),RollNo_text.get(),Branch_text.get(),Grade_text.get(), ContactNo_text.get(), EmailId_text.get(), Address_text.get())

window = Tk()

window.wm_title("StudentSystem")

l1 = Label(window, text="Name")
l1.grid(row=0, column=0)

l2 = Label(window, text="RollNo.")
l2.grid(row=0, column=2)

l3 = Label(window, text="Branch")
l3.grid(row=1, column=0)

l4 = Label(window, text="Grade")
l4.grid(row=1, column=2)

l5 = Label(window, text="ContactNo")
l5.grid(row=2, column=0)

l6 = Label(window, text="EmailId")
l6.grid(row=2, column=2)

l7 = Label(window, text="Address")
l7.grid(row=3, column=0)

Name_text = StringVar()
e1 = Entry(window, textvariable=Name_text)
e1.grid(row=0,column=1)

RollNo_text = StringVar()
e2 = Entry(window, textvariable=RollNo_text)
e2.grid(row=0,column=3)

Branch_text = StringVar()
e3 = Entry(window, textvariable=Branch_text)
e3.grid(row=1,column=1)

Grade_text = StringVar()
e4 = Entry(window, textvariable=Grade_text)
e4.grid(row=1,column=3)

ContactNo_text = StringVar()
e5 = Entry(window, textvariable=ContactNo_text)
e5.grid(row=2,column=1)

EmailId_text = StringVar()
e6 = Entry(window, textvariable=EmailId_text)
e6.grid(row=2,column=3)

Address_text = StringVar()
e7 = Entry(window, textvariable=Address_text)
e7.grid(row=3,column=1)

list = Listbox(window,height=6,width=35)
list.grid(row=4,column=0,rowspan=6,columnspan=2)

sb = Scrollbar(window)
sb.grid(row=4, column=2, rowspan=6)

list.configure(yscrollcommand=sb.set)
sb.configure(command=list.yview)

list.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text='ViewAll', width=12,command=view_command)
b1.grid(row=4,column=3)

b2 = Button(window, text='SearchEntry', width=12,command=search_command)
b2.grid(row=5,column=3)

b3 = Button(window, text='AddEntry', width=12,command=add_command)
b3.grid(row=6,column=3)

b4 = Button(window, text='Update', width=12,command=update_command)
b4.grid(row=7,column=3)

b5 = Button(window, text='Delete', width=12,command=del_command)
b5.grid(row=8,column=3)

b6 = Button(window, text='Close', width=12,command=window.destroy)
b6.grid(row=9,column=3)

window.mainloop()