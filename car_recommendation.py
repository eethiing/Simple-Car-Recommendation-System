from tkinter import *
from tkinter import messagebox
import tkinter.ttk as tk
import pandas as pd

# change the file path
df = pd.read_excel(r'D:\data.xlsx')

#function to add values for dropdown digits
def addInteger(data, min_val, max_val) :
    if (len(data) == 1 and data[0] == min_val) : # output -> [0, 50000]
        data.insert(0,0)
        return data
    elif (len(data) == 1 and data[0] == max_val) : # otuput -> [500000, 100000000]
        data.append(100000000)
        return data
    else :
        return data


# function to show output model of the car
def showModel(df_found):
    window = Tk()
    window.geometry('400x300')
    index = df_found.index.tolist()
    total_rows = df_found.shape[0]
    i=0
    if total_rows == 0 :
        label1 = Label(window, text='No suitable model found', font=('Aerial 14'))
        label1.pack(side=TOP, pady=6)
        button1 = tk.Button(window, text='Close', command=window.destroy)
        button1.pack(side=BOTTOM, pady=6)
    else :
        label1 = Label(window, text='Recommended Car Model : ', font=('Aerial 14 bold'))
        label1.pack()
        for i in range(total_rows):
            model = df_found['CAR MODEL'].values
            label2 = Label(window, text=model[i], font=('Aerial 14'))
            label2.pack()
            # create button to link to showOutput
        button1 = tk.Button(window, text='Close', command=window.destroy)
        button1.pack(side=BOTTOM, padx = 100, pady=10)
        button2 = tk.Button(window, text='Show Details', command=lambda :showOutput(index))
        button2.pack(side=BOTTOM, padx = 100, pady=10)

#function to show output data in table format
def showOutput(index) :
    window = Tk()
    window.geometry("1300x200")
    # get no. and name of columns
    no_cols = df.shape[1]
    #no_rows = df_found.shape[0]
    index = index
    col_names = df.columns
    i=0
    # output columns
    for j, col in enumerate(col_names):
        cols = Text(window, width=18, height=1, bg = "#9BC2E6")
        cols.grid(row=i,column=j)
        cols.insert(INSERT, col)
        cols.config(state='disabled')
        
    # output rows 
    for i in range(len(index)):
        for j in range(no_cols):
            row = Text(window, width=18, height=1)
            row.grid(row=i+1,column=j)
            row.insert(INSERT, df.loc[index[i]][j])
            row.config(state='disabled')

    if index == 0:
        text = Text(window, width=16, height=1)
        text.insert(INSERT, "No data found")
        text.grid(row=1,column=0)

    window.mainloop()
    # output rows 
    #for i in range(no_rows):
    #    for j in range(no_cols):
    #        row = Text(window, width=20, height=1)
    #        row.grid(row=i+1,column=j)
    #        row.insert(INSERT, df.loc[i][j])
    #        row.config(state='disabled')

    
#function to search for label after clicking
def find_clicked():
    # get the value and query using pandas
    p_string = price.get()
    p_int = [int(i) for i in p_string.split() if i.isdigit()] # get the digit from the string
    p_int = addInteger(p_int,50000,500000)
    ct = car_type.get()
    t = transmission.get()
    h_string = horsepower.get()
    h_int = [int(i) for i in h_string.split() if i.isdigit()]
    h_int = addInteger(h_int,200,500)
    l = local_foreign.get()
    y_string = manufactured_year.get()
    y_int = [int(i) for i in y_string.split() if i.isdigit()]
    y_int = addInteger(y_int,2010,2022)
    m_string = mileage.get()
    m_int = [int(i) for i in m_string.split() if i.isdigit()]
    m_int = addInteger(m_int,50000,500000)
    
    # check whether is all the combobox selected
    if not p_string or not ct or not t or not h_string  or not l  or not y_string or not m_string:
        messagebox.showinfo("Error", "Please ensure that all fields are selected.")
        return

    print(p_int, ct, t, h_int,l,y_int,m_int)
    df_found = df.loc[(df['PRICE'] >= p_int[0]) & (df['PRICE'] <= p_int[1]) & 
                      (df['CAR TYPE'] == ct) & (df['TRANSMISSION'] == t)  & 
                      (df['LOCAL VS FOREIGN'] == l) & (df['HORSEPOWER'] >= h_int[0]) & 
                      (df['HORSEPOWER'] <= h_int[1]) & 
                      (df['MANUFACTURED YEAR'] >= y_int[0]) & (df['MANUFACTURED YEAR'] <= y_int[1]) &  
                      (df['MILEAGE'] >= m_int[0]) & (df['MILEAGE'] <= m_int[1])] 
                      
    #print(df_found)
    showModel(df_found)
    #showOutput(df_found)

# o --> option, d--> dropdown, l--> label
o1 = ['< 50000', '50000 - 150000', '150000 - 500000', '500000 >'] # price
o2 = ['SEDAN', 'SUV', 'SUPERCAR'] # car_type
o3 = ['AUTO', 'MANUAL'] # transmission
o4 = ['LOCAL', 'FOREIGN'] # local/foreign
o5 = ['< 200', '200 - 500', '500 >'] # horsepower
o6 = ['< 2010', '2010 - 2021', '2022'] # manufactured_year
o7 = ['< 50000', '50000 - 150000', '150000 - 500000', '500000 >'] # mileage

#TKINTER
win = Tk()
win.title('Car Recommendation System')
win.geometry("715x480")
win.configure(bg='#F5AD9E')

#Set the title of the system
title = Label(win, bg='#F5AD9E', width=50, text='CAR RECOMMENDATION SYSTEM ', font='Helvetica 18 bold').place(x=0 , y=20) 

#datatype of menu text
price = StringVar()
car_type = StringVar()
transmission = StringVar()
horsepower = StringVar()
local_foreign = StringVar()
manufactured_year = StringVar()
mileage = StringVar()

l1 = Label(win, bg='#F5AD9E', width=50, text='Price Range').place(x=0 , y=70)
d1 = tk.Combobox(win, width=50,state='readonly', textvariable = price, values=o1).place(x=250, y =70)

l2 = Label(win, bg='#F5AD9E', width=50, text='Car Type').place(x=0 , y=120)
d2 = tk.Combobox(win, width=50,state='readonly', textvariable = car_type, values=o2).place(x=250, y =120)

l3 = Label(win, bg='#F5AD9E', width=50, text='Transmission').place(x=0 , y=170)
d3 = tk.Combobox(win, width=50,state='readonly',textvariable = transmission, values=o3).place(x=250, y =170)

l4 = Label(win, bg='#F5AD9E', width=50, text='Local/Foreign').place(x=0 , y=220)
d4 = tk.Combobox(win, width=50,state='readonly',textvariable = local_foreign, values=o4).place(x=250, y =220)

l5 = Label(win, bg='#F5AD9E', width=50, text='Horsepower').place(x=0 , y=270)
d5 = tk.Combobox(win, width=50,state='readonly',textvariable = horsepower, values=o5).place(x=250, y =270)

l6 = Label(win, bg='#F5AD9E', width=50, text='Manufactured Year').place(x=0 , y=320)
d6 = tk.Combobox(win, width=50,state='readonly',textvariable = manufactured_year, values=o6).place(x=250, y =320)

l7 = Label(win, bg='#F5AD9E', width=50, text='Mileage (km)').place(x=0 , y=370)
d7 = tk.Combobox(win, width=50,state='readonly',textvariable = mileage, values=o7).place(x=250, y =370)

submit_b = tk.Button(win,text='Find', command=find_clicked).place(x=300, y=420)
win.mainloop()

