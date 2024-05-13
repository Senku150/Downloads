import pyttsx3
import requests
import customtkinter
from customtkinter import CTk
from tkinter import filedialog, simpledialog
from tkinter import messagebox

path=""
string="l9"
def upload():
    global path,label
    path= filedialog.askopenfilename()
    label.configure(text="File PATH =\n"+path)

def commit():
    global path,label,string
    if path=="":
        messagebox.showerror("Error","Please upload a file first")
        return ""
    try:
        myFile = {"my_file": open(path, "rb")}
        s=requests.post("http://public-ip:5000/upload", files = myFile, timeout = 2.5)
        string=str(s.content)
        if string[2]=="1":
            messagebox.showinfo("INFO","The file has been send succsfuly")
            path=""
            label.configure(text="No File Has been Selected !!!")
            
        else:
            messagebox.showerror("ERROR","ERROR "+string[2])
    except:
        messagebox.showerror("ERROR","THE SERVER IS DOWN !!")

#GUI -------------------------------------------------------------------------------------------------
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

APP = customtkinter.CTk()

APP.title("LOC")
APP.geometry("800x750")

button1 = customtkinter.CTkButton(master=APP, text="Upload",
                                     width=100, height=100, font=("", 30),command=upload)
button1.place(relx=0.25, rely=0.8, anchor=customtkinter.CENTER)

button2 = customtkinter.CTkButton(master=APP, text="Commit",
                                    width=100, height=100, font=("", 30),command=commit)
button2.place(relx=0.75, rely=0.8, anchor=customtkinter.CENTER)
label=customtkinter.CTkLabel(APP,text="No File Has been Selected !!!",font=("",15),text_color="red")
label.place(relx=0.5,rely=0.5,anchor=customtkinter.CENTER)



APP.mainloop()






