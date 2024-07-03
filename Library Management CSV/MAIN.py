from tkinter.messagebox import showinfo
import numpy
import pandas as pd
from tkinter import *
from numpy import array
import os

book_path = 'book.csv'
borrow_path = 'borrower_details.csv'

def borrow():
    borrow_name = e1.get()
    borrow_bookname = e2.get()
    borrow_class = e3.get()
    borrow_roll = e4.get()
    try:
        try:
            df3 = pd.read_csv(book_path, index_col='Name')
            df3 = df3.drop([borrow_bookname])
            
            df3.to_csv(book_path)
            top_up4.destroy()

            if os.path.exists(borrow_path):
                df2 = pd.read_csv(borrow_path)

                dict2 = {
                    'Name':[borrow_name],
                    'Book':[borrow_bookname],
                    'class':[borrow_class],
                    'Roll No':[borrow_roll]
                }
                df1 = pd.DataFrame(dict2)

                df2 = df2.append(df1)
                df2.to_csv(borrow_path, index=False)
            else:
                dict2 = {
                    'Name':[borrow_name],
                    'Book':[borrow_bookname],
                    'class':[borrow_class],
                    'Roll No':[borrow_roll]
                }
                df1 = pd.DataFrame(dict2)
                df1.to_csv(borrow_path, index=False)
        
        except:
            showinfo('Invalid','Book is not available')
            top_up4.destroy()
    except:
        showinfo('Error',"Something got wrong")

def update():
    bookname = entry.get()
    if os.path.exists(book_path):
        df2 = pd.read_csv(book_path)
    
        dict1 = {'Name':[bookname]}
        df1 = pd.DataFrame(dict1)

        df2 = df2.append(df1)

        df2.to_csv(book_path, index=False)
        entry.delete(0, END)
    else:
        dict1 = {'Name':[bookname]}
        df1 = pd.DataFrame(dict1)
        df1.to_csv(book_path, index=False)
        entry.delete(0, END)

def enter_books():
    def check():
        def exit():
            top_up2.destroy()

        uservalue = username.get()
        passvalue = password.get()

        if uservalue == 'Admin' and passvalue == '123456':
            top_up1.destroy()
            global top_up2
            top_up2 = Toplevel()
            top_up2.geometry('400x500')
            top_up2.maxsize(400, 500)
            top_up2.configure(bg='cyan')

            frame1 = Frame(top_up2)
            frame1.pack()

            label1 = Label(top_up2,text='BookName', bg='cyan', font='cosmic 15 bold')
            label1.place(x=50, y=50)
            global entry
            entry = Entry(top_up2,)
            entry.place(y=55, x=180)

            

            b1 = Button(top_up2,text='    Done    ', relief=GROOVE, font='cosmic 12 bold', bg='cyan', command=update)
            b1.place(x=160, y= 100)
            b2 = Button(top_up2,text='    EXIT    ', relief=GROOVE, font='cosmic 12 bold', bg='cyan', command=exit)
            b2.place(x=160, y= 150)

        else:
            showinfo('invalid', 'username or password invalid')

    top_up1 = Toplevel(faru)
    top_up1.geometry('400x300')
    frame1 = Frame(top_up1)
    frame1.grid()
    label1 = Label(frame1, text='Username', font='cosmic 15 bold')
    label1.grid()
    label2 = Label(frame1, text='password', font='cosmic 15 bold')
    label2.grid()

    username = Entry(frame1)
    password = Entry(frame1, show='*')
    username.grid(column=2, row=0)
    password.grid(column=2, row=1)

    button1 = Button(frame1, text="DONE", command=check).grid(column=2, row=5)
    
    

def available_books():
    try:
        df = pd.read_csv(book_path)
        df.T
        top_up3 = Toplevel()
        top_up3.geometry('300x400')
        top_up3.configure(bg='cyan')
        frame1 = Frame(top_up3)
        frame1.pack()
        label1 = Listbox(frame1)
        label1.grid()

        df = df['Name'].tolist()

        df = numpy.array(df)
        for i in (df):
            label1.insert(END, i)
    except:
        showinfo('Error', 'Sorry, We dont have books currently') 

def borrow_book():
    def end():
        top_up4.destroy()
    global top_up4
    top_up4 = Toplevel()
    top_up4.geometry('500x600')
    top_up4.configure(bg='maroon')
    top_up4.maxsize(500, 600)
    frame5 = Frame(top_up4)
    frame5.pack()
    l1 = Label(top_up4, text='Your Name', bg="maroon", fg='white',font='cosmic 12 bold')    
    l2 = Label(top_up4, text='Book Name', bg="maroon", fg='white',font='cosmic 12 bold')    
    l3 = Label(top_up4, text='Class & Section', bg="maroon", fg='white',font='cosmic 12 bold')    
    l4 = Label(top_up4, text='Roll No', bg="maroon", fg='white',font='cosmic 12 bold')    
    l1.place(x=20, y=50)
    l2.place(x=20, y=100)
    l3.place(x=20, y=150)
    l4.place(x=20, y=200)

    global e1
    global e2
    global e3
    global e4

    e1 = Entry(top_up4)
    e2 = Entry(top_up4)
    e3 = Entry(top_up4)
    e4 = Entry(top_up4)
    e1.place(x=170, y=50)
    e2.place(x=170, y=100)
    e3.place(x=170, y=150)
    e4.place(x=170, y=200)

    b1 = Button(top_up4, text=' Borrow ', bg='maroon', relief=RAISED, font='cosmic 13 bold', command=borrow)
    b2 = Button(top_up4, text='    Exit    ', bg='maroon', relief=RAISED, font='cosmic 13 bold', command=end)
    b1.place(x=50, y=250)
    b2.place(x=200, y=250)


def return_book():
    def exit():
        top_up5.destroy()

    def updating_return():
        entry1_value = entry1.get()
        entry2_value = entry2.get()
        df3 = pd.read_csv(borrow_path)
        try:
            df3 = df3.drop(df3[(df3.Name == entry1_value) & (df3.Book == entry2_value)].index)
            showinfo('Thankyou','Hope you enjoyed this book')
            
        except:
            top_up5.destroy()
            showinfo('error','something got wrong')
            
        else:
            df3.to_csv(borrow_path, index=False)

            if os.path.exists(book_path):
                df2 = pd.read_csv(book_path)

                dict1 = {'Name':[entry2_value]}
                df1 = pd.DataFrame(dict1)

                df2 = df2.append(df1)

                df2.to_csv(book_path, index=False)

            else:
                dict1 = {'Name':[entry2_value]}
                df1 = pd.DataFrame(dict1)
                df1.to_csv(book_path, index=False)

            top_up5.destroy()

    top_up5 = Toplevel()
    top_up5.geometry('300x400')
    top_up5.configure(bg='lightblue1')

    l1 = Label(top_up5, text='Your Name', font='cosmic 13 bold', bg='lightblue1')
    label2 = Label(top_up5, text='Book Name', font='cosmic 13 bold', bg='lightblue1')
    l1.place(x=20, y=50)
    label2.place(x=20, y=100)

    entry1 = Entry(top_up5)
    entry2 = Entry(top_up5)
    entry1.place(x=130, y=50)
    entry2.place(x=130, y=100)

    b1 = Button(top_up5, text='   Done   ', bg='lightblue1', relief=RAISED, command=updating_return)
    b2 = Button(top_up5, text='   Exit   ', bg='lightblue1', relief=RAISED, command=exit)
    b1.place(x=40,y=200)
    b2.place(x=190,y=200)

def exit():
    faru.destroy()

faru = Tk()
faru.geometry('500x600')
faru.maxsize(500, 600)
faru.title('DMS LIBRARY')
faru.configure(bg='grey')

frame1 = Frame(faru)
frame1.pack()

label1 = Label(text='WELCOME TO DMS LIBRARY', fg='red',bg='black', font = 'cosmic 20')
label1.place(x=60, y=100)

button1 = Button(faru, text='Enter New Book',fg='cyan', bg= 'black', relief=GROOVE, font='cosmic 12 bold', padx=10, command=enter_books)
button1.place(x=184, y=160)

button2 = Button(faru, text='Available Books',fg='cyan', bg= 'black', relief=GROOVE, font='cosmic 12 bold', padx=10, command=available_books)
button2.place(x=184, y=220)

button3 = Button(faru, text='Borrow Book',fg='cyan', bg= 'black', relief=GROOVE, font='cosmic 12 bold', padx=10, command=borrow_book)
button3.place(x=192, y=280)

button4 = Button(faru, text='Return Book',fg='cyan', bg= 'black', relief=GROOVE, font='cosmic 12 bold', padx=10, command=return_book)
button4.place(x=195, y=340)

button5 = Button(faru, text='Exit',fg='cyan', bg= 'black', relief=GROOVE, font='cosmic 12 bold', padx=10, command=exit)
button5.place(x=225, y=400)


faru.mainloop()
