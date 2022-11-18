import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Frame
import tkinter.filedialog
import os
from ThaiEz  import ThaiEz
from Remove_unused_Line import Remove_unused_Line
from spellcheck import spellcheck

class Frm(Frame):
    def __init__(self , parent):
        Frame.__init__(self , parent)
        self.parent = parent
        self.initUI()
        self.centerWindow()
    def initUI(self):
        self.parent.title("OCR")
        self.pack(fill=BOTH , expand=True)
    def centerWindow(self):
        w = 500
        h = 500
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


def CreateFolder():
    # Directory
    path_in = "D:/ocr/in"
    path_out = "D:/ocr/out"
  
    if not os.path.exists(path_in):
        os.makedirs(path_in)

    else:
        print("Directory in Exists")
    
    if not os.path.exists(path_out):
        os.makedirs(path_out)

    else:
        print("Directory out Exists")
        
    


def opendir():
    
    dir = tkinter.filedialog.askdirectory(initialdir="D:\ocr\in")
    pathin.set(dir)

def outputDir():
    dir = tkinter.filedialog.askdirectory()
    pathout.set(dir)
    return dir

def spellck():
    fileout = outputdir + "/" + "end.txt"
    filein = fileout
    fileout= outputdir + "/" + "spellcheck.txt"
    spell = spellcheck(filein,fileout)
    spell.checkspell()

def run():

    pathin = startdir
    pathout = outputdir
    #filein = "D:/ocr/out/argong_blank.txt"
    filein = outputdir+"/"+ "blank.txt"
    #fileout = "D:/ocr/out/argong_end.txt"
    fileout = outputdir + "/" + "end.txt"
    lang = "th"
    language = langvar.get()
    if language == 1:
        lang = "th"
    if language == 2:
        lang = "2"
    if language == 3:
        lang = "en"
    ts = ThaiEz(startdir,outputdir,lang)
    # Ocr_status = StringVar()
    status_Var.set(ts.get_status())
    #lblStatus.config(text = Ocr_status)
    ts.Run()
    

    rl = Remove_unused_Line(filein,fileout)
    rl.remove_line()
    filein = fileout
    fileout= outputdir + "/" + "spellcheck.txt"
    spell = spellcheck(filein,fileout)
    spell.checkspell()

def lang_select():
   selection = "You selected the option " + str(langvar.get())
   #label.config(text = selection)
   print(selection)

X = 30
root = Tk()
root.title("OCR To text")
root.geometry("500x500")
app = Frm(root)
CreateFolder()
startdir = "D:/ocr/in"
pathin = StringVar()
pathin.set(startdir)

outputdir = "D:/ocr/out"
pathout = StringVar()
pathout.set("D:/ocr/out")

status_Var = StringVar()
status_Var.set("Start")
langvar = IntVar()
langvar.set(1)

label1 = Label(app,text="Input Folder",font=30).grid(row=0,column=0,padx=5,pady=5)
label2 = Label(app,text="Output Folder",font=30).grid(row=2,column=0,padx=5,pady=5)
txtStartdir = Entry(app, width=30,textvariable=pathin).grid(row=0,column=1)
txtOutputdir = Entry(app, width=30,textvariable=pathout).grid(row=2,column=1)

btnStartFolder = Button(app,text="Select Folder",width=25,height=2,command=opendir ).grid(row =1,column=1)
btnOutputFolder = Button(app,text="Select Folder",width=25,height=2,command=outputDir).grid(row =3,column=1)
btnRun = Button(app,text="Run",width=15,height=2,command=run).grid(column=3,row=5) 
btnSpellCheck = Button(app,text="Spell Check",width=15,height=2,command=spellck).grid(column=3,row=6)
btnClose = Button(app,text="Close",width=15,height=2,command=root.destroy).grid(column=3,row=7) 

c1 = Checkbutton(app,text="Remove Blank Line",font=X).grid(row=0,column=3 ,padx=10,sticky=W)
c2 = Checkbutton(app,text="Remove unused Line",font= X).grid(row=1,column=3 ,padx=10,sticky=W)
lblStatus = Label(app,textvariable=status_Var,bg= 'yellow',font=30,width=15).grid(row=2,column=3)
lblPerform = Label(app,text="Perform",bg= 'orange',font=30,width=15).grid(row=3,column=3)
lblFinish = Label(app,text="Finished : No",bg= 'light green',font=30,width=15).grid(row=4,column=3,pady=5)

thailang = Radiobutton(app, text="Thai", variable=langvar, value=1,command=lang_select).grid(column=1,row=5,sticky=W ,pady=10 )
thaienglang = Radiobutton(app, text="Thai + English", variable=langvar, value=2,command=lang_select).grid(column=1,row=6,sticky=W)
englang = Radiobutton(app, text="English", variable=langvar, value=3,command=lang_select).grid(column=1,row=7,sticky=W)
label = Label(app).grid(column=0,row=7)

status_Var.set("Start")
mainloop()