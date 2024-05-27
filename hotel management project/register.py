
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # variables

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security_question = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confirmpass = StringVar()


# background image
        self.bg = ImageTk.PhotoImage(
            file=r"C:\Users\91787\Desktop\hotel management project\wp6736569.jpg")

        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, height=690, width=1270)

        # Left image

        #  kam ni kr rha h

        # self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\91787\Desktop\project\655d8f8507ad847fde373d73c3fa987d.jpg")

        # left_lbl= Label(self.root, image=self.bg1)
        # left_lbl.place(x=50, y=100, width=470, relheight=100)

        #   main frame

        frame = Frame(self.root, bg="white")
        frame.place(x=400, y=100, width=620, height=490)

        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="green")
        register_lbl.place(x=20, y=20)


# Label and entry

        fname = Label(frame, text="First Name", font=(
            "times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=(
            "times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=230)
# last name
        lname = Label(frame, text="Last Name", font=(
            "times new roman", 15, "bold"), bg="white")
        lname.place(x=350, y=100)

        self.txt_lname = ttk.Entry(
            frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=350, y=130, width=230)


# row 2#####

        contact = Label(frame, text="Contact No", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(
            frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=230)

        # email

        email = Label(frame, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(
            frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=230)

        #  Row 3

        security_question = Label(frame, text="Select security_question", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        security_question.place(x=50, y=240)

        self.combo_security_question = ttk.Combobox(
            frame, textvariable=self.var_security_question, font=("times new roman", 15), state="readonly")
        self.combo_security_question["values"] = (
            "Select", "Your Birth Place", "Your Pet Name", "Your childhood Name", "Your Pornstar Name", "Your Sex Position")
        self.combo_security_question.place(x=50, y=270, width=250)
        self.combo_security_question.current(0)

        security_A = Label(frame, text=" Security_Answer", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(
            frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=230)

        #  Row 4

        pswrd = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        pswrd.place(x=50, y=310)

        self.txt_pass = ttk.Entry(
            frame, textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pass.place(x=50, y=340, width=230)

        confirm_pass = Label(frame, text="Confirm Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pass.place(x=370, y=310)

        self.txt_confirm_pass = ttk.Entry(
            frame, textvariable=self.var_confirmpass, font=("times new roman", 15))
        self.txt_confirm_pass.place(x=370, y=340, width=230)

        # check button

        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", font=(
            "times new roman", 13), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=370)

        # buttons

        img = Image.open(
            r"C:\Users\91787\Desktop\hotel management project\240_F_513878424_wraCWTLswiXk1szHCPGXmJhH2TMmq2fS - Copy - Copy.jpg")
        img = img.resize((200, 110), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        btn1 = Button(frame, image=self.photoimage, command=self.register_data,
                      borderwidth=0, cursor="hand2", font=("times new roman", 25))
        btn1.place(x=15, y=395, width=200)

        img1 = Image.open(
            r"C:\Users\91787\Desktop\hotel management project\depositphotos_40575109-stock-illustration-login-button - Copy.jpg")
        img1 = img1.resize((200, 110), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        btn2 = Button(frame, image=self.photoimage1, borderwidth=0,
                      cursor="hand2", font=("times new roman", 20))
        btn2.place(x=370, y=390, width=200)

        ###############  function declaration ######################

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_security_question.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confirmpass.get():
            messagebox.showerror(
                "Error", "password & confirm password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "please agree our terms and condition")
        else:
            # messagebox.showinfo("success","welcome freinds")
            conn = mysql.connector.connect(
                host="localhost", username="root", password="1234", database="World")
            my_cursor = conn.cursor()
            query = ("select * from world.register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error", "User all ready exist,please try another email")
            else:
                my_cursor.execute("insert into world.register values( %s, %s, %s, %s, %s, %s, %s)", (


                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_security_question.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()


                ))

            conn.commit()
            conn.close()
            messagebox.showinfo("success", "Register succesfully")


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
