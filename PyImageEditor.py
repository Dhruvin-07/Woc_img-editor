from os import system,name
from tkinter import *
from tkinter.messagebox import askyesno
from PIL import Image,ImageTk,ImageEnhance
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile,asksaveasfilename



import ctypes
import colorsys
import cv2
import numpy as np

root = Tk()
root.title("PhotoMall")
root.geometry("1280x720")

canvas2 = Canvas(root, width="800", height="620", relief=RIDGE, bd=2)
canvas2.place(x=10, y=50)


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

    global img,label,im_resize,im,canvas2,counter
    counter = 0
    canvas2.img_name = filedialog.askopenfilename(title="Select Image",filetypes=(("png files","*.png"),("jpg files","*.jpg")))
    im = Image.open(canvas2.img_name)
    im_resize = im.resize((550,350))
    img = ImageTk.PhotoImage(im_resize) 
    label = Label(canvas2,image=img)
    label.place(x=120,y=120)


def rot_left():
    global im,Img,new,label
    nclick()
    if counter>=1:
        im = im.rotate(angle=90,expand=True)
        Img = im.resize((350,550))
        new = ImageTk.PhotoImage(Img)
        label.configure(image=new)
        label.place(x=200,y=50)
    if counter>=2:
        im = im.rotate(angle=0,expand=True)
        Img = im.resize((550,350))
        new = ImageTk.PhotoImage(Img)
        label.configure(image=new)
        label.place(x=120,y=120)
    if counter>=3:
        im = im.rotate(angle=360,expand=True)
        Img = im.resize((350,550))
        new = ImageTk.PhotoImage(Img)
        label.configure(image=new)
        label.place(x=200,y=50)
    if counter>=4:
        im = im.rotate(angle=0,expand=True)
        Img = im.resize((550,350))
        new = ImageTk.PhotoImage(Img)
        label.configure(image=new)
        label.place(x=120,y=120)


def BnW():
    global im,Img,new,label
    if counter == 1 or counter == 3: 
        im = im.convert("L")
        Img = im.resize((350,550))
        new = ImageTk.PhotoImage(Img)
        label.configure(image=new)
    else:
        im = im.convert("L")
        Img = im.resize((550,350))
        new = ImageTk.PhotoImage(Img)
        label.configure(image=new) 

def flip_vert():
    global new,im,Img,label
    if counter == 1 or counter == 3: 
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
        im_g= im.resize((350,550))
        new = ImageTk.PhotoImage(im_g)
        label.configure(image=new)
    else:
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
        Img= im.resize((550,350))
        new = ImageTk.PhotoImage(Img)
        label.configure(image=new)
        

def flip_hori():
    global new,im,Img,label
    if counter == 1 or counter == 3: 
        im = im.transpose(Image.FLIP_TOP_BOTTOM)
        Img= im.resize((350,550))
        new = ImageTk.PhotoImage(Img)
        label.configure(image=new)
    else:
        im = im.transpose(Image.FLIP_TOP_BOTTOM)
        im_g= im.resize((550,350))
        new = ImageTk.PhotoImage(im_g)
        label.configure(image=new)
    

def save():

    global Img,img_names,counter
    counter = 0
    ext = canvas2.img_name.split(".")[-1]
    file=asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
    new = ImageTk.PhotoImage(Img)
    label.configure(image=new)
    Img.save(file)

imp_button = Button(root,text="Import",command=open)
imp_button.place(x=15,y=15)

rot_btt = Button(root,text="Rotate",command=rot_left)
rot_btt.place(x=960,y=100)

rot_btt = Button(root,text="H.flip",command=flip_hori)
rot_btt.place(x=910,y=150)

rot_btt = Button(root,text="V.flip",command=flip_vert)
rot_btt.place(x=1000,y=150)

bw_btt = Button(root,text="black and white",command=BnW)
bw_btt.place(x=935,y=50)

btn2 = Button(root, text="Save",command=save)
btn2.place(x=90,y=15)

root.mainloop()
