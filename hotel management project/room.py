from tkinter import*
from tokenize import Double
from turtle import right
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Roombooking:

    def __init__(self, root):

        self.root = root
        self.root.title("HOTEL Management System")
        self.root.geometry("1295x550+230+220")

#   variables

        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        # Title>>>>>>>>

        lbl_title = Label(self.root, text="RoomBooking DETAILS", font=(
            "times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # <<<< LOGO>>>>

        img2 = Image.open(
            r"C:\Users\91787\Desktop\hotel management project\images.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        # label frame>>>>>>>

        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking Details", font=(
            "times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # <<<<<<<<< labels and entry>>>>>>>>>>
        # customer contact

        lbl_cust_contact = Label(labelframeleft, text="customer contact", font=(
            "arial", 13, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        enty_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact, width=20, font=(
            "times new roman", 13, "bold"))
        enty_contact.grid(row=0, column=1, sticky=W)

        #  fetch data button

        btnfetchData = Button(labelframeleft, command=self.fetch_contact, text="fetchData", font=(
            "arial", 8, "bold"), bg="black", fg="gold", width=8)
        btnfetchData.place(x=347, y=4)

        # check_in Date

        check_in_date = Label(labelframeleft, text="check_in_date", font=(
            "arial", 13, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date = ttk.Entry(
            labelframeleft, textvariable=self.var_checkin, width=29, font=("times new roman", 13, "bold"))
        txtcheck_in_date.grid(row=1, column=1,)

        # check_out Date

        lbl_check_out_date = Label(labelframeleft, text="check_out_date", font=(
            "arial", 13, "bold"), padx=2, pady=6)
        lbl_check_out_date.grid(row=2, column=0, sticky=W)

        txt_check_out = ttk.Entry(labelframeleft, textvariable=self.var_checkout, width=29, font=(
            "times new roman", 13, "bold"))
        txt_check_out.grid(row=2, column=1,)

        # Room Type

        label_RoomType = Label(labelframeleft, font=(
            "arial", 12, "bold"), text="Room Type:", padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(
            host="localhost", username="root", password="1234", database="world")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        id = my_cursor.fetchall()

        combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, font=(
            "arial", 12, "bold"), width=27, state="readonly")
        combo_RoomType["value"] = id
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Available Room

        lblRoomAvailables = Label(labelframeleft, font=(
            "arial", 12, "bold"), text="Available Room:", padx=2, pady=6)
        lblRoomAvailables.grid(row=4, column=0, sticky=W)
        # txtRoomAvailable = ttk.Entry(
        #     labelframeleft, textvariable=self.var_roomavailable, font=("arial", 13, "bold"), width=29)
        # txtRoomAvailable.grid(row=4, column=1)

        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="world")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows = my_cursor.fetchall()
        combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_RoomType["value"]=rows
        combo_RoomType.current(0)
        combo_RoomType.grid(row=4, column=1)
        # Meal

        lblMeal = Label(labelframeleft, font=(
            "arial", 12, "bold"), text="Meal", padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal = ttk.Entry(labelframeleft, textvariable=self.var_meal, font=(
            "arial", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1)

        #  NO of Days

        lblNo_of_Days = Label(labelframeleft, font=(
            "arial", 12, "bold"), text="No_of_Days", padx=2, pady=6)
        lblNo_of_Days.grid(row=6, column=0, sticky=W)
        txtNo_of_Days = ttk.Entry(labelframeleft, textvariable=self.var_noofdays, font=(
            "arial", 13, "bold"), width=29)
        txtNo_of_Days.grid(row=6, column=1)

        #  paid Tax

        lblPaid_Tax = Label(labelframeleft, font=(
            "arial", 12, "bold"), text="Paid_Tax", padx=2, pady=6)
        lblPaid_Tax.grid(row=7, column=0, sticky=W)
        txtPaid_Tax = ttk.Entry(labelframeleft, textvariable=self.var_paidtax, font=(
            "arial", 13, "bold"), width=29)
        txtPaid_Tax.grid(row=7, column=1)

        #  sub Total

        lblSub_Total = Label(labelframeleft, font=(
            "arial", 12, "bold"), text="Sub_Total", padx=2, pady=6)
        lblSub_Total.grid(row=8, column=0, sticky=W)
        txtSub_Total = ttk.Entry(labelframeleft, textvariable=self. var_actualtotal, font=(
            "arial", 13, "bold"), width=29)
        txtSub_Total.grid(row=8, column=1)

        #  Total cost

        lblTotal_cost = Label(labelframeleft, font=(
            "arial", 12, "bold"), text="Total_cost", padx=2, pady=6)
        lblTotal_cost.grid(row=9, column=0, sticky=W)
        txtTotal_cost = ttk.Entry(labelframeleft, textvariable=self.var_total, font=(
            "arial", 13, "bold"), width=29)
        txtTotal_cost.grid(row=9, column=1)

        #  Bill Buttons

        btnBill = Button(labelframeleft, text="Bill", command=self.total, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        # buttons

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=39)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnupdate = Button(btn_frame, text="update", command=self.update, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnupdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.Delete,  font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.Reset, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        #  Right side image

        img3 = Image.open(
            r"C:\Users\91787\Desktop\hotel management project\gettyimages-1182454657-612x612.jpg")
        img3 = img3.resize((310, 290), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=730, y=50, width=367, height=290)

        #  Table frame

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE,
        text="view Details and search system", font=("arial", 12, "bold"))
        Table_Frame.place(x=420, y=280, width=800, height=490)

        # search system
        lblsearchBy = Label(Table_Frame, font=("arial", 12, "bold"),
                            text="search By:", bg="red", fg="white")
        lblsearchBy.grid(row=0, column=0, sticky=W, padx=2)
        self.search_var = StringVar()

        combo_search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=16)
        combo_search["value"] = ("Contact", "RoomNo")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, sticky=W)
        self.txt_search = StringVar()
        txtsearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, font=("arial", 13, "bold"), width=16)
        txtsearch.grid(row=0, column=2)

        btnsearch = Button(Table_Frame, text="search",command=self.  search, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnsearch.grid(row=0, column=3, padx=1)

        btnshowAll = Button(Table_Frame, text="show All",command=self.fetch_data, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnshowAll.grid(row=0, column=4, padx=1)

#   show table details

        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=650, height=150)
    # scroll Bar
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, column=("contact", "checkin", "checkout", "roomtype",
                                       "roomavailable", "meal", "noofdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Check-in")
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room Available")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noofdays", text="NoOfDays")

        self.room_table["show"] = "headings"
        self.room_table.column("contact", width=80)
        self.room_table.column("checkin", width=80)
        self.room_table.column("checkout", width=80)
        self.room_table.column("roomtype", width=80)
        self.room_table.column("roomavailable", width=80)
        self.room_table.column("meal", width=80)
        self.room_table.column("noofdays", width=80)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

#   Add button

    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="1234", database="World")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)", (

                    self.var_contact.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get()


                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "success", "room booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning(
                    "warning", f"something went wrong:{str(es)}", parent=self.root)


#   fetch data

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="1234", database="world")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()
 
#  get cursor

    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_no_of_days_set(row[6])

#    update button

    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror(
                "success", "please enter mobile number", parent=self.root)
        else:

            conn = mysql.connector.connect(
                host="localhost", username="root", password="1234", database="World")
            my_cursor = conn.cursor()
            my_cursor.execute("update world.room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s where contact=%s", (

                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofdays.get(),
                self.var_contact.get()


            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(
                "success", "room details has been update succesfully", parent=self.root)

#   delete button
    def Delete(self):
        Delete = messagebox.askyesno(
            "Hotel management system", "do u want to delete this room", parent=self.root)
        if Delete > 0:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="1234", database="World")
            my_cursor = conn.cursor()
            query = "delete from world.room where contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


#    reset button

    def Reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")


#   All DAtA fetch

    def fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror(
                "Error", "please enter contact Number", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="1234", database="World")
            my_cursor = conn.cursor()
            query = ("select Name from customer where Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror(
                    "Error", "This number not found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=455, y=55, width=300, height=180)

                lblName = Label(showDataframe, text="Name:",
                                font=("arial", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl = Label(showDataframe, text=row,
                            font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

                #  Gender

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="1234", database="world")
                my_cursor = conn.cursor()
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Gender:",
                                  font=("arial", 12, "bold"))
                lblGender.place(x=0, y=30)

                lbl2 = Label(showDataframe, text=row,
                             font=("arial", 12, "bold"))
                lbl2.place(x=90, y=30)

                # email

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="1234", database="world")
                my_cursor = conn.cursor()
                query = ("select Email from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblEmail = Label(showDataframe, text="Email:",
                                 font=("arial", 12, "bold"))
                lblEmail.place(x=0, y=60)

                lbl3 = Label(showDataframe, text=row,
                             font=("arial", 12, "bold"))
                lbl3.place(x=90, y=60)

  # search system
# kam ni kr rha h
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="world")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room  where " +str(self.search_var.get())+" Like '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
         self.room_table.delete(*self.room_table.get_children())
         for i in rows:
            self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()  


#   total Bills

    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "single"):
            q1 = float(300)
            q2 = float(400)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f" % ((q5)*0.09))
            ST = "Rs."+str("%.2f" % ((q5)))  # sub Total
            TT = "Rs."+str("%.2f" % (q5+((q5)*0.09)))  # totaltax
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "lunch" and self.var_roomtype.get() == "Double"):
            q1 = float(300)
            q2 = float(400)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f" % ((q5)*0.09))
            ST = "Rs."+str("%.2f" % ((q5)))  # sub Total
            TT = "Rs."+str("%.2f" % (q5+((q5)*0.09)))  # totaltax
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "dinner" and self.var_roomtype.get() == "laxary"):
            q1 = float(700)
            q2 = float(600)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f" % ((q5)*0.09))
            ST = "Rs."+str("%.2f" % ((q5)))  # sub Total
            TT = "Rs."+str("%.2f" % (q5+((q5)*0.09)))  # totaltax
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
