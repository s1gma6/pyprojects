import tkinter as tk
from tkinter import Label, Button
import time

localtime = time.asctime(time.localtime(time.time()))

def display(num):
    number = 0
    number += num

class App1:

    def __init__(self, top):
        self.top = top
        top.title("Restaurant Management")
        top.geometry("1028x500")
        top.configure(background="#333333")
        fonttitle = "{Ubuntu Mono} 25 bold" 
        fontsmall = "{Ubuntu Mono} 15 bold"
        fontsmallxs = "{Ubuntu Mono} 8 normal"
    
        #____________________Info Food____________________

        self.Label1 = tk.Label(master=top, text='Restaurant Management System'.upper(), background="#333333", foreground="#E95420", font=fonttitle)
        self.Label1.place(relx=0.268, rely=0.02, height=51, width=507)
        
        localtime1 = Label(master=top, text=localtime, background="#333333", foreground="#E95420")
        localtime1.place(relx=0.420, rely=0.12)

        #____________________Label Food____________________
        self.label112 = tk.Label(master=top, text='Order Num'.upper(), background="#333333", fg="white", font=fontsmall)
        self.label112.place(relx=0.054, rely=0.25)
        self.label112 = tk.Label(master=top, text='Aloo Curry'.upper(), background="#333333", fg="white", font=fontsmall)
        self.label112.place(relx=0.054, rely=0.31)
        self.label112 = tk.Label(master=top, text='Chicken Curry'.upper(), background="#333333", fg="white", font=fontsmall)
        self.label112.place(relx=0.054, rely=0.37)
        self.label112 = tk.Label(master=top, text='Veg Biriyani'.upper(), background="#333333", fg="white", font=fontsmall)
        self.label112.place(relx=0.054, rely=0.43)
        self.label112 = tk.Label(master=top, text='Malai Icecream'.upper(), background="#333333", fg="white", font=fontsmall)
        self.label112.place(relx=0.054, rely=0.49)
        self.label112 = tk.Label(master=top, text='Mango Juice'.upper(), background="#333333", fg="white", font=fontsmall)
        self.label112.place(relx=0.054, rely=0.55)
        self.label112 = tk.Label(master=top, text='Masala Chai'.upper(), background="#333333", fg="white", font=fontsmall)
        self.label112.place(relx=0.054, rely=0.61)

        
        #____________________Entry of Food____________________
        self.entry1 = tk.Entry(master=top, background="#222222", foreground="WHITE",font=fontsmall)
        self.entry1.place(relx = 0.22, rely = 0.25)
        self.entry1 = tk.Entry(master=top, background="#222222", foreground="WHITE",font=fontsmall)
        self.entry1.place(relx = 0.22, rely = 0.31)
        self.entry1 = tk.Entry(master=top, background="#222222", foreground="WHITE",font=fontsmall)
        self.entry1.place(relx = 0.22, rely = 0.37)
        self.entry1 = tk.Entry(master=top, background="#222222", foreground="WHITE",font=fontsmall)
        self.entry1.place(relx = 0.22, rely = 0.43)
        self.entry1 = tk.Entry(master=top, background="#222222", foreground="WHITE",font=fontsmall)
        self.entry1.place(relx = 0.22, rely = 0.49)
        self.entry1 = tk.Entry(master=top, background="#222222", foreground="WHITE",font=fontsmall)
        self.entry1.place(relx = 0.22, rely = 0.55)
        self.entry1 = tk.Entry(master=top, background="#222222", foreground="WHITE",font=fontsmall)
        self.entry1.place(relx = 0.22, rely = 0.61)


        #____________________Calculator____________________
        self.entry1 = tk.Entry(master=top, background="#222222", foreground="WHITE",font=fontsmall)
        self.entry1.place(relx = 0.705, rely = 0.24, height=35, relwidth=0.267)

        self.Button1 = tk.Button(master=top, text='''7''', background="gray", font=fontsmall, borderwidth=0, fg="white", command=lambda: display(7))
        self.Button1.place(relx=0.705, rely=0.34, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''8''', background="gray", font=fontsmall, borderwidth=0, fg="white", command=lambda: display(8))
        self.Button1.place(relx=0.775, rely=0.34, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''9''', background="gray", font=fontsmall, borderwidth=0, fg="white", command=lambda: display(9))
        self.Button1.place(relx=0.845, rely=0.34, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''6''', background="gray", font=fontsmall, borderwidth=0, fg="white", command=lambda: display(6))
        self.Button1.place(relx=0.705, rely=0.44, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''5''', background="gray", font=fontsmall, borderwidth=0, fg="white", command=lambda: display(5))
        self.Button1.place(relx=0.775, rely=0.44, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''4''', background="gray", font=fontsmall, borderwidth=0, fg="white", command=lambda: display(4))
        self.Button1.place(relx=0.845, rely=0.44, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''3''', background="gray", font=fontsmall, borderwidth=0, fg="white", command=lambda: display(3))
        self.Button1.place(relx=0.705, rely=0.54, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''2''', background="gray", font=fontsmall, borderwidth=0, fg="white", command=lambda: display(2))
        self.Button1.place(relx=0.775, rely=0.54, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''1''', background="gray", font=fontsmall, borderwidth=0, fg="white", command=lambda: display(1))
        self.Button1.place(relx=0.845, rely=0.54, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''0''', background="gray", font=fontsmall, borderwidth=0, fg="white", command=lambda: display(0))
        self.Button1.place(relx=0.705, rely=0.64, height=44, width=139)
        
        self.Button1 = tk.Button(master=top, text='''/''', background="gray", font=fontsmall, borderwidth=0, fg="white", command=lambda: display("/"))
        self.Button1.place(relx=0.915, rely=0.34, height=44, width=58)
        self.Button1 = tk.Button(master=top, text='''*''', background="gray", font=fontsmall, borderwidth=0, fg="white", command=lambda: display("*"))
        self.Button1.place(relx=0.915, rely=0.44, height=44, width=58)
        self.Button1 = tk.Button(master=top, text='''+''', background="gray", font=fontsmall, borderwidth=0, fg="white", command=lambda: display("+"))
        self.Button1.place(relx=0.915, rely=0.54, height=44, width=58)
        self.Button1 = tk.Button(master=top, text='''-''', background="gray", font=fontsmall, borderwidth=0, fg="white", command=lambda: display("-"))
        self.Button1.place(relx=0.915, rely=0.64, height=44, width=58)
        self.Button1 = tk.Button(master=top, text='''.''', background="gray", font=fontsmall, borderwidth=0, fg="white", command=lambda: display("."))
        self.Button1.place(relx=0.845, rely=0.64, height=44, width=67)

        self.Button1 = tk.Button(master=top, text='''=''', background="gray", font=fontsmall, borderwidth=0, fg="white", command=lambda: display("="))
        self.Button1.place(relx=0.705, rely=0.74, height=44, width=274)

        #____________________Cost____________________
        self.label112 = tk.Label(master=top, text='Cost :'.upper(), background="#333333", fg="white", font=fontsmall)
        self.label112.place(relx=0.45, rely=0.28)
        self.label112 = tk.Label(master=top, text='GST :'.upper(), background="#333333", fg="white", font=fontsmall)
        self.label112.place(relx=0.45, rely=0.38)
        self.label112 = tk.Label(master=top, text='Service :'.upper(), background="#333333", fg="white", font=fontsmall)
        self.label112.place(relx=0.45, rely=0.48)
        self.label112 = tk.Label(master=top, text='Total :'.upper(), background="#333333", fg="white", font=fontsmall)
        self.label112.place(relx=0.45, rely=0.58)

        #____________________Cost____________________
        self.entry1 = tk.Entry(master=top, background="#222222", foreground="WHITE",font=fontsmallxs)
        self.entry1.place(relx = 0.57, rely = 0.29)
        self.entry1 = tk.Entry(master=top, background="#222222", foreground="WHITE",font=fontsmallxs)
        self.entry1.place(relx = 0.57, rely = 0.39)
        self.entry1 = tk.Entry(master=top, background="#222222", foreground="WHITE",font=fontsmallxs)
        self.entry1.place(relx = 0.57, rely = 0.49)
        self.entry1 = tk.Entry(master=top, background="#222222", foreground="WHITE",font=fontsmallxs)
        self.entry1.place(relx = 0.57, rely = 0.59)

        #____________________Button Controls____________________
        
        self.Button2 = tk.Button(master=top, text='PRICE', background="#E95420", font=fontsmall, fg="white", command=lambda: display(0))
        self.Button2.place(relx=0.039, rely=0.86, height=34, width=107)        
        self.Button2 = tk.Button(master=top, text='TOTAL', background="#E95420", font=fontsmall, fg="white", command=lambda: display(0))
        self.Button2.place(relx=0.156, rely=0.86, height=34, width=107)
        self.Button2 = tk.Button(master=top, text='RESET', background="#E95420", font=fontsmall, fg="white", command=lambda: display(0))
        self.Button2.place(relx=0.272, rely=0.86, height=34, width=107)
        self.Button2 = tk.Button(master=top, text='EXIT', background="#E95420", font=fontsmall, fg="white", command=self.Button2.quit)
        self.Button2.place(relx=0.389, rely=0.86, height=34, width=107)



root = tk.Tk()
my_gui = App1(root)
root.mainloop()
