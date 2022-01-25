import builtins
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps


root = Tk()
root.title("PhotoMall")

root.geometry("1280x720")

global counter
counter = 0

def nclick():
    global counter
    counter += 1
    mbutt.config(text=counter)
    if counter>4:
        counter = 0 
mbutt = Button(text = "add",command=nclick)



def open():
    global img_dir,img
    img_dir = filedialog.askopenfilename(initialdir=os.getcwd())
    img = Image.open(img_dir)
    img.thumbnail((350,650))
    img1 = ImageTk.PhotoImage(img)
    canvas2.create_image(300,210,image = img1)
    canvas2.image=img1



def rot_left():
    nclick()
    global img_dir,img_1 ,img_2
    img = Image.open(img_dir)
    img.thumbnail((350, 350))
    if counter>=1:
        img_1 = img.rotate(angle=90,expand=True)
        img_2 = ImageTk.PhotoImage(img_1)
        canvas2.create_image(300,210,image=img_2)
        canvas2.image=img_2
    if counter >= 2 :
        img_1 = img.rotate(angle=180,expand=True)
        img_2 = ImageTk.PhotoImage(img_1)
        canvas2.create_image(300,210,image=img_2)
        canvas2.image=img_2
    if counter >= 3 :
        img_1 = img.rotate(angle=270,expand=True)
        img_2 = ImageTk.PhotoImage(img_1)
        canvas2.create_image(300,210,image=img_2)
        canvas2.image=img_2
    if counter >= 4 :
        img_1 = img.rotate(angle=0,expand=True)
        img_2 = ImageTk.PhotoImage(img_1)
        canvas2.create_image(300,210,image=img_2)
        canvas2.image=img_2
        

def B_W():
    nclick()
    rot_left()
    global img_dir,img_1,img_2
    img = Image.open(img_dir)
    img.thumbnail((350, 350))
    img_1 = img.convert("L")
    img_2 = ImageTk.PhotoImage(img_1)
    canvas2.create_image(300,210,image=img_2)
    canvas2.image=img_2
    
def save():
    global img_dir,img_1,img_2
    ext = img_dir.split(".")[-1]
    file=asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
    canvas2.image=img_1
    img_1.save(file)

canvas2 = Canvas(root, width="800", height="620", relief=RIDGE, bd=2)
canvas2.place(x=10, y=50)

imp_button = Button(root,text="Import",command=open)
imp_button.place(x=15,y=15)

rot_btt = Button(root,text="Rotate",command=rot_left)
rot_btt.place(x=960,y=100)

rot_btt = Button(root,text="Rotate",command=rot_left)
rot_btt.place(x=960,y=100)

bw_btt = Button(root,text="black and white",command=B_W)
bw_btt.place(x=935,y=50)

btn2 = Button(root, text="Save",command=save)
btn2.place(x=90,y=15)
root.mainloop()