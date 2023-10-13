#Password generator
import random
from tkinter import *
from tkinter import messagebox as mb
import string

root = Tk()
root.geometry("1366x768")
root.maxsize(720, 480)
root.minsize(720, 480)
root.title("Password Generator")
root.configure(bg="#111111")


def generate_password():
    try:
        n = int(length.get())
        if n>50:
            mb.showerror("Error","Size of password is too large.")
            return
        elif n<1:
            mb.showerror("Error","Size of password should be greater than 0!")
            return
        lower_alpha = string.ascii_lowercase
        uper_alpha = string.ascii_uppercase
        digi = string.digits
        lis = []
        lis.extend(lower_alpha)
        lis.extend(uper_alpha)
        lis.extend(digi)
        lis.extend(["!","@","#","$","%","&","*","(",")",";",":",",",".","/", "?"])
        random.shuffle(lis)
        password = ''.join(lis[0:n])
        password_lable.configure(text=password)
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        l4.configure(text="**Copied to clipboard**")
    except Exception as e:
        mb.showerror("Error", "Input should be an integer!")
def reset_data():
    password_lable.configure(text="")
    user_entry.delete(0, END)
    l4.configure(text="")




l1_border = Label(root, text = "Password Gene", bg="#000000", fg="#000000", font=("Comic Sans Ms", 30, "bold"), pady=5).place(x = 218, y = 5)
l1 = Label(root, text = "Password Generator", bg="#111111", fg="#ffffff", font=("Comic Sans Ms", 20, "bold"), pady=5).pack(side = "top", pady = 12)

l2 = Label(root, text = "Enter the length of password you want: ", bg="#111111", fg="#ffffff", font=("Comic Sans Ms", 12, "bold"), pady=5).pack(side = "top", pady = 12)
length = StringVar()
user_entry = Entry(root, textvariable=length, width= 35, bg="#222222", fg="#ffffff", font=("Comic Sans Ms", 15, "bold"))
user_entry.pack(pady=15, padx=10)
btn = Button(root, text="Create", activeforeground="#0097ff", command = generate_password ,activebackground="#000000" , width=15, height=1 , bg="#222222", fg="#ffffff", borderwidth=5 , font=("Comic Sans Ms", 10, "bold")).place(x = 200, y = 200)
btn2 = Button(root, text="Reset", activeforeground="#0097ff", command = reset_data ,activebackground="#000000" , width=15, height=1 , bg="#222222", fg="#ffffff", borderwidth=5 , font=("Comic Sans Ms", 10, "bold")).place(x = 390, y = 200)
l3 = Label(root, text = "Your password is:", bg="#111111", fg="#ffffff", font=("Comic Sans Ms", 12, "bold"), pady=5).pack(pady = 50)
password_lable = Label(root, text = "", bg="#111111", fg="#ffffff", font=("Comic Sans Ms", 12, "bold"), pady=5)
password_lable.pack()
l4 = Label(root, text = "", bg="#111111", fg="#00b8e6", font=("Comic Sans Ms", 8, "bold"), pady=5)
l4.pack(pady = 40)



root.mainloop()