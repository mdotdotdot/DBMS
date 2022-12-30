from tkinter import *
import mysql.connector
from tkinter import messagebox

def log_out(frame):
    frame.pack_forget()
    mainframe.pack()

def connect():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bazinga21!",
        database="trainingmanagementsys"
    )
    return db

def check_login(mainframe,username,password,acc_type):
    db = connect()
    cursor = db.cursor()
    query = "SELECT * FROM login WHERE username = %s AND password = %s AND account_type = %s"
    values = (username, password, acc_type)
    cursor.execute(query, values)
    user = cursor.fetchone()
    if user is not None:
        print("valid")
        logged_in(acc_type,mainframe,username)
    else:
        print("not valid")
    cursor.close()
    db.close()

my_window = Tk()  # Creating a window.

title_label = Label(
    text='Trainee-Course Management System',
    background='#a5e8f2',  # bg parameter can be used instead of background parameter as a short hand.
    foreground='white',  # fg parameter can be used instead of foreground parameter as a short hand.
    font=('Ariel', 25),
    )  # Creating a Label.

title_label.pack(padx=200,pady=80)

mainframe = Frame(my_window)
mainframe.pack()

def log_in_window():
    loginprompt = Label(
    mainframe,
    text='Log in',
    background='white',
    foreground='#071654',
    font=('Ariel', 15),
    )
    loginprompt.pack()
    prompt1 = Label(mainframe,text='Log-in as trainee, instructor or administrator:')
    prompt1.pack(padx=0,pady=10)
    options1 = ["instructor","trainee","administrator"]
    clicked1 = StringVar()
    clicked1.set( "trainee" )
    drop1 = OptionMenu(mainframe , clicked1 , *options1 )
    drop1.pack(padx=10,pady=10)
    username_label = Label(mainframe,text="Username:")
    username_entry = Entry(mainframe)
    password_label = Label(mainframe,text="Password:")
    password_entry = Entry(mainframe,show="*")
    login_button = Button(
        mainframe,
        text="Login",
        activebackground='#0f2da6',
        background='#c5e0ed',
        foreground='#5f466b',
        command=lambda:check_login(mainframe,username_entry.get(),password_entry.get(),clicked1.get())
        ) #add command
    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()
    login_button.pack(padx=10,pady=10)


log_in_window()


def course_details_view(frame):
    frame.pack_forget()
    coursesframe = Frame(my_window)
    coursesframe.pack()
    db = connect()
    cursor = db.cursor()
    query = "SELECT * FROM course"
    cursor.execute(query)
    result = cursor.fetchall()
    for i in range(0,len(result)):
        courseid1 = Label(coursesframe, text='Course Id:')
        courseid1.pack()
        courseid1 = Label(coursesframe, text=result[i][0])
        courseid1.pack()
        coursename1 = Label(coursesframe, text='Course Name:')
        coursename1.pack()
        coursename2 = Label(coursesframe, text=result[i][1])
        coursename2.pack()
        coursedesc1 = Label(coursesframe, text='Course Description:')
        coursedesc1.pack()
        coursedesc2 = Label(coursesframe, text=result[i][2])
        coursedesc2.pack()
        coursedur1 = Label(coursesframe, text='Course Duration:')
        coursedur1.pack()
        coursedur2 = Label(coursesframe, text=result[i][3])
        coursedur2.pack()

    cursor.close()
    db.close()

def logged_in(usertype,mainframe,username):
    mainframe.pack_forget()
    if usertype=='trainee':
        trainee_menu(username)

def backtomainscreen(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    mainframe.pack()

def trainee_menu(username):
    frametrainee=Frame(my_window)
    frametrainee.pack()
    prompt_1=Label(
        frametrainee,
        text='Welcome!',
        background='#a5e8f2',  # bg parameter can be used instead of background parameter as a short hand.
        foreground='white',  # fg parameter can be used instead of foreground parameter as a short hand.
        font=('Ariel', 14),
    )
    prompt_1.pack()
    db = connect()
    cursor = db.cursor()
    query = "SELECT t_id,first_name,last_name,contact_no,email,joining_date,address,time_slot,course_name FROM (((trainee JOIN login using (username)) JOIN session using(session_id)) JOIN course using(course_id)) WHERE username ='"+username+"'"
    # values = (username)
    cursor.execute(query)
    result = cursor.fetchall()
    tidlabel1 = Label(frametrainee,text='Trainee ID:')
    tidlabel1.pack()
    tidlabel2 = Label(frametrainee,text=result[0][0])
    tidlabel2.pack()
    fname1 = Label(frametrainee,text='Name: ')
    fname1.pack()
    fname2 = Label(frametrainee,text=result[0][1]+result[0][2])
    fname2.pack()
    contact1 = Label(frametrainee,text='Contact Number:')
    contact1.pack()
    contact2 = Label(frametrainee,text=result[0][3])
    contact2.pack()
    email1 = Label(frametrainee,text='Email:')
    email1.pack()
    email2 = Label(frametrainee,text=result[0][4])
    email2.pack()
    joiningdate1 = Label(frametrainee,text='Joining Date:')
    joiningdate1.pack()
    joiningdate2 = Label(frametrainee,text=result[0][5])
    joiningdate2.pack()
    address1 = Label(frametrainee,text='Address')
    address1.pack()
    address2 = Label(frametrainee,text=result[0][6])
    address2.pack()
    time_slot1 = Label(frametrainee,text='Time Slot:')
    time_slot1.pack()
    time_slot2 = Label(frametrainee,text=result[0][7])
    time_slot2.pack()
    coursename1 = Label(frametrainee,text='Course Name:')
    coursename1.pack()
    coursename2 = Label(frametrainee,text=result[0][8])
    coursename2.pack()
    cursor.close()
    db.close()

    coursedetailbutton = Button(
        frametrainee,
        text = 'Course Details',
        command= lambda: course_details_view(frametrainee)
    )
    coursedetailbutton.pack()
    logoutbutton = Button(
        frametrainee,
        text = 'Log out',
        command=lambda: log_out(frametrainee)
    )
    logoutbutton.pack()

my_window.mainloop()
