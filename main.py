from tkinter.filedialog import askopenfilenames
from tkinter import *
from tkinter import messagebox as mb

from java_format import Java
from cpp_format import Cpp
from cs_format import Cs


flag = 0
# if flag is 1 a message box gets printed showing the extraction was succesful

# delete file contents for new insertion
def close():
    f = open("extractor.txt", "w")
    f.write("")
    f.close()

def select():
    close()
    filenames = askopenfilenames(title='Select files',
                                 filetypes=(('java', '.java'),
                                            ('C++', '.cpp'),
                                            ('C#', '.cs'),
                                            ('All files', '.*')))

    for filename in filenames:
        if '.java' in filename:
            flag = 1
            jav = Java() # java object
            jav.tjava(filename)

        if '.cpp' in filename:
            flag = 1
            cp = Cpp() # C++ object
            cp.tcpp(filename)

        if '.cs' in filename:
            flag = 1
            cs = Cs() # C# object
            cs.tcs(filename)

    # prints a dialogue statement confirming file selection
    if flag == 1:
        mb.showinfo("Success", "File elements can be viewed in the console and in Extractor.txt file")
        op()


# ////////////////////////////////////


# main window
root = Tk()
root.title('File Element Collector')

# label on top
label1 = Label(root, text='       Press button to either select a java, C++ or a C# file      \n')
label1.pack()

# select file button
button1 = Button(root, text='Click to select files', command=select)
button1.pack()

# quit button
button2 = Button(root, text='Quit', command=sys.exit)
button2.pack()

# open text file
def opntxt():
    tx = open('Extractor.txt', 'r')
    l = tx.read()
    tx.close()
    return l


# open a new window to display said files
def op():
    top = Toplevel()
    top.title('Extractor')
    txt = Text(top, width=150, height=38)
    txt.insert(END, opntxt())

    txt.pack()
    btn3 = Button(top, text='Close Window', command=top.destroy, )
    btn3.pack(side=BOTTOM)
    top.geometry('1200x650')


# looping root main window
mainloop()