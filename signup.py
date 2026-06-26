from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def register_details(username,password,mobile,email):
    if username!="" and password!="" and mobile!="" and email!="":
        file=open("user_details.txt",'w')
        file.write(str({'username':username,'password':password,'mobile':mobile,'email':email}))
        file.close()

        messagebox.showinfo("Registration Completed!!","All data Stored!!!")
        
    else:
        messagebox.showwarning("Blank detected!!!","All blamks should be filled")

def signup_pg():

    signup_window = Tk()
    signup_window.geometry("1920x1080")
    signup_window.title("Sign Up")
    signup_window.config(bg="#66C6EC")

    image = Image.open("./asset/signup.png")
    image=image.resize((300,200))
    photoImage = ImageTk.PhotoImage(image=image)

   
    label = Label(
    signup_window,
    image=photoImage,
    compound=TOP,
    text="Register Here ⬇️",
    bg="#66C6EC",
    fg="#0A2540",
    font=("Arial Black", 40, "bold")
    )
    label.pack(pady=30)

     
    username_frame = Frame(signup_window, bg="#66C6EC")
    username_frame.pack(pady=10)

    username_label = Label(
        username_frame,
        text="Username",
        bg="#2F4F4F",
        fg="white",
        font=("Arial Black", 16),
        width=10
    )
    username_label.pack(side=LEFT)

    username_entry = Entry(
        username_frame,
        bg="#8DD8F6",
        fg="black",
        font=("Arial", 16),
        width=20
    )
    username_entry.pack(side=LEFT, padx=10)

    
    password_frame = Frame(signup_window, bg="#66C6EC")
    password_frame.pack(pady=10)

    password_label = Label(
        password_frame,
        text="Password",
        bg="#2F4F4F",
        fg="white",
        font=("Arial Black", 16),
        width=10
    )
    password_label.pack(side=LEFT)

    password_entry = Entry(
        password_frame,
        show="*",
        bg="#8DD8F6",
        fg="black",
        font=("Arial", 16),
        width=20
    )
    password_entry.pack(side=LEFT, padx=10)

    
    mobile_frame = Frame(signup_window, bg="#66C6EC")
    mobile_frame.pack(pady=10)

    mobile_label = Label(
        mobile_frame,
        text="Mobile",
        bg="#2F4F4F",
        fg="white",
        font=("Arial Black", 16),
        width=10
    )
    mobile_label.pack(side=LEFT)

    mobile_entry = Entry(
        mobile_frame,
        bg="#8DD8F6",
        fg="black",
        font=("Arial", 16),
        width=20
    )
    mobile_entry.pack(side=LEFT, padx=10)

    
    email_frame = Frame(signup_window, bg="#66C6EC")
    email_frame.pack(pady=10)

    email_label = Label(
        email_frame,
        text="Email",
        bg="#2F4F4F",
        fg="white",
        font=("Arial Black", 16),
        width=10
    )
    email_label.pack(side=LEFT)

    email_entry = Entry(
        email_frame,
        bg="#8DD8F6",
        fg="black",
        font=("Arial", 16),
        width=20
    )
    email_entry.pack(side=LEFT, padx=10)

    
    btn_register = Button(
        signup_window,
        text="Register",
        bg="green",
        command=lambda: register_details(username_entry.get(),password_entry.get(),mobile_entry.get(),email_entry.get()),
        fg="white",
        font=("Arial Black", 20, "bold"),
        width=10,
        bd=5,
        relief="raised"
    )
    btn_register.pack(pady=40)

    signup_window.mainloop()