
import tkinter
from tkinter import *
from tkinter import filedialog




filepath = ''
root = Tk()
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(700,200) )
root.title(' Check files ')
root.config(bg='lightgray')
info_display = StringVar()

def main():
        fileselection = LabelFrame(root)
        fileselection.pack(padx=0, pady=60,)


        lbl_info = Label(fileselection, font=("arial", 8, "bold"), text="File Name:", fg="steel blue", bd=5)
        lbl_info.pack(side=LEFT, padx=5)

        txt_filepath = Entry(fileselection, font=("arial", 8, "bold"), textvariable=info_display,insertwidth=2,bg="white", justify=LEFT,state=DISABLED,width=50)
        txt_filepath.pack(side=LEFT, padx=12, pady=0)

        close_btn = Button(fileselection, text="Close", justify=LEFT,width=10, height=2, font=("arial", 8, "bold"))
        close_btn.pack(side=RIGHT, padx=5)

        close_btn.config(command=root.destroy)

        browse_btn = Button(fileselection, text="Browse file...", justify=CENTER, anchor=E,width=10, height=2, font=("arial", 8, "bold"))
        browse_btn.pack(side=RIGHT, padx=5)

        browse_btn.config(command=file_dialog)

        

        print(info_display.get())
        
        print(txt_filepath.get())

        root.mainloop()

def file_dialog():
        global filepath
        global info_display
        getfile = filedialog.askdirectory()

        filepath = '' + getfile
        info_display.set(filepath)
    
                
                
if __name__ == "__main__":
        main()
