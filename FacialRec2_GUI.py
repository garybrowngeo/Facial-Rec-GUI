from email.policy import default
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
from tkinter.ttk import Treeview
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps
import tkinter.font
from FacialRec2_functions import *
from FacialRec2 import close_log


#Define GUI windows

#define GUI results window
def results_gui(results,window = ""):
    try:
        window.w1.destroy()
    except:
        window = ""
    class result_gui():
        def __init__(self, parent):
            self.gui(parent)

        def gui(self, parent):
            if parent == 0:
                self.w1 = Tk()
                self.w1.configure(bg = '#000000')
                self.w1.geometry('500x450')
                self.w1.title("Photos with Facial matchs")
            else:
                self.w1 = Frame(parent)
                self.w1.configure(bg = '#000000')
                self.w1.place(x = 0, y = 0, width = 500, height = 450)
            self.list1 = Listbox(self.w1, font = tkinter.font.Font(family = "Segoe UI", size = 9), selectmode = "SINGLE", cursor = "arrow", state = "normal")
            self.list1.place(x = 10, y = 50, width = 480, height = 300)
            list_no = 0
            for match in results:
                list_no +=1
                self.list1.insert(list_no, match)
            scrollbar_v = Scrollbar(self.list1, orient="vertical")
            scrollbar_v.config(command=self.list1.yview)
            scrollbar_v.pack(side="right", fill= "y")
            self.list1.config(yscrollcommand = scrollbar_v.set)
            scrollbar_h = Scrollbar(self.list1, orient="horizontal")
            scrollbar_h.config(command=self.list1.xview)
            scrollbar_h.pack(side="bottom", fill= "both")
            self.list1.config(xscrollcommand = scrollbar_h.set)
            self.label1 = Label(self.w1, text = "Matchs Found:", anchor='w', fg = "#ffffff", bg = "#000000", font = tkinter.font.Font(family = "Calibri", size = 10, weight = "bold"), cursor = "arrow", state = "normal")
            self.label1.place(x = 10, y = 20, width = 230, height = 22)
            self.label2 = Label(self.w1, text = "Full results can be found in Results.txt", anchor='w', fg = "#ffffff", bg = "#000000", font = tkinter.font.Font(family = "Calibri", size = 10, weight = "bold"), cursor = "arrow", state = "normal")
            self.label2.place(x = 10, y = 380, width = 430, height = 22)
            self.list1.bind("<<ListboxSelect>>", self.image_open)
            self.button1 = Button(self.w1, text = "View Pictures", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
            self.button1.place(x = 20, y = 420, width = 150, height = 22)
            self.button1['command'] = self.menu_results           

        def image_open(self,arg2):
            selection = self.list1.curselection()
            image = self.list1.get(selection)
            im = Image.open(image)
            im.show()

        def menu_results(self):
            view_results(results,self)
    

        
    b = result_gui(0)
    b.w1.mainloop()
    main_menu()

def view_results(results,window):
    window.w1.destroy()
    class PictureView():
        def __init__(self, parent):
            self.gui(parent)

        def gui(self, parent):
            if parent == 0:
                self.w1 = Tk()
                self.w1.geometry('800x600')
                self.w1.title("Facial Recognition - View Pictures")
            else:
                self.w1 = Frame(parent)
                self.w1.place(x = 0, y = 0, width = 800, height = 600)
            self.w1.resizable(True, True)
            self.frame1 = Frame(self.w1)
            self.frame1.pack(fill=X,side=BOTTOM)
            self.canvas1 = Canvas(self.w1)
            self.canvas1.pack(side=LEFT,fill=BOTH,expand=1)
            self.scrollbar_x = Scrollbar(self.frame1,orient=HORIZONTAL,command=self.canvas1.xview)
            self.scrollbar_x.pack(side=BOTTOM,fill=X)
            self.scrollbar_v = Scrollbar(self.w1, orient=VERTICAL, command=self.canvas1.yview)
            self.scrollbar_v.pack(side=RIGHT,fill=Y)
            self.canvas1.configure(xscrollcommand = self.scrollbar_x.set)
            self.canvas1.configure(yscrollcommand = self.scrollbar_v.set)
            self.canvas1.bind("<Configure>",lambda e: self.canvas1.config(scrollregion = self.canvas1.bbox(ALL)))
            self.frame2 = Frame(self.canvas1)
            self.canvas1.create_window((0,0), window = self.frame2, anchor = "nw")
# Removed as do not need to set grid pattern first
#            for b in range(1,5):
#                self.w1.columnconfigure(b, weight=1)
            i = 1
            y = 0
            for match in results:
                if i <= 6:
                    x = (i-1)
                if x == 6:
                    x = 0
                    y += 1
                x += 1
#Removed as labels seem to work better than creating images
#                globals()['self.image%s' % i] = Canvas(self.frame2, bg = 'white')
#                globals()['self.image%s' % i].grid(column = x, row = y, sticky = "nw")                
                globals()[('self.image%s' % i)+'im'] = Image.open(match)
                globals()[('self.image%s' % i)+'im1'] = ImageOps.fit(globals()[('self.image%s' % i)+'im'], (250, 300), method = 0,  bleed = 0.0, centering =(0.5, 0.5))                
                globals()[('self.image%s' % i)+'img'] = ImageTk.PhotoImage(globals()[('self.image%s' % i)+'im1'])              
#               globals()['self.image%s' % i].create_image(0, 0, image = globals()[('self.image%s' % i)+'img'], anchor=NW)
                globals()['self.label%s' % i] = Label(self.frame2, image = globals()[('self.image%s' % i)+'img'])
                globals()['self.label%s' % i].image = globals()[('self.image%s' % i)+'img']
                globals()['self.label%s' % i].grid(column = x, row = y, sticky = "nw")
                i += 1
   

    a = PictureView(0)
    a.w1.mainloop()
    results_gui(results)


#define GUI selection window
def selection_gui(window):        
    window.w1.destroy()
    class SelectionWindow():
        def __init__(self, parent):
            self.gui(parent)
        

        def gui(self, parent):
            if parent == 0:
                self.w1 = Tk()
                self.w1.configure(bg = '#000000')
                self.w1.geometry('500x220')
                self.w1.title("Facial Recognition - Select Person")
            else:
                self.w1 = Frame(parent)
                self.w1.configure(bg = '#000000')
                self.w1.place(x = 0, y = 0, width = 500, height = 220)
            self.person = Combobox(self.w1, font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
            self.person.place(x = 290, y = 75, width = 110, height = 22)
            self.person['values'] = facial_rec_query()
            self.person.current(0)
            self.label1 = Label(self.w1, text = "Select Person to Find:", anchor='w', fg = "#ffffff", bg = '#000000', font = tkinter.font.Font(family = "Calibri", size = 14), cursor = "arrow", state = "normal")
            self.label1.place(x = 90, y = 75, width = 190, height = 22)
            self.button1 = Button(self.w1, text = "Search", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
            self.button1.place(x = 380, y = 170, width = 90, height = 22)
            self.button1['command'] = self.submit
            self.hprogress1 = Progressbar(self.w1, maximum = 100, cursor = "arrow")
            self.hprogress1.place(x = 140, y = 170, width = 190, height = 22)
            self.hprogress1['value'] = 0
            self.label2 = Label(self.w1, text = "Progress:", anchor='w', fg = "#ffffff", bg = '#000000', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
            self.label2.place(x = 40, y = 170, width = 90, height = 22)

    #Define actions to perform when submit button pressed
        def submit(self):
            self.button1.destroy()
            # Create a list containing all .jpg files with path
            file_path = Path(filedialog.askdirectory())
            file_list = []
            file_list.extend(list(file_path.glob('**/*.jpg')))
            # Get selection and run facial rec
            self.person = self.person.get()
            matchs = []
            position = 0
            self.hprogress1.start()
            for file in file_list:
                facial_rec(file,self.person,matchs)
                position += 1
                progress = ((len(file_list) - (len(file_list) - position))/len(file_list)) * 100
                print("Progress {:2f}%".format(progress))
                self.hprogress1['value'] = progress
                a.w1.update_idletasks()
                a.w1.update()
                if position == len(file_list):
                    self.hprogress1.stop()
                    print()
                    print("Matching photos:")
                    for match in matchs:
                        print(match)
                    close_log()
                    results_gui(matchs,self)


    a = SelectionWindow(0)
    a.w1.mainloop()
    main_menu()

#define GUI add picture window
def add_picture_gui(window):
    window.w1.destroy()
    class AddWindow():
        def __init__(self, parent):
            self.gui(parent)
        

        def gui(self, parent):
            if parent == 0:
                self.w1 = Tk()
                self.w1.configure(bg = '#000000')
                self.w1.geometry('500x220')
                self.w1.title("Facial Recognition - Select Person")
            else:
                self.w1 = Frame(parent)
                self.w1.configure(bg = '#000000')
                self.w1.place(x = 0, y = 0, width = 500, height = 220)
            
            self.person = Combobox(self.w1, font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
            self.person.place(x = 290, y = 75, width = 110, height = 22)
            self.person['values'] = facial_rec_query()
            self.person.current(0)
            self.label1 = Label(self.w1, text = "Select Person to add picture:", anchor='w', fg = "#ffffff", bg = '#000000', font = tkinter.font.Font(family = "Calibri", size = 14), cursor = "arrow", state = "normal")
            self.label1.place(x = 20, y = 75, width = 250, height = 22)
            self.button1 = Button(self.w1, text = "Select & Add", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
            self.button1.place(x = 380, y = 170, width = 100, height = 22)
            self.button1['command'] = self.submit
            self.button2 = Button(self.w1, text = "Return to Menu", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
            self.button2.place(x = 20, y = 170, width = 150, height = 22)
            self.button2['command'] = self.menu_return


    #Define actions to perform when submit button pressed
        def submit(self):
            self.person = self.person.get()
            add_picture_result(self.person,self)
            
    #Define actions to perform when return button pressed
        def menu_return(self):
            main_menu(self)
    

    a = AddWindow(0)
    a.w1.mainloop()
    main_menu()

#define GUI results window
def list_subjects_gui(window):
    window.w1.destroy()
    class subjects_gui():
        def __init__(self, parent):
            self.gui(parent)

        def gui(self, parent):
            if parent == 0:
                self.w1 = Tk()
                self.w1.configure(bg = '#000000')
                self.w1.geometry('500x450')
                self.w1.title("Subjects")
            else:
                self.w1 = Frame(parent)
                self.w1.configure(bg = '#000000')
                self.w1.place(x = 0, y = 0, width = 500, height = 450)
            self.list1 = Listbox(self.w1, font = tkinter.font.Font(family = "Segoe UI", size = 9), cursor = "arrow", state = "normal")
            self.list1.place(x = 30, y = 50, width = 430, height = 200)
            list_no = 0
            for subject in facial_rec_query():
                list_no +=1
                self.list1.insert(list_no, subject)
            self.label1 = Label(self.w1, text = "Subjects:", anchor='w', fg = "#ffffff", bg = "#000000", font = tkinter.font.Font(family = "Calibri", size = 10, weight = "bold"), cursor = "arrow", state = "normal")
            self.label1.place(x = 30, y = 20, width = 230, height = 22)
            self.button1 = Button(self.w1, text = "Return to Menu", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
            self.button1.place(x = 20, y = 400, width = 150, height = 22)
            self.button1['command'] = self.menu_return

    #Define actions to perform when return button pressed
        def menu_return(self):
            main_menu(self)
        
    b = subjects_gui(0)
    b.w1.mainloop()
    main_menu()

#define Add subject window
def add_subjects_gui(window):
    window.w1.destroy()
    class AddSubject():
        def __init__(self, parent):
            self.gui(parent)

        def gui(self, parent):
            if parent == 0:
                self.w1 = Tk()
                self.w1.configure(bg = '#000000')
                self.w1.geometry('500x250')
                self.w1.title("Facial Recognition - Add Subject")
            else:
                self.w1 = Frame(parent)
                self.w1.configure(bg = '#000000')
                self.w1.place(x = 0, y = 0, width = 500, height = 250)
            self.label1 = Label(self.w1, text = "Subject Name:", anchor='w', fg = "#ffffff", bg = "#000000", font = tkinter.font.Font(family = "Calibri", size = 12, weight = "bold"), cursor = "arrow", state = "normal")
            self.label1.place(x = 30, y = 110, width = 150, height = 42)
            self.ltext1 = Entry(self.w1, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal")
            self.ltext1.place(x = 230, y = 120, width = 230, height = 22)
            self.label2 = Label(self.w1, text = "Type Subject Name and click add:", anchor='w', fg = "#ffffff", bg = "#000000", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
            self.label2.place(x = 30, y = 80, width = 300, height = 22)
            self.button1 = Button(self.w1, text = "Add", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
            self.button1.place(x = 380, y = 200, width = 90, height = 22)
            self.button1['command'] = self.add_subject

        def add_subject(self):
            response = subjects.add(self.ltext1.get())
            list_subjects_gui(self)

    a = AddSubject(0)
    a.w1.mainloop()    
    main_menu()

#define Add picture to subject results window
def add_picture_result(subject,window):
    window.w1.destroy()
    class PictureAdd():
        def __init__(self, parent):
            self.gui(parent)

        def gui(self, parent):
            if parent == 0:
                self.w1 = Tk()
                self.w1.configure(bg = '#000000')
                self.w1.geometry('500x200')
            else:
                self.w1 = Frame(parent)
                self.w1.configure(bg = '#000000')
                self.w1.place(x = 0, y = 0, width = 500, height = 200)
            self.label1 = Label(self.w1, text = "Result:", anchor='w', bg = "#000000", fg = "#ffffff", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
            self.label1.place(x = 20, y = 18, width = 90, height = 22)
            self.text1 = Text(self.w1, bg = "#000000", fg = "#ffffff", font = tkinter.font.Font(family = "Calibri", size = 14, weight = "bold"), cursor = "arrow", state  = "normal")
            self.text1.place(x = 50, y = 40, width = 390, height = 70)
            self.text1.insert(INSERT, facial_rec_add(subject))
            self.button1 = Button(self.w1, text = "Return to Main Menu", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
            self.button1.place(x = 130, y = 130, width = 230, height = 22)
            self.button1['command'] = self.menu_return
            
        
        #Define actions to perform when return button pressed
        def menu_return(self):
            main_menu(self)        

    a = PictureAdd(0)
    a.w1.mainloop()
    main_menu()

#define GUI main menu
def main_menu(window = ""):
    try:
        window.w1.destroy()
    except:
        window = ""
    class MainMenu():
        def __init__(self, parent):
            self.gui(parent)

        def gui(self, parent):
            if parent == 0:
                self.w1 = Tk()
                self.w1.configure(bg = '#000000')                
                self.w1.geometry('500x450')
                self.w1.title("Facial Recognition - Main Menu")
            else:
                self.w1 = Frame(parent)
                self.w1.place(x = 0, y = 0, width = 500, height = 450)
            self.label1 = Label(self.w1, text = "Main Menu", anchor='w', fg = "#ffffff", bg = "#000000", font = tkinter.font.Font(family = "Calibri", size = 20, weight = "bold"), cursor = "arrow", state = "normal")
            self.label1.place(x = 100, y = 40, width = 310, height = 52)
            self.button1 = Button(self.w1, text = "Add Picture to Subject", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
            self.button1.place(x = 100, y = 200, width = 300, height = 42)
            self.button1['command'] = self.add_picture
            self.button2 = Button(self.w1, text = "List Subjects", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
            self.button2.place(x = 100, y = 150, width = 300, height = 42)
            self.button2['command'] = self.list_subjects
            self.button3 = Button(self.w1, text = "Run Facial Recognition", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
            self.button3.place(x = 100, y = 250, width = 300, height = 42)
            self.button3['command'] = self.facial_recognition
            self.button4 = Button(self.w1, text = "Add Subject", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
            self.button4.place(x = 100, y = 100, width = 300, height = 42)
            self.button4['command'] = self.add_subject

        def add_picture(self):
            add_picture_gui(self)
            

        def list_subjects(self):
            list_subjects_gui(self)

        def facial_recognition(self):
            selection_gui(self)

        def add_subject(self):
            add_subjects_gui(self)    

    a = MainMenu(0)
    a.w1.mainloop()
    sys.exit()
