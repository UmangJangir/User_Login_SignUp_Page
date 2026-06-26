from tkinter import *
from PIL import Image, ImageTk
import signup
from tkinter import messagebox

def login_click():
    username=user_entry.get()
    password=password_entry.get()

    try:
        file=open('user_details.txt','r')
        data=eval(file.read())
        file.close()

        if username==data['username'] and password==data['password']:
            messagebox.showinfo("Success","Login Successful")
        else:
            messagebox.showerror("Error","Invaild Username or password")
    except FileNotFoundError:
        messagebox.showerror("Error","No user yet Registerd")

    

def signup_click():

    root.destroy()
    signup.signup_pg()

root = Tk()
root.geometry("1920x1080")
root.title("Login")
root.config(background="#66C6EC")

image = Image.open("./asset/login.png")
image=image.resize((300,200))
photoImage = ImageTk.PhotoImage(image=image)

image_label=Label(root,
                  image=photoImage,
                  bg="#66C6EC"
                  )
image_label.pack(pady=(5,0))


heading = Label(root,
              compound=TOP,
              text = "Login Here ⬇️",
              bg ="#66C6EC",
              font=("Arial Black", 40, "bold"),
              fg = "#0A2540")
heading.pack()

user_frame = Frame(root, bg ='#66C6EC')
user_frame.pack(pady=30)

user_label = Label(user_frame,
              text = "Username",
              bg ='#2F4F4F',
              font=("Arial Black", 16),
              fg = "White", 
              width=10)
user_label.pack(side=LEFT)

user_entry = Entry(user_frame, 
                   bg ="#8DD8F6",
              font=("Arial Black", 16),
              fg = "Black",
              width=20)
user_entry.pack()

password_frame = Frame(root, bg ='#66C6EC')
password_frame.pack()

password_label = Label(password_frame,
              text = "Password",
              bg ='#2F4F4F',
              font=("Arial Black", 16),
              fg = "White",
              width=10)
password_label.pack(side=LEFT)

password_entry = Entry(password_frame, 
                   bg ='#8DD8F6',
              font=("Arial Black", 16),
              fg = "Black",
              show='*',
              width=20)
password_entry.pack()


btn_frame = Frame(root, bg ='#66C6EC')
btn_frame.pack(pady=30)

btn_login = Button(btn_frame,
                   text='Login',
                   command=login_click,
                   bg ='green',
              font=("Arial Black", 20, "bold"),
              fg = "White",
              width=10,
              bd = 5,
              relief='raised')
btn_login.pack(side=LEFT, padx=30)

btn_signup = Button(btn_frame,
                   text='Sign Up',
                   command=signup_click,
                   bg ='red',
              font=("Arial Black", 20, "bold"),
              fg = "White",
              width=10,
              bd = 5,
              relief='raised')
btn_signup.pack(side=LEFT)
root.mainloop()