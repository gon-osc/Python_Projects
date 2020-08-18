import tkinter
from tkinter import *
from tkinter import filedialog
import time
import shutil
import os


filepath = ''
root = Tk()
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(900,300) )
root.title(' Check files ')
root.config(bg='lightgray')
info_display = StringVar()
info_display2 = StringVar()

SECONDS_IN_DAY = 24 * 60 * 60

now = time.time()
before = now - SECONDS_IN_DAY


def main():
        fileselection = LabelFrame(root)
        fileselection.pack(padx=0, pady=40,)

        fileselection2 = LabelFrame(root)
        fileselection2.pack(padx=0, pady=0,)


        lbl_info = Label(fileselection, font=("arial", 8, "bold"), text="Folder with files to be checked:", fg="steel blue", bd=5)
        lbl_info.pack(side=LEFT, padx=5)

        txt_filepath = Entry(fileselection, font=("arial", 8, "bold"), textvariable=info_display,insertwidth=2,bg="white", justify=LEFT,state=DISABLED,width=50)
        txt_filepath.pack(side=LEFT, padx=12, pady=0)

        lbl_info2 = Label(fileselection2, font=("arial", 8, "bold"), text="Folder that receives copied files:", fg="steel blue", bd=5)
        lbl_info2.pack(side=LEFT,padx=5)

        txt_filepath2 = Entry(fileselection2, font=("arial", 8, "bold"), textvariable=info_display2,insertwidth=2,bg="white", justify=LEFT,state=DISABLED,width=50)
        txt_filepath2.pack( side=LEFT,padx=12, pady=0)

        browse_btn = Button(fileselection, text="Browse file...", justify=CENTER, anchor=E,width=10, height=2, font=("arial", 8, "bold"))
        browse_btn.pack(side=RIGHT, padx=5)

        browse_btn.config(command=source)

        browse_btn2 = Button(fileselection2, text="Browse file...", justify=CENTER, anchor=E,width=10, height=2, font=("arial", 8, "bold"))
        browse_btn2.pack(side=RIGHT, padx=5)

        browse_btn2.config(command=destination)

        check_btn = Button(fileselection2, text="File Check", justify=LEFT,width=10, height=2, font=("arial", 8, "bold"))
        check_btn.pack(side=RIGHT, padx=5)

        check_btn.config(command=move_text_files)

        src = set('info_display')

        dst = set('info_display2')


        root.mainloop()


def source():
        global source_directory

        source_directory = filedialog.askdirectory()
        info_display.set(source_directory)
        

def destination():
        global destination_directory
        destination_directory = filedialog.askdirectory()
        info_display2.set(destination_directory)

def move_text_files():
        src_directory = source_directory
        dst_directory = destination_directory
        
        for file in os.listdir(src_directory):
                ab_path = os.path.join(source_directory, file)
                new_ab_path = os.path.join(destination_directory,file)
                if ab_path.endswith(".txt"):
                        if os.stat(ab_path).st_mtime > before:
                                shutil.move(ab_path, new_ab_path)

        


               
if __name__ == "__main__":
        main()
