
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from hotel import HotelManagementSystem
from customer import cust_Win
from room import Roombooking
from Details import DetailsRoom



def main():
  win=Tk()    #window 
  app=login_window(win)
  win.mainloop()







class login_window:
 def __init__(self,root):
  self.root=root
  self.root.title("Login")
  self.root.geometry("1550x1000+0+0")
   # background image
  self.bg = ImageTk.PhotoImage(
      file=r"C:\Users\91787\Desktop\hotel management project\wp1846069.jpg")

  lbl_bg=Label(self.root,image=self.bg)
  lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

  frame=Frame(self.root,bg="black")
  frame.place(x=510,y=140,width=340,height=410)

  img1 = Image.open(
      r"C:\Users\91787\Desktop\hotel management project\97923644-user-icon-avatar-login-sign-circle-button-with-soft-color-gradient-background-vector-.webp")
  img1=img1.resize((70,70),Image.ANTIALIAS)
  self.photoimage1 = ImageTk.PhotoImage(img1)
  lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
  lblimg1.place(x=630,y=142,width=100,height=100)
  
  get_str=Label(frame,text="Get started",font=("times new roman",20,"bold"),fg="white",bg="black")
  get_str.place(x=95,y=95)

  # Label username
  username = lbl = Label(frame, text="username", font=("times new roman", 15, "bold"), fg="white", bg="black")
  username.place(x=70,y=155)

  self.txtuser =ttk. Entry(frame, font=("times new roman", 15, "bold"))
  self.txtuser.place(x=40,y=180,width=270)


# Label password

  password = Label(frame, text="password", font=(
      "times new roman", 15, "bold"), fg="white", bg="black")
  password.place(x=70, y=210)

  self.txtpass = ttk.Entry(frame,show='*', font=("times new roman", 15, "bold"))
  self.txtpass.place(x=40, y=243, width=270)


#  username icon images
 
  img2 = Image.open(
      r"C:\Users\91787\Desktop\hotel management project\depositphotos_39580519-stock-illustration-user-man-icon-flat-design - Copy - Copy.jpg")
  img2 = img1.resize((20, 20), Image.ANTIALIAS)
  self.photoimage2 = ImageTk.PhotoImage(img2)
  lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
  lblimg2.place(x=552, y=299, width=18, height=18)


# password icon image

  img3 = Image.open(
      r"C:\Users\91787\Desktop\hotel management project\login-icon-button-vector-illustration-isolated-white-background-127000574.jpg")
  img3 = img1.resize((20, 20), Image.ANTIALIAS)
  self.photoimage3 = ImageTk.PhotoImage(img3)
  lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
  lblimg3.place(x=553, y=360, width=18, height=18)

# login Button

  loginbtn = Button(frame,command=self.login, text="Login", font=("times new roman", 15, "bold"), fg="white", bd=3,relief=RIDGE,bg="red",activeforeground="white",activebackground="red")
  loginbtn.place(x=100,y=285,width=90,height=30)

#  register button

  registerbtn = Button(frame, text="New User Register",command=self.register_window ,font=("times new roman", 10, "bold"), fg="white",borderwidth=0, bg="black", activeforeground="white", activebackground="black")
  registerbtn.place(x=15, y=325, width=165)

  # forget password

  forgetbtn = Button(frame, text="Forget Password", command=self.forgot_password_window,font=( "times new roman", 10, "bold"), fg="white", borderwidth=0, bg="black", activeforeground="white", activebackground="black")
  forgetbtn.place(x=10, y=350, width=160)

 def register_window(self):
    self.new_window=Toplevel(self.root)
    self.app = Register(self.new_window)

 def login(self):
  if self.txtuser.get()=="" or self.txtpass.get()=="":
    messagebox.showerror("Error","all field required")
  elif self.txtuser.get()=="satyam" and self.txtpass.get()=="wats":
    messagebox.showinfo("successfull")
  else:
    # print("row")
  

      conn = mysql.connector.connect(
          host="localhost", username="root", password="1234", database="World")
      my_cursor = conn.cursor()
      query = ("select * from world.register where email=%s and password=%s")
      Value=(self.txtuser.get(),self.txtpass.get())
      my_cursor.execute(query,Value)
      row=my_cursor.fetchone()
      # print(row)
      if row==None:
         messagebox.showerror("Error","Invalid Username & password")
      else:
        open_main=messagebox.askyesno("YesNo","Access only admin")
        if open_main>0:
            self.new_window = Toplevel(self.root)
            self.app = HotelManagementSystem(self.new_window)
        else:
          if not open_main:
            return 
      conn.commit()
      conn.close()

    # reset password


 def reset_pass(self):
  if self.combo_security_question.get()=="select":
    messagebox.showerror("Error","select the security question")
  elif self.txt_security.get()=="":
    messagebox.showerror("Error","please enter the answer")
  elif self.txt_newpass.get()=="":
    messagebox.showerror("Error","please enter the new password")
  else:
        conn = mysql.connector.connect(
            host="localhost", username="root", password="1234", database="World")
        my_cursor = conn.cursor()
        query=("select * from world.register where email=%s and security_question=%s and securityA=%s")
        value = (self.txtuser.get(), self.combo_security_question.get(),self.txt_security.get())
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()

        if row==None:
          messagebox.showerror("Error","please select the correct security Answer")
        else:
          query=("update register set password=%s where email=%s")
          value=(self.txt_newpass.get(),self.txtuser.get())
          my_cursor.execute(query, value)
          conn.commit()
          conn.close()
          messagebox.showinfo("success","your password has been reset,please login new password",parent=self.root2)
          self.root2.destroy()

       
#

#   forget password
 def forgot_password_window(self):
  if self.txtuser.get()=="":
    messagebox.showerror("Error","Please Enter the Email address to reset password")
  else:
     conn = mysql.connector.connect(
         host="localhost", username="root", password="1234", database="World")
     my_cursor = conn.cursor()
     query = ("select * from register where email=%s")
     value = (self.txtuser.get(),)
     my_cursor.execute(query, value)
     row = my_cursor.fetchone
     if row==None:
      messagebox.showerror("Error","Please enter the valid user name")
     else:
      conn.close()
      self.root2=Toplevel()
      self.root2.title("Forget password")
      self.root2.geometry("360x400+510+150")

      lbl = Label(self.root2,text="Forget password",font=("times new roman", 20, "bold"), fg="red", bg="white")
      lbl.place(x=0,y=10,relwidth=1)

      security_question = Label(self.root2, text="Select security_question", font=("times new roman", 15, "bold"), bg="white", fg="black")
      security_question.place(x=50, y=80)

      self.combo_security_question = ttk.Combobox(self.root2, font=("times new roman", 15), state="readonly")
      self.combo_security_question["values"] = ("Select", "Your Birth Place", "Your Pet Name", "Your childhood Name", "Your Pornstar Name", "Your Position")
      self.combo_security_question.place(x=50, y=110, width=250)
      self.combo_security_question.current(0)

      security_A = Label(self.root2, text=" Security_Answer", font=(
          "times new roman", 15, "bold"), bg="white", fg="black")
      security_A.place(x=50, y=140)

      self.txt_security = ttk.Entry(
          self.root2,  font=("times new roman", 15))
      self.txt_security.place(x=50, y=180, width=250)

      new_password = Label(self.root2, text=" New password", font=("times new roman", 15, "bold"), bg="white", fg="black")
      new_password.place(x=50, y=220)

      self.txt_newpass = ttk.Entry(
          self.root2,  font=("times new roman", 15))
      self.txt_newpass.place(x=50, y=250, width=250)

      btn = Button(self.root2, text="Reset", font=("times new roman", 15, "bold"), bg="green", fg="white")
      btn.place(x=100,y=290)







        


       
 

class Register:
 def __init__(self,root):
  self.root=root
  self.root.title("Register")
  self.root.geometry("1600x900+0+0")


  # variables

  self.var_fname=StringVar()
  self.var_lname = StringVar()
  self.var_contact = StringVar()
  self.var_email = StringVar()
  self.var_security_question = StringVar()
  self.var_securityA = StringVar()
  self.var_pswrd = StringVar()
  self.var_confirmpswrd = StringVar()


# background image
  self.bg = ImageTk.PhotoImage(
      file=r"C:\Users\91787\Desktop\hotel management project\wp6736569.jpg")
   
  bg_lbl = Label(self.root, image=self.bg)
  bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)


  

  #   main frame

  frame = Frame(self.root, bg="white")
  frame.place(x=400, y=100, width=640, height=490)

  register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="green")
  register_lbl.place(x=20,y=20)


# Label and entry
  
  fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"),bg="white")
  fname.place(x=50,y=100)

  fname_entry = ttk.Entry(frame,textvariable=self.var_fname, font=("times new roman", 15, "bold"))
  fname_entry.place(x=50,y=130,width=230)
# last name  
  lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
  lname.place(x=350, y=100)

  self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
  self.txt_lname.place(x=350, y=130, width=230)
  

# row 2#####

  contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white",fg="black")
  contact.place(x=50, y=170)

  self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
  self.txt_contact.place(x=50, y=200,width=230)

  # email

  email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
  email.place(x=370,y=170)

  self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
  self.txt_email.place(x=370, y=200, width=230)

  #  Row 3

  security_question=Label(frame, text="Select security_question", font=("times new roman", 15, "bold"), bg="white", fg="black")
  security_question.place(x=50, y=240)

  self.combo_security_question = ttk.Combobox(frame, textvariable=self.var_security_question, font=("times new roman", 15), state="readonly")
  self.combo_security_question["values"]=("Select","Your Birth Place","Your Pet Name","Your childhood Name","Your Pornstar Name","Your Position")
  self.combo_security_question.place(x=50,y=270,width=250)
  self.combo_security_question.current(0)

  security_A = Label(frame, text=" Security_Answer", font=(
      "times new roman", 15, "bold"), bg="white", fg="black")
  security_A.place(x=370, y=240)

  self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA ,font=("times new roman", 15))
  self.txt_security.place(x=370, y=270, width=230)


  #  Row 4

  pswrd = Label(frame, text="Password", font=(
      "times new roman", 15, "bold"), bg="white", fg="black")
  pswrd.place(x=50,y=310)

  self.txt_pswrd = ttk.Entry(frame, textvariable=self.var_pswrd, font=("times new roman", 15))
  self.txt_pswrd.place(x=50, y=340, width=230)

  confirm_pswrd = Label(frame, text="Confirm Password", font=(
      "times new roman", 15, "bold"), bg="white", fg="black")
  confirm_pswrd.place(x=370,y=310)

  self.txt_confirm_pswrd = ttk.Entry(frame, textvariable=self.var_confirmpswrd, font=("times new roman", 15))
  self.txt_confirm_pswrd.place(x=370, y=340, width=230)


  # check button

  self.var_check=IntVar()
  checkbtn = Checkbutton(frame,variable=self.var_check, text="I Agree The Terms & Conditions", font=("times new roman", 12),onvalue=1,offvalue=0)
  checkbtn.place(x=50,y=370)

  # buttons

  img = Image.open(
      r"C:\Users\91787\Desktop\hotel management project\240_F_513878424_wraCWTLswiXk1szHCPGXmJhH2TMmq2fS - Copy - Copy.jpg")
  img=img.resize((200,110),Image.ANTIALIAS)
  self.photoimage=ImageTk.PhotoImage(img)
  btn1 = Button(frame, image=self.photoimage,command=self.register_data, borderwidth=0, cursor="hand2", font=("times new roman", 25))
  btn1.place(x=10,y=390,width=200)

  img1 = Image.open(
      r"C:\Users\91787\Desktop\hotel management project\depositphotos_40575109-stock-illustration-login-button - Copy.jpg")
  img1 = img1.resize((200, 110), Image.ANTIALIAS)
  self.photoimage1 = ImageTk.PhotoImage(img1)
  btn2 = Button(frame, image=self.photoimage1,command=self.return_login, borderwidth=0, cursor="hand2" ,font=("times new roman", 25))
  btn2.place(x=330, y=390, width=200)



  #  function declaration

 def register_data(self):
  if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security_question.get()=="":
    messagebox.showerror("Error","All fields are required")
  elif self.var_pswrd.get()!=self.var_confirmpswrd.get():
    messagebox.showerror("Error","password & confirm password must be same")
  elif self.var_check.get()==0:
    messagebox.showerror("Error","please agree our terms and condition")
  else:
    # messagebox.showinfo("success","welcome freinds")
      conn = mysql.connector.connect(
          host="localhost", username="root", password="1234", database="World")
      my_cursor = conn.cursor()
      query=("select * from world.register1 where email=%s")
      value=(self.var_email.get(),)
      my_cursor.execute(query,value) 
      row=my_cursor.fetchone()
      if row!=None:
        messagebox.showerror("Error","User all ready exist,please try another email")
      else:
        my_cursor.execute("insert into world.register1 values( %s, %s, %s, %s, %s, %s, %s)",(


                                                                                self.var_fname.get(),
                                                                                self.var_lname.get(),
                                                                                self.var_contact.get(),
                                                                                self.var_email.get(),
                                                                                self.var_security_question.get(),
                                                                                self.var_securityA.get(),
                                                                                self.var_pswrd.get()


                                                                              ))

      conn.commit()
      conn.close()
      messagebox.showinfo( "success", "Register succesfully")     
#  login now

 def return_login(self):
  self.root.destroy()

class HotelManagementSystem:

 def __init__(self, root):

  self.root = root
  self.root.title("HOTEL Management System")
  self.root.geometry("1550x800+0+0")

  img1 = Image.open(
      r"C:\Users\91787\Desktop\hotel management project\Screenshot (15).png")
  img1 = img1.resize((1070, 140), Image.ANTIALIAS)
  self.photoimg1 = ImageTk.PhotoImage(img1)

  lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
  lblimg.place(x=0, y=0, width=1500, height=150)


#logo

  img2 = Image.open(
      r"C:\Users\91787\Desktop\hotel management project\images.png")
  img2 = img2.resize((230, 140), Image.ANTIALIAS)
  self.photoimg2 = ImageTk.PhotoImage(img2)

  lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
  lblimg.place(x=0, y=0, width=230, height=140)

  # Title
  lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=(
      "times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
  lbl_title.place(x=0, y=140, width=1550, height=50)

  # main frame
  main_frame = Frame(self.root, bd=4, relief=RIDGE)
  main_frame.place(x=0, y=190, width=1550, height=620)

  #menu

  lbl_menu = Label(main_frame, text="MENU", font=(
      "times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
  lbl_menu.place(x=0, y=0, width=230)

  #button frame

  btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
  btn_frame.place(x=0, y=35, width=228, height=190)

  cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=22, font=(
      "times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
  cust_btn.grid(row=0, column=0, pady=1)

  room_btn = Button(btn_frame, text="ROOM", command=self.roombooking, width=22, font=(
      "times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
  room_btn.grid(row=1, column=0, pady=1)

  details_btn = Button(btn_frame, text="DETAILS", command=self.details_room, width=22, font=(
      "times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
  details_btn.grid(row=2, column=0, pady=1)

  report_btn = Button(btn_frame, text="REPORT", width=22, font=(
      "times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
  report_btn.grid(row=3, column=0, pady=1)

  logout_btn = Button(btn_frame, text="LOGOUT",command=self.logout, width=22, font=(
      "times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
  logout_btn.grid(row=4, column=0, pady=1)

  # right side image

  img3 = Image.open(
      r"C:\Users\91787\Desktop\hotel management project\hotel-style-bedroom-ideas-warm-light-options.webp")
  img3 = img3.resize((1050, 440), Image.ANTIALIAS)
  self.photoimg3 = ImageTk.PhotoImage(img3)

  lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
  lblimg1.place(x=225, y=0, width=1050, height=440)

  # DOWN Images

  img4 = Image.open(
      r"C:\Users\91787\Desktop\hotel management project\pexels-chevanon-photography-312418 - Copy.jpg")
  img4 = img4.resize((275, 250), Image.ANTIALIAS)
  self.photoimg4 = ImageTk.PhotoImage(img4)

  lblimg2 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
  lblimg2.place(x=0, y=225, width=230, height=220)

 

 def cust_details(self):
  self.new_window = Toplevel(self.root)
  self.app = cust_Win(self.new_window)

 def roombooking(self):
  self.new_window = Toplevel(self.root)
  self.app = Roombooking(self.new_window)

 def details_room(self):
  self.new_window = Toplevel(self.root)
  self.app = DetailsRoom(self.new_window)

 def logout(self):
    self.root.destroy()



if __name__=="__main__":
  main()
