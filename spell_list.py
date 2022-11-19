#Import the required Libraries
from tkinter import *
from pythainlp.corpus import thai_words

def find_word(word):
  return [i for i in words if i.startswith(word)]

def get_txt():
    txt = input_txt.get()
    result = find_word(txt)
    res_txt.set(result)
    text.delete(1.0,END)
    text.insert(INSERT,result)
   
def centerwidow(win):
    window_height = 500
    window_width = 750

    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))



#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
#win.geometry("750x500")
centerwidow(win)

#Create a Text Box




input_txt = StringVar()
res_txt = StringVar()
res_txt.set("start")


label1 = Label(win,text="คำเริ่มต้น",font=30).grid(row=1,column=1,padx=5,pady=5)
btnStart = Button(win,text="ค้นหา",width=15,height=2,command=get_txt).grid(row=1,column=2,padx=10,pady=10 ,sticky= E)
label2 = Label(win,text="ผลลัพธ์",font=30).grid(row=3,column=1,padx=5,pady=5)
e = Entry(win,width=30 ,textvariable=input_txt, font= 25 ).grid(column=2,row=1,sticky=W)
#e1 = Text(app,width=50,height=5).grid(column=2,row=4)
#lbl_result = Label(win,textvariable= res_txt ,font=30,width= 50 ).grid(column=2,row=5)
btnClose = Button(win,text="Close",width=15,height=2,command=win.destroy).grid(column=2,row=10,pady=20) 

#txtbox.insert('1.0', 'here is my text to insert')
text= Text(win, width= 70, height= 10, background=
"gray71",foreground="black",font= ('Sans Serif', 13))

#Insert the text at the begining

text.grid(column=2,row=7)

words=list(thai_words())

win.mainloop()