# from dataclasses import dataclass
from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox 








class cust_Win:

 def __init__(self, root):

  self.root = root
  self.root.title("HOTEL Management System")
  self.root.geometry("1295x550+230+220")


  # variables

  self.var_ref = StringVar()
  x = random.randint(1000, 9999)
  self.var_ref.set(str(x))

  self.var_cust_name = StringVar()
  self.var_mother = StringVar()
  self.var_gender = StringVar()
  self.var_post = StringVar()
  self.var_mobile = StringVar()
  self.var_email= StringVar()
  self.var_nationality= StringVar()
  self.var_address = StringVar()
  self.var_id_proof= StringVar()
  self.var_id_number = StringVar()

  # Title>>>>>>>>

  lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=(
      "times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
  lbl_title.place(x=0, y=0, width=1295, height=50)

  #<<<< LOGO>>>>

  img2 = Image.open(
      r"C:\Users\91787\Desktop\hotel management project\1200px-Nyumbani_Hotel_Logo - Copy - Copy.png")
  img2 = img2.resize((100, 40), Image.ANTIALIAS)
  self.photoimg2 = ImageTk.PhotoImage(img2)

  lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
  lblimg.place(x=5, y=7, width=100, height=40)


  # label frame>>>>>>>

  labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="customer Details", font=("times new roman", 12, "bold"),padx=2)
  labelframeleft.place(x=5,y=-30,width=425,height=490)

  #<<<<<<<<< labels and entry>>>>>>>>>>
  # cust Ref
  lbl_cust_ref =Label (labelframeleft,text="customer Ref", font = ("arial", 13, "bold"),padx=2,pady=6)
  lbl_cust_ref.grid(row=0,column=0,sticky=W)

  enty_ref = ttk.Entry(labelframeleft,textvariable=self.var_ref, width=29,state="readonly", font=("times new roman", 13, "bold"))
  enty_ref.grid(row=0, column=1,)

  # cust name
  cname=Label(labelframeleft,font=("arial",12,"bold"),text="Customer Name:",padx=2,pady=6)
  cname.grid(row=1,column=0,sticky=W)
  txtcname = ttk.Entry(labelframeleft, textvariable=self.var_cust_name,font=("arial", 13, "bold"), width=29)
  txtcname.grid(row=1,column=1)

  # mother name
  lblmname = Label(labelframeleft, font=("arial", 12, "bold"), text="Mother Name:", padx=2, pady=6)
  lblmname.grid(row=2, column=0, sticky=W)
  txtmname = ttk.Entry(labelframeleft, textvariable=self.var_mother,font=("arial", 13, "bold"), width=29)
  txtmname.grid(row=2, column=1)

  # gender combobox
  label_gender = Label(labelframeleft, font=("arial", 12, "bold"), text="Gender:", padx=2, pady=6)
  label_gender.grid(row=3, column=0, sticky=W)
  combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender, font=("arial", 12, "bold"), width=27)
  combo_gender["value"]=("Male","Female","other")
  combo_gender.current(0)
  combo_gender.grid(row=3, column=1, sticky=W)

  # post code

  lblpostcode = Label(labelframeleft, font=("arial", 12, "bold"),
  text="postcode:", padx=2, pady=6)
  lblpostcode.grid(row=4, column=0, sticky=W)
  txtpostcode = ttk.Entry(labelframeleft, textvariable=self.var_post,  font=( "arial", 13, "bold"), width=29)
  txtpostcode.grid(row=4, column=1)
  # Mobile no
  lblmobile_no = Label(labelframeleft, font=("arial", 12, "bold"),text="mobile_no:", padx=2, pady=6)
  lblmobile_no.grid(row=5, column=0, sticky=W)
  txtmobile_no = ttk.Entry(labelframeleft, textvariable=self.var_mobile,  font=("arial", 13, "bold"), width=29)
  txtmobile_no.grid(row=5, column=1)

  # email

  lblEmail = Label(labelframeleft, font=("arial", 12, "bold"), text="Email:", padx=2, pady=6)
  lblEmail.grid(row=6, column=0, sticky=W)
  txtEmail = ttk.Entry(labelframeleft, textvariable=self.var_email,font=("arial", 13, "bold"), width=29)
  txtEmail.grid(row=6, column=1)


  # Nationality

  lblNationality = Label(labelframeleft, font=("arial",12,"bold"), text="Nationality:", padx=2, pady=6)
  lblNationality.grid(row=7, column=0, sticky=W)
  txtNationality = ttk.Entry(labelframeleft,  font=("arial", 13, "bold"), width=29)
  txtNationality.grid(row=7, column=1)

  combo_Nationality = ttk.Combobox(labelframeleft, textvariable=self.var_nationality,  font=("arial", 12, "bold"), width=27)
  combo_Nationality["value"] = ("Indian", "American", "Pakistan")
  combo_Nationality.current(0)
  combo_Nationality.grid(row=7, column=1, sticky=W)

# Idproof

  lblIdproof = Label(labelframeleft, font=("arial", 12, "bold"), text="Idproof:", padx=2, pady=6)
  lblIdproof.grid(row=8, column=0, sticky=W)

  combo_Idproof = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof,  font=("arial", 12, "bold"), width=27)
  combo_Idproof["value"] = ("Adharcard", "Pancard", "votercard","License")
  combo_Idproof.current(0)
  combo_Idproof.grid(row=8, column=1, sticky=W)


  # id number

  lblIdNumber = Label(labelframeleft, font=("arial", 12, "bold"), text="IdNumber:", padx=2, pady=6)
  lblIdNumber.grid(row=9, column=0, sticky=W)
  txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.var_id_number,  font=("arial", 13, "bold"), width=29)
  txtIdNumber.grid(row=9, column=1)


  # Address

  lblAddress = Label(labelframeleft, font=("arial", 12, "bold"), text="Address:", padx=2, pady=6)
  lblAddress.grid(row=10, column=0, sticky=W)
  txtAddress = ttk.Entry(labelframeleft, textvariable=self.var_address,  font=("arial", 13, "bold"), width=29)
  txtAddress.grid(row=10, column=1)




  # buttons

  btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
  btn_frame.place(x=0,y=400,width=412,height=39)

  btnAdd = Button(btn_frame, text="Add",command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
  btnAdd.grid(row=0,column=0,padx=1)

  btnupdate = Button(btn_frame, text="update",command=self.update,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
  btnupdate.grid(row=0, column=1, padx=1)


  btnDelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
  btnDelete.grid(row=0,column=2,padx=1)

  btnReset = Button(btn_frame, text="Reset",command=self.Reset,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
  btnReset.grid(row=0, column=3, padx=1)



  #  Table frame
  
  Table_Frame = LabelFrame(self.root,bd=2,relief=RIDGE,text="view Details and search system",font=("arial",12,"bold"))
  Table_Frame.place(x=420,y=50,width=800,height=490)


  #########   search system  ########### 

  # print("Hello")
  lblsearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="search By:",bg="red",fg="white")
  lblsearchBy.grid(row=0,column=0,sticky=W,padx=2)
  self.search_var=StringVar()

  combo_search = ttk.Combobox(Table_Frame,textvariable=self.search_var, font=("arial", 12, "bold"), width=16,state="readonly")
  # print(combo_search)
  combo_search["value"] = ("Mobile", "Ref")
  combo_search.current(0)
  combo_search.grid(row=0, column=1, sticky=W)
  self.txt_search=StringVar()
  txtsearch = ttk.Entry(Table_Frame,textvariable=self.txt_search, font=("arial", 13, "bold"), width=16)
  # print(txtsearch.get())
  txtsearch.grid(row=0, column=2)

  btnsearch = Button(Table_Frame, text="search",command=self.search, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
  btnsearch.grid(row=0, column=3, padx=1)

  btnshowAll = Button(Table_Frame, text="show All",command=self.fetch_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
  btnshowAll.grid(row=0, column=4, padx=1)

  # Show Data Table
  details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
  details_table.place(x=0,y=50,width=650,height=300)
  
 
  scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
  scroll_y = ttk.Scrollbar(details_table,orient=VERTICAL)

  self.cust_Details_Table = ttk.Treeview(details_table, column=("ref", "name", "mother", "gender", "post", "mobile", "email", "nationality", "idproof","idnumber", "address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
 
  scroll_x.pack(side=BOTTOM,fill=X)
  scroll_y.pack(side=RIGHT, fill=Y)

  scroll_x.config(command=self.cust_Details_Table.xview)
  scroll_y.config(command=self.cust_Details_Table.yview)

  self.cust_Details_Table.heading("ref",text="Refer No")
  self.cust_Details_Table.heading("name", text="Name")
  self.cust_Details_Table.heading("mother",text="Mother")
  self.cust_Details_Table.heading("gender", text="Gender")
  self.cust_Details_Table.heading("post", text="Postcode")
  self.cust_Details_Table.heading("mobile", text="Mobile")
  self.cust_Details_Table.heading("email", text="Email")
  self.cust_Details_Table.heading("nationality", text="Nationality")
  self.cust_Details_Table.heading("idproof", text="Id proof")
  self.cust_Details_Table.heading("idnumber",text="Id Number")
  self.cust_Details_Table.heading("address", text="Address")

  self.cust_Details_Table["show"]="headings"
  self.cust_Details_Table.column("ref",width=80)
  self.cust_Details_Table.column("name",width=80)
  self.cust_Details_Table.column("mother", width=80)
  self.cust_Details_Table.column("gender",width=80)
  self.cust_Details_Table.column("post", width=80)
  self.cust_Details_Table.column("mobile",width=80)
  self.cust_Details_Table.column("email",width=80)
  self.cust_Details_Table.column("nationality",width=80)
  self.cust_Details_Table.column("idproof", width=80)
  self.cust_Details_Table.column("idnumber", width=80)
  self.cust_Details_Table.column("address",width=80)

  self.cust_Details_Table.pack(fill=BOTH,expand=1)
  self.cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
  self.fetch_data()


  #data add

 def add_data(self):
      if self.var_mobile.get() == "" or self.var_mother.get() == "":
         messagebox.showerror("Error", "All fields are required", parent=self.root)
      else:
         try:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="World")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into world.customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_ref.get(),
                                                                            self.var_cust_name.get(),
                                                                            self.var_mother.get(),
                                                                            self.var_gender.get(),
                                                                            self.var_post.get(),
                                                                            self.var_mobile.get(),
                                                                            self.var_email.get(),
                                                                            self.var_nationality.get(),
                                                                            self.var_id_proof.get(),
                                                                            self.var_id_number.get(),
                                                                            self.var_address.get()
                                                                            
                                                                         ))
            conn.commit()
            self.fetch_data()
            conn.close()             
            messagebox.showinfo("success", "customer has been added", parent=self.root)
         except Exception as es:
            messagebox.showwarning("warning", f"something went wrong:{str(es)}", parent=self.root)

 def fetch_data(self):
  conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="world")
  my_cursor = conn.cursor()
  my_cursor.execute("select * from world.customer")
  rows=my_cursor.fetchall()
  if len(rows)!=0:
    self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
    for i in rows:
      self.cust_Details_Table.insert("",END,values=i)
    conn.commit()
  conn.close()

 def get_cursor(self,event=""):
   cursor_row=self.cust_Details_Table.focus()
   content= self.cust_Details_Table.item(cursor_row)
   row=content["values"]
   self.var_ref.set(row[0]),
   self.var_cust_name.set(row[1]),
   self.var_mother.set(row[2]),
   self.var_gender.set(row[3]),
   self.var_post.set(row[4]),
   self.var_mobile.set(row[5]),
   self.var_email.set(row[6]),
   self.var_nationality.set(row[7]),
   self.var_id_proof.set(row[8]),
   self.var_id_number.set(row[9]),
   self.var_address.set(row[10])


 def update(self):
     if self.var_mobile.get()=="":
         messagebox.showerror("success", "customer has been added", parent=self.root)
     else:
      
         conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="World")
         my_cursor = conn.cursor()
         my_cursor.execute("update world.customer set Name=%s,Mother=%s,Gender=%s,Postcode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                                
                                    self.var_cust_name.get(),
                                    self.var_mother.get(),
                                    self.var_gender.get(),
                                    self.var_post.get(),
                                    self.var_mobile.get(),
                                    self.var_email.get(),
                                    self.var_nationality.get(),
                                    self.var_id_proof.get(),
                                    self.var_id_number.get(),
                                    self.var_address.get(),
                                    self.var_ref.get() #update k liye ishko last me likhna h
                               ))

         conn.commit()
         conn.close()
         self.fetch_data()
         messagebox.showinfo("update","customer details has been update successfully",parent=self.root)


 def Delete(self):
   Delete=messagebox.askyesno("Hotel management system","do u want to delete this customer",parent=self.root)
   if Delete>0:
       conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="World")
       my_cursor = conn.cursor()
       query="delete from world.customer where Ref=%s"
       value=(self.var_ref.get(),)
       my_cursor.execute(query,value)
   else:
      if not Delete:
         return
   conn.commit()
   self.fetch_data()
   conn.close()

 def Reset(self):

   # self.var_ref.set(""),
   self.var_cust_name.set(""),
   self.var_mother.set(""),
   # self.var_gender.set(""),
   self.var_post.set(""),
   self.var_mobile.set(""),
   self.var_email.set(""),
   # self.var_nationality.set(""),
   # self.var_id_proof.set(""),
   self.var_id_number.set(""),
   self.var_address.set("")
   x = random.randint(1000, 9999)
   self.var_ref.set(str(x))

 def search(self):
    conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="World")
    my_cursor = conn.cursor()
    # print(self.search_var.get())
    # print())
    my_cursor.execute("select * from world.customer where "+str(self.search_var.get())+" Like '%"+str(self.txt_search.get())+"%'")
    # print()
    rows=my_cursor.fetchall()
    if len(rows)!=0:
      self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
      for i in rows:
         self.cust_Details_Table.insert("",END,values=i)
      conn.commit()
    conn.close()  


   




















if __name__ == "__main__":
  root = Tk()
  obj = cust_Win(root)
  root.mainloop()
