from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Notebook
from PIL import Image as PilImage
from PIL import ImageTk
from tkinter import filedialog as fd
import psycopg2
import os

m = [[[['id', 'name', 'surname', 'patronymic', 'variant', 'graduate']], [['id_var', 'variant']]]]
count_1, count_2, base = [1], [1], 0
color = '#2f4a50'
'''
------------------------------Server------------------------------------------------------------------------------------------
'''
host = "localhost"
user = "postgres"
password = "050267Ai"
db_name = "students"
'''
------------------------------Start------------------------------------------------------------------------------------------
'''


class Window:
    def __init__(self, width, height, title='Menu', colour='#2f4a50', resizable=(True, True)):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+400+100")
        self.root.resizable(resizable[0], resizable[1])
        self.root['bg'] = color
        #  Image________________________________________________________________________________________________________________
        update = PilImage.open('update.webp')
        update = update.resize((50, 50), PilImage.ANTIALIAS)
        self.update = ImageTk.PhotoImage(update)
        exit_tab = PilImage.open('exit_2.png')
        exit_tab = exit_tab.resize((100, 50), PilImage.ANTIALIAS)
        self.exit_img = ImageTk.PhotoImage(exit_tab)
        # Vkladki______________________________________________________________________________________________________________________
        self.tabs_control = Notebook(self.root, height=700)
        # Start____________________________________________________________________________________________________________________
        self.Hello = Frame(self.tabs_control, bg=color)
        self.tabs_control.add(self.Hello, text='Start')
        # Tab_Level_2______________________________________
        self.lable_Hello = Label(self.Hello, width=60, height=10, font=("Courier", 16, "italic"),
                                 text='Hello,this program is about databases.\n Here you can:\n 1) view the lists\n 2) Delete/add a student or students\n 3) Find a student',
                                 fg='#df9a78', bg='#4A5A6C', relief=RAISED)
        # Vvod_____________________________________________________________________________________________________________________
        self.Vvod = Frame(self.tabs_control, bg=color)
        self.tabs_control.add(self.Vvod, text='Vvod')
        # Tab_Level_2______________________________________
        self.tabs_vvod = Notebook(self.Vvod)
        # Database_________________________________________
        self.Database = Frame(self.tabs_vvod, bg=color)
        self.tabs_vvod.add(self.Database, text='Database')
        # Tab_Level_2______________________________________
        self.lable_Database = Label(self.Database, width=40, height=5, font=("Courier", 16, "italic"),
                                    text="Enter: data-bases's number  ", fg='#df9a78', bg='#4A5A6C',
                                    relief=RAISED)
        self.entry_Database = Entry(self.Database)
        self.lable_Database_2 = Label(self.Database, width=40, height=5, font=("Courier", 16, "italic"),
                                      text="Enter: name for your new file ", fg='#df9a78', bg='#4A5A6C', relief=RAISED)
        self.entry_Database_2 = Entry(self.Database)
        # Separately______________________________________
        self.Separately = Frame(self.tabs_vvod, bg=color)
        self.tabs_vvod.add(self.Separately, text='Separately')
        # Tab_Level_2______________________________________
        self.lable_Separately = Label(self.Separately, width=40, height=5, font=("Courier", 16, "italic"),
                                      text='Enter: name , surname , patronymic', fg='#df9a78', bg='#4A5A6C',
                                      relief=RAISED)
        self.entry_Separately = Entry(self.Separately)
        # ------------------------------------------------
        self.lable_ticket = Label(self.Separately, width=40, height=5, font=("Courier", 16, "italic"),
                                  text='Enter: ticket', fg='#df9a78', bg='#4A5A6C', relief=RAISED)
        self.entry_ticket = Entry(self.Separately)
        # Files___________________________________________
        self.Files = Frame(self.tabs_vvod, bg=color)
        self.tabs_vvod.add(self.Files, text='Files')
        # Tab_Level_2______________________________________
        self.lable_Files_1 = Label(self.Files, width=40, height=5, font=("Courier", 16, "italic"),
                                   text='Choose a file with students', fg='#df9a78', bg='#4A5A6C', relief=RAISED)
        self.lable_Files_2 = Label(self.Files, width=40, height=5, font=("Courier", 16, "italic"),
                                   text='Choose a tickets', fg='#df9a78', bg='#4A5A6C', relief=RAISED)
        self.lable_Files_3 = Label(self.Files, width=40, height=5, font=("Courier", 16, "italic"), text='Choose a file',
                                   fg='#df9a78', bg='#4A5A6C', relief=RAISED)
        # Info____________________________________________________________________________________________________________________
        self.Info = Frame(self.tabs_control, bg=color)
        self.tabs_control.add(self.Info, text='Info')
        # Tab_Level_2______________________________________
        self.tabs_Info = Notebook(self.Info)
        # Students table_____________________________
        self.Students = Frame(self.tabs_Info, bg=color)
        self.tabs_Info.add(self.Students, text='Students')
        # Variants______________________________
        self.Course = Frame(self.tabs_Info, bg=color)
        self.tabs_Info.add(self.Course, text='Variants')
        # Testing table ________________________
        self.Testin = Frame(self.tabs_Info, bg=color)
        self.tabs_Info.add(self.Testin, text='Testing table')
        # student-variant_______________________
        self.student_variant = Frame(self.tabs_Info, bg=color)
        self.tabs_Info.add(self.student_variant, text='Student-variant')
        # Table____________________________________
        self.Table = Frame(self.tabs_Info, bg=color)
        self.tabs_Info.add(self.Table, text='Table')
        # Found______________________________________
        self.Found = Frame(self.tabs_Info, bg=color)
        self.tabs_Info.add(self.Found, text='Found')
        self.lable_Found = Label(self.Found, width=40, height=5, font=("Courier", 16, "italic"),
                                 text='Enter: id OR name surname patronymic', fg='#df9a78', bg='#4A5A6C', relief=RAISED)
        self.entry_Found = Entry(self.Found)
        # Changes___________________________________________________________________________________________________________________
        self.Changing = Frame(self.tabs_control, bg=color)
        self.tabs_control.add(self.Changing, text='Changing')
        # Tab_Level_2______________________________________
        self.tabs_changing = Notebook(self.Changing)
        # Changing information________________________
        self.Changes = Frame(self.tabs_changing, bg=color)
        self.tabs_changing.add(self.Changes, text='Changing information')
        # Tab_Level_2______________________________________
        self.lable_Changes = Label(self.Changes, width=40, height=5, font=("Courier", 16, "italic"),
                                   text='Enter: id , name , surname , patronymic', fg='#df9a78', bg='#4A5A6C',
                                   relief=RAISED)
        self.entry_Changes = Entry(self.Changes)
        # Delete______________________________________
        self.Delete = Frame(self.tabs_control, bg=color)
        self.tabs_changing.add(self.Delete, text='Delete')
        # Tab_Level_2______________________________________
        self.lable_Delete = Label(self.Delete, width=40, height=5, font=("Courier", 16, "italic"), text='Enter: id',
                                  fg='#df9a78', bg='#4A5A6C', relief=RAISED)
        self.entry_Delete = Entry(self.Delete)
        # Change graduate_____________________________
        self.graduate = Frame(self.tabs_control, bg=color)
        self.tabs_changing.add(self.graduate, text='Change graduate')
        # Tab_Level_2______________________________________
        self.lable_graduate = Label(self.graduate, width=40, height=5, font=("Courier", 16, "italic"),
                                    text='Enter: id, graduate', fg='#df9a78', bg='#4A5A6C', relief=RAISED)
        self.entry_graduate = Entry(self.graduate)
        # sefver __________________________________________
        self.server = Frame(self.tabs_control, bg=color)
        self.tabs_control.add(self.server, text='Server')
        # Tab_Level_2______________________________________
        self.lable_serf = Label(self.server, width=60, height=10, font=("Courier", 16, "italic"),
                                text="Chose table name", fg='#df9a78', bg='#4A5A6C', relief=RAISED)

    # -------------------Function---------------------------------------------------------------------------------------------------
    def run(self):
        self.drow_widget()
        self.root.mainloop()

    def drow_widget(self):
        # Vkladki______________________________________________________________________________________________________________________
        self.tabs_control.pack(fill=BOTH)
        # Start____________________________________________________________________________________________________________________
        self.lable_Hello.pack(pady=30)
        Button(self.Hello, fg='#7c0b2f', width=90, height=4, text='Recent saves', compound=TOP, bd=8,
               command=self.recent_saves).pack()
        Button(self.Hello, fg='#7c0b2f', width=1100, image=self.exit_img, compound=TOP, bd=8, command=self.exit).pack()
        # Vvod_____________________________________________________________________________________________________________________
        self.tabs_vvod.pack(fill=BOTH)
        # Database_________________________________________
        Button(self.Database, fg='#7c0b2f', width=10, height=2, text='Create new base', compound=TOP, bd=8,
               command=self.createbase).pack()
        self.lable_Database.pack(pady=30)
        self.entry_Database.pack()
        Button(self.Database, fg='#7c0b2f', width=10, height=2, text='continue', compound=TOP, bd=8,
               command=self.chousebase).pack()
        self.lable_Database_2.pack(pady=30)
        self.entry_Database_2.pack()
        Button(self.Database, text='Save to file', width=10, height=2, fg='#7c0b2f', compound=LEFT, bd=8,
               command=self.craete).pack()
        # Separately______________________________________
        self.lable_Separately.pack(pady=30)
        self.entry_Separately.pack()
        Button(self.Separately, width=10, height=2, text='continue', command=self.get_text).pack()
        # ticket-------------------------------------
        self.lable_ticket.pack()
        self.entry_ticket.pack()
        Button(self.Separately, width=10, height=2, text='continue', command=self.ticket).pack()
        # Files_____________________________________
        self.lable_Files_1.pack(pady=30)
        Button(self.Files, width=10, height=2, text='chose list', command=self.open_file_1).pack()
        self.lable_Files_2.pack(pady=30)
        Button(self.Files, width=10, height=2, text='chose list', command=self.open_file_2).pack()
        self.lable_Files_3.pack(pady=30)
        Button(self.Files, width=10, height=2, text='chose file', command=self.open_file_3).pack()
        # Info_____________________________________________________________________________________________________________________
        self.tabs_Info.pack(fill=BOTH)
        # Students table_____________________________
        Button(self.Students, text='Update', width=300, fg='#7c0b2f', image=self.update, compound=LEFT, bd=8,
               command=self.Student).pack()
        self.stu = ScrolledText(self.Students, height=100, width=52, selectbackground='#6fdbf5')
        self.stu.pack()
        # Variants________________________
        Button(self.Course, text='Update', width=500, fg='#7c0b2f', image=self.update, compound=LEFT, bd=8,
               command=self.Cours).pack()
        self.cou = ScrolledText(self.Course, width=20, height=100, selectbackground='#6fdbf5')
        self.cou.pack()
        # Testing table ________________________
        Button(self.Testin, text='Update', width=500, fg='#7c0b2f', image=self.update, compound=LEFT, bd=8,
               command=self.test_tab).pack()
        self.test_table = ScrolledText(self.Testin, width=13, height=100, selectbackground='#6fdbf5')
        self.test_table.pack()
        # student-variant_______________________
        Button(self.student_variant, text='Update', width=500, fg='#7c0b2f', image=self.update, compound=LEFT, bd=8,
               command=self.stud_var).pack()
        self.stvar = ScrolledText(self.student_variant, width=67, height=100, selectbackground='#6fdbf5')
        self.stvar.pack()
        # Table______________________________________
        Button(self.Table, text='Update', width=500, fg='#7c0b2f', image=self.update, compound=LEFT, bd=8,
               command=self.Tab).pack()
        self.tab = ScrolledText(self.Table, width=84, height=100, selectbackground='#6fdbf5')
        self.tab.pack()
        # Found______________________________________
        self.lable_Found.pack(pady=30)
        self.entry_Found.pack()
        Button(self.Found, width=10, height=2, text='Found', command=self.found).pack()
        # Changes__________________________________________________________________________________________________________________
        self.tabs_changing.pack(fill=BOTH)
        # Changing information________________________
        self.lable_Changes.pack(pady=30)
        self.entry_Changes.pack()
        Button(self.Changes, width=10, height=2, text='Change', command=self.changes).pack()
        # Delete______________________________________
        self.lable_Delete.pack(pady=30)
        self.entry_Delete.pack()
        Button(self.Delete, width=10, height=2, text='Delete', command=self.delete).pack()
        # Change graduate_____________________________
        self.lable_graduate.pack(pady=30)
        self.entry_graduate.pack()
        Button(self.graduate, width=10, height=2, text='Change', command=self.grad).pack()
        # sefver __________________________________________
        self.lable_serf.pack(pady=30)
        Button(self.server, fg='#7c0b2f', width=90, height=4, text='Upload to the server', compound=TOP, bd=8,
               command=self.serv).pack()

    # -------------------------Add_function---------------------------------------------------------------------------------------------------------------
    def exit(self):
        self.backup()
        self.root.destroy()

    # Start ____________________________________________________________________________________________________________________
    def recent_saves(self):
        global base
        self.recent_read()
        messagebox.showinfo('Info', f'You have {base + 1} base')

    def recent_read(self):
        global count_1, count_2, base
        flag = False
        with open('Back-up') as f:
            while True:
                line = (f.readline()).split()
                if not line:
                    break
                else:
                    if flag == False:
                        flag = True
                    else:
                        if str(line[0]).isdigit():
                            m[base][0].append([line[0], line[1], line[2], line[3], '-', line[5]])
                            if line[4] != '-':
                                flag_2 = True
                                for i in m[base][1]:
                                    if line[4] == i[1]: flag_2 = False
                                if flag_2 == True:
                                    m[base][1].append([count_2[base], line[4]])
                                    count_2[base] = count_2[base] + 1
                            count_1[base] = count_1[base] + 1
                        else:
                            base += 1
                            count_1.append(1)
                            count_2.append(1)
                            m.append([[['id', 'name', 'surname', 'patronymic', 'variant', 'graduate']],
                                      [['id_var', 'variant']]])

    # Info_____________________________________________________________________________________________________________________
    # Students table_____________________________
    def Student(self):
        self.stu.delete('1.0', END)
        self.stu.insert(END, f"{'studens'.center(51)}|\n")
        self.stu.insert(END, f"{'-' * 51}|\n")
        for i in range(len(m[base][0])):
            self.stu.insert(END, f"{str(m[base][0][i][0]).ljust(3)}|")
            self.stu.insert(END, f"{str(m[base][0][i][1]).ljust(15)}|")
            self.stu.insert(END, f"{str(m[base][0][i][2]).ljust(15)}|")
            self.stu.insert(END, f"{str(m[base][0][i][3]).ljust(15)}|\n")
            self.stu.insert(END, f"{'-' * 51}|\n")

    # Variants________________________
    def Cours(self):
        self.tickets()
        self.cou.delete('1.0', END)
        self.cou.insert(END, f"{'variants'.center(19)}|\n")
        self.cou.insert(END, f"{'-' * 19}|\n")
        self.cou.insert(END, f"{str(m[base][0][0][0]).ljust(3)}|")
        self.cou.insert(END, f"{str(m[base][1][0][1]).ljust(15)}|\n")
        self.cou.insert(END, f"{'-' * 19}|\n")
        for i in range(1, len(m[base][1])):
            self.cou.insert(END, f"{str(m[base][1][i][0]).ljust(3)}|")
            self.cou.insert(END, f"{str(m[base][1][i][1]).ljust(15)}|")
            self.cou.insert(END, f"{'-' * 19}|\n")

    # Testing table ________________________
    def test_tab(self):
        self.tickets()
        self.test_table.delete('1.0', END)
        self.test_table.insert(END, f"{'Testing tabl'}|\n")
        self.test_table.insert(END, f"{'-' * 12}|\n")
        self.test_table.insert(END, f"{str(m[base][0][0][0]).ljust(4)}|")
        self.test_table.insert(END, f"{str(m[base][1][0][0]).ljust(7)}|\n")
        self.test_table.insert(END, f"{'-' * 12}|\n")
        f = 1
        for i in range(1, len(m[base][0])):
            self.test_table.insert(END, f"{str(m[base][0][i][0]).ljust(4)}|")
            if len(m[base][1]) > 1:
                self.test_table.insert(END, f"{str(m[base][1][f][0]).ljust(7)}|\n")
            else:
                self.test_table.insert(END, f"{'-'.ljust(7)}|\n")
            self.test_table.insert(END, f"{'-' * 12}|\n")
            if f != len(m[base][1]) - 1:
                f += 1
            else:
                f = 1

    # student-variant_______________________
    def stud_var(self):
        self.tickets()
        self.stvar.delete('1.0', END)
        self.stvar.insert(END, f"{'student-variant'.center(66)}|\n")
        self.stvar.insert(END, f"{'-' * 66}|\n")
        self.stvar.insert(END, f"{str(' '.join(map(str, m[base][0][0][1:4]))).ljust(50)}|")
        self.stvar.insert(END, f"{str(m[base][1][0][1]).ljust(15)}|\n")
        self.stvar.insert(END, f"{'-' * 66}|\n")
        f = 1
        for i in range(1, len(m[base][0])):
            self.stvar.insert(END, f"{str(' '.join(map(str, m[base][0][i][1:4]))).ljust(50)}|")
            if len(m[base][1]) > 1:
                self.stvar.insert(END, f"{str(m[base][1][f][1]).ljust(15)}|\n")
            else:
                self.stvar.insert(END, f"{'-'.ljust(15)}|\n")
            self.stvar.insert(END, f"{'-' * 66}|\n")
            if f != len(m[base][1]) - 1:
                f += 1
            else:
                f = 1

    # Table______________________________________
    def Tab(self):
        self.tickets()
        self.tab.delete('1.0', END)
        self.tab.insert(END, f"{'table'.center(83)}|\n")
        self.tab.insert(END, f"{'-' * 83}|\n")
        for i in range(len(m[base][0])):
            self.tab.insert(END, f"{str(m[base][0][i][0]).ljust(3)}|")
            self.tab.insert(END, f"{str(m[base][0][i][1]).ljust(15)}|")
            self.tab.insert(END, f"{str(m[base][0][i][2]).ljust(15)}|")
            self.tab.insert(END, f"{str(m[base][0][i][3]).ljust(15)}|")
            self.tab.insert(END, f"{str(m[base][0][i][4]).ljust(15)}|")
            self.tab.insert(END, f"{str(m[base][0][i][5]).ljust(15)}|\n")
            self.tab.insert(END, f"{'-' * 83}|\n")

    def craete(self):
        text = str(self.entry_Database_2.get())
        new_file = open(f'{text}', 'w+')
        self.saves(new_file, base)
        os.replace(f'{text}', f'/Users/mihailcernysevskii/Downloads/{text}.txt')
        messagebox.showinfo('successfully', 'Check Download')

    # Found______________________________________
    def found(self):
        text = str(self.entry_Found.get())
        if text.isdigit():
            string_show = ' '.join(map(str, m[base][0][int(text)][1:]))
            messagebox.showinfo('Info', f'{string_show}')
        else:
            for el in m[base][0]:
                if text == ' '.join(map(str, el[1:4])):
                    string_show = ' '.join(map(str, el))
                    messagebox.showinfo('Info', f'{string_show}')
        self.entry_Found.delete(0, END)

    # Vvod_____________________________________________________________________________________________________________________
    def createbase(self):
        global base
        base += 1
        count_1.append(1)
        count_2.append(1)
        m.append([[['id', 'name', 'surname', 'patronymic', 'variant', 'graduate']], [['id_var', 'variant']]])

    def chousebase(self):
        global base
        base = int(self.entry_Database.get()) - 1
        messagebox.showinfo('Info', f'work on {base + 1}')
        self.entry_Database.delete(0, END)

    # Separately______________________________________
    def get_text(self):
        global count_1
        text = (str(self.entry_Separately.get())).split()
        flag = True
        if len(m[base][0]) > 1:
            for i in range(len(m[base][0])):
                if ''.join(text[0:3]) == ''.join(m[base][0][i][1:4]):
                    flag = False
            if flag == False:
                messagebox.showinfo('Info', 'Error')
            else:
                m[base][0].append([count_1[base], text[0], text[1], text[2], '-', '-'])
                count_1[base] = count_1[base] + 1

        else:
            m[base][0].append([count_1[base], text[0], text[1], text[2], '-', '-'])
            count_1[base] = count_1[base] + 1
        self.entry_Separately.delete(0, END)

    # ------------------------------------------------
    def ticket(self):
        global count_2
        text = str(self.entry_ticket.get())
        if text != ' ':
            m[base][1].append([count_2[base], text])
            count_2[base] = count_2[base] + 1
        self.entry_ticket.delete(0, END)

    # Files_____________________________________
    def open_file_1(self):
        global count_1
        file_name = fd.askopenfilename()
        with open(f'{file_name}') as f:
            while True:
                line = (f.readline()).split()
                if len(line) != 0:
                    m[base][0].append([count_1[base], line[0], line[1], line[2], '-', '-'])
                    count_1[base] = count_1[base] + 1
                else:
                    break

    def open_file_2(self):
        global count_2
        file_name = fd.askopenfilename()
        with open(f'{file_name}') as f:
            while True:
                line = (f.readline()).rstrip()
                if not line:
                    break
                else:
                    m[base][1].append([count_2[base], line])
                    count_2[base] = count_2[base] + 1

    def open_file_3(self):
        global base
        file_name = fd.askopenfilename()
        for index in range(base + 1):
            self.read(file_name, index)

    # Changes__________________________________________________________________________________________________________________
    # Changing information________________________
    def changes(self):
        text = (str(self.entry_Changes.get())).split()
        flag = True
        for i in range(len(m[base][0])):
            if ''.join(text[1:]) == ''.join(m[base][0][i][1:4]):
                flag = False
        if flag == False:
            messagebox.showinfo('Info', 'Error')
        else:
            for i in range(4): m[base][0][int(text[0])][i] = text[i]
            self.entry_Changes.delete(0, END)

    # Delete______________________________________
    def delete(self):
        global count_1
        count_1[base] = count_1[base] - 1
        text = int(self.entry_Delete.get())
        m[base][0].pop(text)
        while text != len(m[base][0]):
            m[base][0][text][0] = str(text)
            text += 1
        self.entry_Delete.delete(0, END)

    # Change graduate_____________________________
    def grad(self):
        text = (str(self.entry_graduate.get())).split()
        m[base][0][int(text[0])][5] = text[1]
        self.entry_graduate.delete(0, END)

    # _________________________________________________________________________________________________________________________________________________
    def tickets(self):
        if len(m[base][1]) > 1:
            f = 1
            for i in range(len(m[base][0]) - 1):
                m[base][0][i + 1][4] = m[base][1][f][1]
                if f != len(m[base][1]) - 1:
                    f += 1
                else:
                    f = 1

    def backup(self):
        new_file = open('Back-up', 'w+')
        for index in range(base + 1):
            self.saves(new_file, index)
        new_file.close()

    def saves(self, new_file, index):
        new_file.write(f"{str(m[index][0][0][0]).ljust(3)}")
        for i in range(1, len(m[index][0][0])):
            if i == len(m[index][0][0]) - 1:
                new_file.write(f"{str(m[index][0][0][i]).ljust(15)}\n")
            else:
                new_file.write(f"{str(m[index][0][0][i]).ljust(15)}")
        f = 1
        for i in range(1, len(m[index][0])):
            if str(m[index][0][i][0]).isdigit():
                new_file.write(f"{str(m[index][0][i][0]).ljust(3)}")
                for j in range(1, 4): new_file.write(f"{str(m[index][0][i][j]).ljust(15)}")
                if len(m[index][1]) > 1:
                    new_file.write(f"{str(m[index][1][f][1]).ljust(15)}")
                    if f != len(m[index][1]) - 1:
                        f += 1
                    else:
                        f = 1
                if len(m[index][1]) == 1: new_file.write(f"{'-'.ljust(17)}")
                if True:
                    if len(m[index][0][i][5]) > 0:
                        new_file.write(f"{str(m[index][0][i][5]).ljust(17)}\n")
                    else:
                        new_file.write(f"{'-'.ljust(17)}")
            else:
                break

    def serv(self):
        messagebox.showinfo('Info', 'Compleat')
        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    f"""CREATE TABLE students(
                        id serial PRIMARY KEY,
                        name varchar(50) NOT NULL,
                        surname varchar(50) NOT NULL,
                        patronymic varchar(50) NOT NULL,
                        variant VARCHAR(20) NOT NULL,
                        graduate VARCHAR(20) )
                    """
                )
            with connection.cursor() as cursor:
                print(m[base][0])
                print(m[base][0][1][2])
                for i in range(1, len(m[base][0])):
                    cursor.execute(
                        f"""INSERT INTO students (name,surname,patronymic,variant,graduate) VALUES
                        ('{m[base][0][i][1]}','{m[base][0][i][2]}','{m[base][0][i][3]}','{m[base][0][i][4]}','{m[base][0][i][5]}');
                        """
                    )
        except Exception as _ex:
            print('error')
        finally:
            if connection:
                connection.close()

    def read(self, name, index):
        global count_1, count_2
        flag = False
        with open(f'{name}') as f:
            while True:
                line = (f.readline()).split()
                if not line:
                    break
                else:
                    if flag == False:
                        flag = True
                    else:
                        if str(line[0]).isdigit():
                            m[index][0].append([line[0], line[1], line[2], line[3], '-', line[5]])
                            if line[4] != '-':
                                flag_2 = True
                                for i in m[index][1]:
                                    if line[4] == i[1]: flag_2 = False
                                if flag_2 == True:
                                    m[index][1].append([count_2[index], line[4]])
                                    count_2[index] = count_2[index] + 1
                            count_1[index] = count_2[index] + 1
                        else:
                            m[index][0].append('id', 'name', 'surname', 'patronymic', 'variant', 'graduate')


# Server----------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    window = Window(900, 700, 'Menu')
    window.run()
