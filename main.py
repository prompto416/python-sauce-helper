import webbrowser
from tkinter import *

class sourceHelper(Tk):
    def __init__(self):
        super(sourceHelper,self).__init__()
        self.title('Source Helper')
        self.minsize(300,100)

        self.default = 'http://www.twitter.com/'
        self.lab = Label(text=self.default)
        self.lab.pack()

        self.entry = Entry()
        self.entry.bind('<Return>', self.enter)
        self.entry.pack()

        self.go = Button(text= 'Go to website ',command=self.entryCommand)
        self.set = Button(text='Set as default website',command=self.setNew)



        self.go.pack()
        self.set.pack()
        self.instruct1 = Label(text='Paste the source into the entry.')
        self.instruct1.pack()

        self.instruct = Label(text='Press enter to go to the website.')
        self.instruct.pack()
        self.instruct2 = Label(text='Change the source format by setting new website as default.')


# webbrowser.open('youtube.com')

    def entryCommand(self):
        user = self.entry.get()

        webbrowser.open(self.default+user)

    def enter(self,event):
        user = self.entry.get()

        webbrowser.open(self.default + user)

    def setNew(self):
        user = self.entry.get()
        self.default = user

        self.lab.config(text=self.default)




root = sourceHelper()
root.mainloop()
