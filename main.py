from tkinter import *
import tkinter as tk
import os
from PIL import Image,ImageTk
from tkinter.filedialog import askdirectory 
root=Tk()
root.title("Photo Gallery")
root.geometry("890x470+300+200")
root.iconbitmap(R'D:\computer\Study\image_copy\image\icon_1.ico')
Universal_color="#555657"   
root.resizable(False,False)
def get_data():
    greet="Welcome "+user_name.get()
    label.config(text=greet, font= ('Helvetica 13'))

def image_(url,size):
    img=Image.open(url)
    resized_image= img.resize(size)
    img= ImageTk.PhotoImage(resized_image)
    return img
path_main=[]
def file_dilog():
    global path 
    path_=askdirectory()
    path=path_.replace('/', r'\\')
    path_name.config(text=path_,fg="Black")
def image_hold():
    load.config(text="Processing.......")
    try:
        if len(path)==0:
            load.config(text="File is not selected\nTo select\nClick on File Icon",fg="Red")
        else:
            import run
            user_name_=os.getlogin()
            run.copy_image(user_name_,path)
            
            name=run.convert(path)
            ex=f"Done......\nFile Name is :- \n{name}"
            load.config(text=ex)
    except:
        load.config(text="File is not selected\nTo select\nClick on File Icon")





username_space_image=image_(R"D:\computer\Study\image_copy\image\Group1.png",(900,500))
username_space=Label(image=username_space_image,bg=Universal_color)
username_space.place(x=-5,y=-5)
user_name_=os.getlogin()   

icon_image=image_(R"D:\computer\Study\image_copy\image\icon_1.png",(110,110))
icon_space=Label(image=icon_image,bg="#177F78")
icon_space.place(x=778,y=0)


greet="Welcome "+user_name_
label= Label(root, text=greet, font=('Helvetica', 20),bg="#177F78",fg="White")
label.place(x=345,y=30)

#select path were to copy


folder_image=image_(R"D:\computer\Study\image_copy\image\folder.png",(70,70))
button=tk.Button(root, text= "Select Folder", image=folder_image,command= file_dilog,bg="#D9D9D9",activebackground="#06234d",bd=0)
button.place(x=60,y=180)

path_name= Label(root, text="File Is not selected, Please Select the file ", font=('Helvetica', 15),bg="#D9D9D9",fg="Red")
path_name.place(x=170,y=200)



copy_image=image_(R"D:\computer\Study\image_copy\image\copy.png",(100,100))
button1=tk.Button(root, text= "Select Folder", image=copy_image,command= image_hold,bg="#00938A",activebackground="#06234d",bd=0)
button1.place(x=350,y=300)

load= Label(root, text="To copy \nclick on the copy ICON", font=('Helvetica', 13),bg="#138A79",fg="White")
load.place(x=660,y=310)
root.mainloop()



  

