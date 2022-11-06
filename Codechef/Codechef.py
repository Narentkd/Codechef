#importing necessary libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#creating a window
root =Tk()
bg=PhotoImage(file="C:/Users/snktg/Desktop/qgimage1.png")
mylabel=Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
height= root.winfo_screenheight()
width=root.winfo_screenwidth()
root.title("SRM TIME TABLE")
#root.iconbitmap("C:/Users/snktg/Desktop/icon.ico")
root.geometry("%dx%d" % (width, height))


# Create an object of Style widget
style = ttk.Style()
style.theme_use("clam")
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold'),background="black")
style.map("Treeview", background=[('selected','aquamarine4')])


# Add a Treeview widget
frame1 = LabelFrame(root)
frame1.pack()
tree=ttk.Treeview(frame1, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings")

#entering the headings to the table which is the periods
tree.heading(1, text="Period/Day")
tree.heading(2, text="1")
tree.heading(3, text="2")
tree.heading(4, text="3")
tree.heading(5, text="4")
tree.heading(6, text="5")
tree.heading(7, text="6")
tree.heading(8, text="7")
tree.heading(9, text="8")

#entering data
tree.insert('', 'end', text=1, values=('Monday','CLA','CE','VAC','VAC','PPS','CB','EVS','SPCM'))
tree.insert('', 'end', text=2, values=('Tuesday','POE','POE','PSP','PSP','SPCM','CLA','CE',''))
tree.insert('', 'end', text=3, values=('Wednesday','WS','WS','WS','CE','SPCM','SPCM','',''))
tree.insert('', 'end', text=4, values=('Thursday','SPCM','PPS','CB','CLA','SPCM','POE','COUNSELLING'))
tree.insert('', 'end', text=5, values=('Friday','PPS','WS','PPS','PPS','CLA','LIBRARY','',''))

#alignment of data and the heading cell size
tree.column("# 1",stretch=NO, anchor=CENTER,minwidth=25, width=73)
tree.column("# 2",stretch=NO, anchor=CENTER,minwidth=80, width=125)
tree.column("# 3",stretch=NO, anchor=CENTER)
tree.column("# 4",stretch=NO, anchor=CENTER)
tree.column("# 5",stretch=NO, anchor=CENTER)
tree.column("# 6",stretch=NO, anchor=CENTER)
tree.column("# 7",stretch=NO, anchor=CENTER)
tree.column("# 8",stretch=NO, anchor=CENTER)
tree.column("# 9",stretch=NO, anchor=CENTER,minwidth=80, width=125)

tree.pack()

root.mainloop()
