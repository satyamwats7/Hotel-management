from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class DetailsRoom:

    def __init__(self, root):

        self.root = root
        self.root.title("HOTEL Management System")
        self.root.geometry("1295x550+230+220")

        # Title>>>>>>>>

        lbl_title = Label(self.root, text="RoomBooking DETAILS", font=(
            "times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # <<<< LOGO>>>>

        img2 = Image.open(
            r"C:\Users\91787\Desktop\hotel management project\1200px-Nyumbani_Hotel_Logo - Copy - Copy.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        # label frame>>>>>>>

        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", font=(
            "times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=540, height=350)

        # <<<<<<<<< labels and entry>>>>>>>>>>
        # Floor

        lbl_floor = Label(labelframeleft, text="floor", font=(
            "arial", 13, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)

        self.var_floor = StringVar()
        enty_floor = ttk.Entry(labelframeleft, textvariable=self.var_floor, width=20, font=(
            "times new roman", 13, "bold"))
        enty_floor.grid(row=0, column=1, sticky=W)

        #  Room No

        lbl_RoomNO = Label(labelframeleft, text="Room No",
                           font=("arial", 13, "bold"), padx=2, pady=6)
        lbl_RoomNO.grid(row=1, column=0, sticky=W)
        self.var_roomno = StringVar()
        enty_RoomNo = ttk.Entry(labelframeleft, textvariable=self.var_roomno, width=20, font=(
            "times new roman", 13, "bold"))
        enty_RoomNo.grid(row=1, column=1, sticky=W)

        # Room TYpe

        lbl_RoomType = Label(labelframeleft, text="RoomType", font=(
            "arial", 13, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W)
        self.var_RoomType = StringVar()
        enty_RoomType = ttk.Entry(labelframeleft, textvariable=self.var_RoomType, width=20, font=(
            "times new roman", 13, "bold"))
        enty_RoomType.grid(row=2, column=1, sticky=W)

        # Buttons

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=39)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnupdate = Button(btn_frame, text="update", command=self.update,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnupdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.Delete,   font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.Reset, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        #  Table Frame

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE,
                                 text="show Room Details", font=("arial", 12, "bold"))
        Table_Frame.place(x=550, y=55, width=500, height=350)

        #  scroll Bar

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        self.room_table = ttk.Treeview(Table_Frame, column=(
            "floor", "roomno", "roomType",), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomType", text="Room Type")

        self.room_table["show"] = "headings"
        self.room_table.column("floor", width=80)
        self.room_table.column("roomno", width=80)
        self.room_table.column("roomType", width=80)

        self.room_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        # Add button

    def add_data(self):
        if self.var_floor.get() == "" or self.var_RoomType.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="1234", database="World")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into world.details values(%s,%s,%s)", (

                    self.var_floor.get(),
                    self.var_roomno.get(),
                    self.var_RoomType.get(),


                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "success", "New Room Added Succesfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning(
                    "warning", f"something went wrong:{str(es)}", parent=self.root)

    #   fetch data

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="1234", database="world")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # get cursor

    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]
        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_RoomType.set(row[2])

        #  update button
# update quary kam ni kr rha h
    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error", "please enter roomno", parent=self.root)
        else:

            conn = mysql.connector.connect(
                host="localhost", username="root", password="1234", database="World")
            my_cursor = conn.cursor()
            my_cursor.execute("update world.details set Floor=%s,RoomType=%s where roomno=%s", (

                                                                                            self.var_floor.get(),
                                                                                            self.var_RoomType.get(),
                                                                                            self.var_roomno.get(),


                                                                                          ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","New Room details has been update succesfully", parent=self.root)

    #    delete button
    def Delete(self):
        Delete = messagebox.askyesno(
            "Hotel management system", "do u want to delete this details", parent=self.root)
        if Delete > 0:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="1234", database="World")
            my_cursor = conn.cursor()
            query = "delete from world.details where roomno=%s"
            value = (self.var_roomno.get(),)
            my_cursor.execute(query, value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    # reset button

    def Reset(self):
        self.var_floor.set("")
        self.var_RoomType.set("")
        self.var_roomno.set("")
        


if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()
