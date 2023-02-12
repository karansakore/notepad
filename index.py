from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfile
import os

def newFile():
    global file
    root.title("Untitled -Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension = ".txt", filetypes=[("All Files", "*.*",),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfile(initialfile ='Untitled.txt',defaultextension=".txt", filetypes=[("All Files", "*.*",),("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            # save as a new file
            f = open(file,"w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("file save")
    else:
        # save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Created by Karan")

if __name__ == '__main__':
    root = Tk()
    root.title("Untitled -Notepad")
    root.wm_iconbitmap("notepad_icon-icons.com_60631.ico")
    root.geometry("644x700")

    #Add textArea
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=TRUE, fill=BOTH)

    #Add Menu bar
    MenuBar = Menu(root)

    # ***** FILE MENU START *****#
    FileMenu = Menu(MenuBar, tearoff=0)
    # to open new file
    FileMenu.add_command(label="New",command=newFile)
    # To open alraedy existing file
    FileMenu.add_command(label="Open", command=openFile)
    # To save the current file
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    # ***** FILE MENU ENDS *****#


    #***** EDIT MENU STARTS *****#
    EditMenu = Menu(MenuBar, tearoff=0)
    # CUT, COPY, Paste
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu = EditMenu)
    #***** EDIT MENU ENDS *****#


    #***** HElP MENU STARTS *****#
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    #***** EDIT MENU ENDS *****#

    root.config(menu=MenuBar)

    # Adding Scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()