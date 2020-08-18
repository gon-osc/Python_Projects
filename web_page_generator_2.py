
import tkinter
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True,height=True)
        self.master.geometry('{}x{}'.format(700,300))
        self.master.title('Webpage Generator')
        self.master.config(bg='lightgray')

        self.varBody = StringVar()

        self.lblBody = Label(self.master,text = 'Webpage Body : ', font=('Helvetica', 16), fg = 'black', bg='lightgray')
        self.lblBody.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.txtBody = Entry(self.master, text= self.varBody, width = 30, font=('Helvetica', 16), fg = 'black', bg='white')
        self.txtBody.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text = ' ', font=('Helvetica', 16), fg = 'black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text='Submit', width=10, height=2, command = self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text='Cancel', width=10, height=2, command = self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)



    def submit(self) :
        self.varBody.get()
        self.lblDisplay.config
        f = open('Custom_WebPage.html','x')

        message = """<html><body>"""+self.varBody.get()+"""</body></html>"""

        f.write(message)
        f.close()

        webbrowser.open_new_tab('Custom_WebPage.html')


    def cancel(self) :
        self.master.destroy()

        


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
