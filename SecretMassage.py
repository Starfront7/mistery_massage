from tkinter import *
from tkinter import messagebox
import base64
import os


def encrypt():
    password = code.get()
    if password == "":
        messagebox.showerror("Error", "Please enter a secret key")
    else:
        if password == "9999": 
            message = text1.get(1.0, END)
            encode_message = message.encode("utf-8")
            base64_bytes = base64.b64encode(encode_message)
            encrypted = base64_bytes.decode("utf-8")

            text2.delete(1.0, END)
            text2.insert(END, encrypted)
        else:
            messagebox.showerror("Error", "Invalid Password")


def decrypt():
    password = code.get()
    if password == "":
        messagebox.showerror("Error", "Please enter a secret key")
    else:
        if password == "4321":  # Password benar
            message = text1.get(1.0, END)
            try:
                decode_message = base64.b64decode(message)
                decrypted = decode_message.decode("utf-8")

                text2.delete(1.0, END)
                text2.insert(END, decrypted)
            except:
                messagebox.showerror("Error", "Invalid encryption or wrong data")
        else:
            messagebox.showerror("Error", "Invalid Password")


def clear():
    code.set("")
    text1.delete(1.0, END)
    text2.delete(1.0, END)


def main_screen():
    global screen, code, text1, text2
    screen = Tk()
    screen.geometry("400x450")
    screen.title("PctApp")


    image_icon = PhotoImage(file="keys.png")
    screen.iconphoto(False, image_icon)

    Label(screen, text="Enter text for encryption/decryption", fg="black", font=("calibri", 13)).pack(pady=10)

    text1 = Text(screen, font=("calibri", 12), wrap=WORD, width=40, height=5)
    text1.pack(pady=5)

    Label(screen, text="Enter secret key (password)", fg="black", font=("calibri", 13)).pack(pady=5)
    code = StringVar()
    Entry(screen, textvariable=code, width=20, bd=2, font=("calibri", 12), show="*").pack()

    Frame(screen, height=10).pack()

    Button(screen, text="ENCRYPT", bg="lightgreen", fg="black", width=10, command=encrypt).pack(pady=5)
    Button(screen, text="DECRYPT", bg="lightblue", fg="black", width=10, command=decrypt).pack(pady=5)
    Button(screen, text="CLEAR", bg="lightcoral", fg="black", width=10, command=clear).pack(pady=5)

    Label(screen, text="Result:", fg="black", font=("calibri", 13)).pack(pady=5)
    text2 = Text(screen, font=("calibri", 12), wrap=WORD, width=40, height=5)
    text2.pack(pady=5)

    screen.mainloop()

main_screen()
