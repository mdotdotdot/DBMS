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
        logged_in(acc_type,mainframe,username)
    else:
        messagebox.showerror('Error', 'Invalid Login')
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

def close_courses_back(frame,username,acc_type):
    frame.pack_forget()
    if acc_type=='trainee':
        trainee_menu(username)
    elif acc_type=='instructor':
        instructor_menu(username)
    elif acc_type=='administrator':
        admin_menu()

def close_tt(frame,username,acc_type):
    frame.pack_forget()
    if acc_type=='instructor':
        instructor_menu(username)
    elif acc_type=='administrator':
        admin_menu()


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

def all_instructors_view(frame,username,acc_type):
    frame.pack_forget()
    sframe=Frame(my_window)
    sframe.pack()
    db = connect()
    cursor = db.cursor()
    query = "SELECT * FROM instructor"
    cursor.execute(query)
    result = cursor.fetchall()
    head1 = Label(sframe, text='Instructor ID: ')
    head1.grid(row=0, column=0)
    head2 = Label(sframe, text='Name: ')
    head2.grid(row=0, column=1)
    head3 = Label(sframe, text='Email: ')
    head3.grid(row=0, column=2)
    head4 = Label(sframe, text='Contact Number: ')
    head4.grid(row=0, column=3)
    head5 = Label(sframe, text='Address: ')
    head5.grid(row=0, column=4)
    head6 = Label(sframe, text='Joining Date: ')
    head6.grid(row=0, column=5)
    head7 = Label(sframe, text='Username: ')
    head7.grid(row=0, column=6)
    for i in range(0,len(result)):
        tail1 = Label(sframe, text=result[i][0])
        tail1.grid(row=i+1,column=0)
        tail2 = Label(sframe, text=result[i][1])
        tail2.grid(row=i+1,column=1)
        tail3 = Label(sframe, text=result[i][2])
        tail3.grid(row=i+1,column=2)
        tail4 = Label(sframe, text=result[i][3])
        tail4.grid(row=i+1,column=3)
        tail5 = Label(sframe, text=result[i][4])
        tail5.grid(row=i+1, column=4)
        tail6 = Label(sframe, text=result[i][5])
        tail6.grid(row=i+1, column=5)
        tail7 = Label(sframe, text=result[i][6])
        tail7.grid(row=i+1, column=6)
    cursor.close()
    db.close()
    backbuttonmalih = Button(
        sframe,
        text='Back',
        command=lambda: close_tt(sframe, 'admin', 'administrator')
    )
    backbuttonmalih.grid(row=30, column=4)
    logoutbuttonmalih = Button(
        sframe,
        text='Log out',
        command=lambda: log_out(sframe)
    )
    logoutbuttonmalih.grid(row=35, column=4)

def all_trainees_view(frame,username,acc_type):
    frame.pack_forget()
    alltrainframe=Frame(my_window)
    alltrainframe.pack()
    db=connect()
    cursor=db.cursor()
    query = "SELECT * FROM trainee"
    cursor.execute(query)
    result = cursor.fetchall()
    head1 = Label(alltrainframe, text='Trainee Id: ')
    head1.grid(row=0, column=0)
    head2 = Label(alltrainframe, text='First Name: ')
    head2.grid(row=0, column=1)
    head3 = Label(alltrainframe, text='Last Name: ')
    head3.grid(row=0, column=2)
    head4 = Label(alltrainframe, text='Contact Number: ')
    head4.grid(row=0, column=3)
    head5 = Label(alltrainframe, text='Email: ')
    head5.grid(row=0, column=4)
    head6 = Label(alltrainframe, text='Joining Date: ')
    head6.grid(row=0, column=5)
    head7 = Label(alltrainframe, text='Address: ')
    head7.grid(row=0, column=6)
    head8 = Label(alltrainframe, text='Username: ')
    head8.grid(row=0, column=7)
    head9 = Label(alltrainframe, text='Session ID: ')
    head9.grid(row=0, column=8)
    for i in range(0,len(result)):
        tail1 = Label(alltrainframe, text=result[i][0])
        tail1.grid(row=i+1,column=0)
        tail2 = Label(alltrainframe, text=result[i][1])
        tail2.grid(row=i+1,column=1)
        tail3 = Label(alltrainframe, text=result[i][2])
        tail3.grid(row=i+1,column=2)
        tail4 = Label(alltrainframe, text=result[i][3])
        tail4.grid(row=i+1,column=3)
        tail5 = Label(alltrainframe, text=result[i][4])
        tail5.grid(row=i+1, column=4)
        tail6 = Label(alltrainframe, text=result[i][5])
        tail6.grid(row=i+1, column=5)
        tail7 = Label(alltrainframe, text=result[i][6])
        tail7.grid(row=i+1, column=6)
        tail8 = Label(alltrainframe, text=result[i][7])
        tail8.grid(row=i+1, column=7)
        tail9 = Label(alltrainframe, text=result[i][8])
        tail9.grid(row=i+1, column=8)

    cursor.close()
    db.close()
    backbuttonslay = Button(
        alltrainframe,
        text='Back',
        command=lambda: close_tt(alltrainframe,username,acc_type)
    )
    backbuttonslay.grid(row=40, column=4)
    logoutbuttonslay = Button(
        alltrainframe,
        text='Log out',
        command=lambda: log_out(alltrainframe)
    )
    logoutbuttonslay.grid(row=45, column=4)


def teaching_teams_view(frame,username):
    frame.pack_forget()
    tt=Frame(my_window)
    tt.pack()
    db = connect()
    cursor = db.cursor()
    query = "SELECT team_id,course_id,course_name,description,duration_months from (instructor join teaching_team using(instructor_id)) join course using (team_id) where username='"+username+"'"
    cursor.execute(query)
    result = cursor.fetchall()
    head1=Label(tt, text='Team Id: ')
    head1.grid(row=0,column=0)
    head2=Label(tt,text='Course Id: ')
    head2.grid(row=0, column=1)
    head3 = Label(tt, text='Course Name: ')
    head3.grid(row=0, column=2)
    head4 = Label(tt, text='Description: ')
    head4.grid(row=0, column=3)
    head5 = Label(tt, text='Duration in Months: ')
    head5.grid(row=0, column=4)
    for i in range(0,len(result)):
        tail1 = Label(tt, text=result[i][0])
        tail1.grid(row=i+1,column=0)
        tail2 = Label(tt, text=result[i][1])
        tail2.grid(row=i+1,column=1)
        tail3 = Label(tt, text=result[i][2])
        tail3.grid(row=i+1,column=2)
        tail4 = Label(tt, text=result[i][3])
        tail4.grid(row=i+1,column=3)
        tail5 = Label(tt, text=result[i][4])
        tail5.grid(row=i + 1, column=4)

    cursor.close()
    db.close()

    backbuttonnew = Button(
        tt,
        text='Back',
        command=lambda: close_tt(tt, username,'instructor')
    )
    backbuttonnew.grid(row=7, column=8)
    logoutbuttonnew = Button(
        tt,
        text='Log out',
        command=lambda: log_out(tt)
    )
    logoutbuttonnew.grid(row=8, column=8)

def session_details_view(frame):
    frame.pack_forget()
    sessionsframe=Frame(my_window)
    sessionsframe.pack()
    db=connect()
    cursor=db.cursor()
    query="SELECT * FROM session"
    cursor.execute(query)
    result=cursor.fetchall()
    head1 = Label(sessionsframe, text='Session ID: ')
    head1.grid(row=0, column=0)
    head2 = Label(sessionsframe, text='Time Slot: ')
    head2.grid(row=0, column=1)
    head3 = Label(sessionsframe, text='Course ID: ')
    head3.grid(row=0, column=2)
    for i in range(0,len(result)):
        tail1 = Label(sessionsframe, text=result[i][0])
        tail1.grid(row=i+1,column=0)
        tail2 = Label(sessionsframe, text=result[i][1])
        tail2.grid(row=i+1,column=1)
        tail3 = Label(sessionsframe, text=result[i][2])
        tail3.grid(row=i+1,column=2)
    cursor.close()
    db.close()
    backbuttonqudsia = Button(
        sessionsframe,
        text='Back',
        command=lambda: close_tt(sessionsframe, 'admin', 'administrator')
    )
    backbuttonqudsia.grid(row=30, column=3)
    logoutbuttonqudsia = Button(
        sessionsframe,
        text='Log out',
        command=lambda: log_out(sessionsframe)
    )
    logoutbuttonqudsia.grid(row=40, column=3)

def course_details_view(frame,username,acc_type):
    frame.pack_forget()
    coursesframe = Frame(my_window)
    coursesframe.pack()
    db = connect()
    cursor = db.cursor()
    query = "SELECT * FROM course"
    cursor.execute(query)
    result = cursor.fetchall()
    courseid1 = Label(coursesframe, text='Course Id:')
    courseid1.grid(row=0, column=0)
    coursename1 = Label(coursesframe, text='Course Name:')
    coursename1.grid(row=0, column=1)
    coursedesc1 = Label(coursesframe, text='Course Description:')
    coursedesc1.grid(row=0, column=2)
    coursedur1 = Label(coursesframe, text='Course Duration:')
    coursedur1.grid(row=0, column=3)
    for i in range(0,len(result)):
        courseid1 = Label(coursesframe, text=result[i][0])
        courseid1.grid(row=i+1,column=0)
        coursename2 = Label(coursesframe, text=result[i][1])
        coursename2.grid(row=i+1,column=1)
        coursedesc2 = Label(coursesframe, text=result[i][2])
        coursedesc2.grid(row=i+1,column=2)
        coursedur2 = Label(coursesframe, text=result[i][3])
        coursedur2.grid(row=i+1,column=3)

    cursor.close()
    db.close()
    backbutton = Button(
        coursesframe,
        text='Back',
        command=lambda:close_courses_back(coursesframe,username,acc_type)
    )
    backbutton.grid(row=7,column=8)
    logoutbutton2 = Button(
        coursesframe,
        text='Log out',
        command=lambda: log_out(coursesframe)
    )
    logoutbutton2.grid(row=8,column=8)
# ///////////////////////////////////Maliha Addition/////////////////////////////////////////////////////
def add_instructor_view(frame):
    frame.pack_forget()
    addiframe = Frame(my_window)
    addiframe.pack()
    prompt1 = Label(addiframe,text='Fill the personal details:')
    prompt1.pack(padx=0,pady=10)
    username_label = Label(addiframe,text="Username:")
    username_entry = Entry(addiframe)
    password_label = Label(addiframe,text="Password:")
    password_entry = Entry(addiframe)
    name_label = Label(addiframe,text="Name:")
    name_entry = Entry(addiframe)
    id_label = Label(addiframe,text="ID:")
    id_entry = Entry(addiframe)
    email_label = Label(addiframe,text="Email:")
    email_entry = Entry(addiframe)
    address_label = Label(addiframe,text="Address:")
    address_entry = Entry(addiframe)
    phone_label = Label(addiframe,text="Contact Number:")
    phone_entry = Entry(addiframe)
    joining_label = Label(addiframe,text="Joining Date(YYYY/MM/DD):")
    joining_entry = Entry(addiframe)
    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()
    name_label.pack()
    name_entry.pack()
    id_label.pack()
    id_entry.pack()
    email_label.pack()
    email_entry.pack()
    address_label.pack()
    address_entry.pack()
    phone_label.pack()
    phone_entry.pack()
    joining_label.pack()
    joining_entry.pack()
    submit_info = Button(
        addiframe,
        text = "Submit",
        command=lambda :verify_add_instructors1(username_entry.get(),id_entry.get(),phone_entry.get(),addiframe)
    )
    submit_info.pack()
    backbutton = Button(
        addiframe,
        text='Back',
        command=lambda:close_courses_back(frame,"admin","adminstrator")
    )
    backbutton.pack()

def verify_add_instructors1(username,id,phone,frame):
    flag = 0
    if len(phone) != 11:
        messagebox.showerror('Error', 'Invalid contact number.')
        flag = 1
    db = connect()
    cursor = db.cursor()
    query = "SELECT username FROM login WHERE username = '"+username+"'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result is not None:
        messagebox.showerror('Error', 'Invalid username already assigned.')
        flag = 1
    cursor.close()
    db.close()
    db = connect()
    cursor = db.cursor()
    query = "SELECT Instructor_id FROM instructor where Instructor_id = '"+id+"'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result is not None:
        messagebox.showerror('Error', 'ID already assigned.')
        flag = 1
    cursor.close()
    db.close()
    if flag==0:
        add_more_info(frame)

def changeflagandproceed(frame,flag):
    frame.pack_forget()
    flag=0

def add_more_info(frame):
    # loop=1
    # while loop:
    frame.pack_forget()
    malihqudsiframe = Frame(my_window)
    malihqudsiframe.pack()
    prompt1 = Label(malihqudsiframe,text='Fill Instructor details')
    prompt1.pack(padx=0,pady=10)
    prompt2 = Label(malihqudsiframe,text='Job Description:')
    prompt2.pack(padx=0,pady=10)
    options = ["Course Instructor","Researcher","Both"]
    clicked = StringVar()
    clicked.set( "Course Instructor" )
    drop1 = OptionMenu(malihqudsiframe , clicked , *options)
    drop1.pack(padx=10,pady=10)
    extraf1 = Frame(malihqudsiframe)
    extraf2 = Frame(malihqudsiframe)
    prompt10= Label(extraf1,text="Years of Experience: ")
    prompt10.pack(padx=10,pady=10)
    prompt10entry = Entry(extraf1)
    prompt10entry.pack(padx=10,pady=10)
    prompt11= Label(extraf1,text="Course : ")
    prompt11.pack(padx=10,pady=10)
    courseoptions = ["Database Systems","Calculus","Linear Algebra", "Mechanics"]
    clickedcourse = StringVar()
    clickedcourse.set( "Database Systems" )
    drop2 = OptionMenu(extraf1 , clickedcourse , *courseoptions)
    drop2.pack(padx=10,pady=10)
    prompt20= Label(extraf2,text="Research Field:")
    prompt20.pack(padx=10,pady=10)
    prompt20entry = Entry(extraf2)
    prompt20entry.pack(padx=10,pady=10)
    prompt21= Label(extraf2,text="Field Description:")
    prompt21.pack(padx=10,pady=10)
    if clicked=="Course Instructor":
        extraf1.pack()
    elif clicked=="Researcher":
        extraf2.pack()
    else:
        extraf1.pack()
        extraf2.pack()
    submitbutton = Button(malihqudsiframe,text="Submit", command=lambda:changeflagandproceed(frame,flag))
    submitbutton.pack()





def logged_in(usertype,mainframe,username):
    mainframe.pack_forget()
    if usertype=='trainee':
        trainee_menu(username)
    elif usertype=='instructor':
        instructor_menu(username)
    elif usertype=='administrator':
        admin_menu()



def backtomainscreen(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    mainframe.pack()

def admin_menu():
    adminframe=Frame(my_window)
    adminframe.pack()
    prompt_a = Label(
        adminframe,
        text='Welcome!',
        background='#a5e8f2',  # bg parameter can be used instead of background parameter as a short hand.
        foreground='white',  # fg parameter can be used instead of foreground parameter as a short hand.
        font=('Ariel', 14),
    )
    prompt_a.grid(row=0, column=2)
    look_at_trainee=Button(
        adminframe,
        text='View Trainees',
        command=lambda:all_trainees_view(adminframe,'admin','administrator')
    )
    look_at_trainee.grid(row=10, column=2)
    look_at_instructors=Button(
        adminframe,
        text='View Instructors',
        command=lambda:all_instructors_view(adminframe,'admin','administrator')
    )
    look_at_instructors.grid(row=15,column=2)
    look_at_courses=Button(
        adminframe,
        text='View Courses',
        command=lambda: course_details_view(adminframe,'admin','administrator')
    )
    look_at_courses.grid(row=20,column=2)
    look_at_sessions=Button(
        adminframe,
        text='View Sessions',
        command=lambda: session_details_view(adminframe)
    )
    look_at_sessions.grid(row=25,column=2)
    add_instructor=Button(
        adminframe,
        text="Add Instructor",
        command= lambda: add_instructor_view(adminframe)
    )
    add_instructor.grid(row=30,column=2)

def instructor_menu(username):
    frameinstructor=Frame(my_window)
    frameinstructor.pack()
    prompt_1 = Label(
        frameinstructor,
        text='Welcome!',
        background='#a5e8f2',  # bg parameter can be used instead of background parameter as a short hand.
        foreground='white',  # fg parameter can be used instead of foreground parameter as a short hand.
        font=('Ariel', 14),
    )
    prompt_1.grid(row=0, column=2)
    db = connect()
    cursor = db.cursor()
    query = "SELECT distinct instructor_name,email,contact_no,address,joining_date,username FROM instructor join teaching_team using (instructor_id) WHERE username='"+username+"'"
    # values = (username)
    cursor.execute(query)
    result = cursor.fetchall()

    tidlabel1 = Label(frameinstructor, text='Instructor Name: ')
    tidlabel1.grid(row=1, column=0)
    fname1 = Label(frameinstructor, text='Email: ')
    fname1.grid(row=1, column=1)
    contact1 = Label(frameinstructor, text='Contact Number:')
    contact1.grid(row=1, column=2)
    email1 = Label(frameinstructor, text='Address:')
    email1.grid(row=1, column=3)
    joiningdate1 = Label(frameinstructor, text='Joining Date:')
    joiningdate1.grid(row=1, column=4)
    address1 = Label(frameinstructor, text='Username: ')
    address1.grid(row=1, column=5)
    tidlabel2 = Label(frameinstructor, text=result[0][0])
    tidlabel2.grid(row=2, column=0)
    fname2 = Label(frameinstructor, text=result[0][1])
    fname2.grid(row=2, column=1)
    contact2 = Label(frameinstructor, text=result[0][2])
    contact2.grid(row=2, column=2)
    email2 = Label(frameinstructor, text=result[0][3])
    email2.grid(row=2, column=3)
    joiningdate2 = Label(frameinstructor, text=result[0][4])
    joiningdate2.grid(row=2, column=4)
    address2 = Label(frameinstructor, text=result[0][5])
    address2.grid(row=2, column=5)
    cursor.close()
    db.close()

    all_trainees_info_button=Button(
        frameinstructor,
        text='All Trainees Info',
        command=lambda: all_trainees_view(frameinstructor,username,'instructor')
    )
    all_trainees_info_button.grid(row=4,column=2)
    teaching_team_info_button=Button(
        frameinstructor,
        text='Teaching Team Details',
        command=lambda: teaching_teams_view(frameinstructor,username)

    )
    teaching_team_info_button.grid(row=6,column=2)
    coursedetailbutton2 = Button(
        frameinstructor,
        text='Course Details',
        command=lambda: course_details_view(frameinstructor, username, 'instructor')
    )
    coursedetailbutton2.grid(row=8, column=2)
    logoutbutton2 = Button(
        frameinstructor,
        text='Log out',
        command=lambda: log_out(frameinstructor)
    )
    logoutbutton2.grid(row=10, column=2)

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
    prompt_1.grid(row=0,column=0)
    db = connect()
    cursor = db.cursor()
    # query = "SELECT t_id,first_name,last_name,contact_no,email,joining_date,address,time_slot,course_name FROM (((trainee JOIN login using (username)) JOIN session using(session_id)) JOIN course using(course_id)) WHERE username ='"+username+"'"
    query = "SELECT * from student where username='"+username+"'"
    cursor.execute(query)
    result = cursor.fetchone()

    tidlabel1 = Label(frametrainee, text='Trainee ID:')
    tidlabel1.grid(row=1, column=0)
    fname1 = Label(frametrainee,text='Name: ')
    fname1.grid(row=1, column=1)
    contact1 = Label(frametrainee,text='Contact Number:')
    contact1.grid(row=1, column=2)
    email1 = Label(frametrainee,text='Email:')
    email1.grid(row=1, column=3)
    joiningdate1 = Label(frametrainee, text='Joining Date:')
    joiningdate1.grid(row=1, column=4)
    address1 = Label(frametrainee, text='Address: ')
    address1.grid(row=1, column=5)
    time_slot1 = Label(frametrainee, text='Time Slot:')
    time_slot1.grid(row=1, column=6)
    coursename1 = Label(frametrainee, text='Course Name:')
    coursename1.grid(row=1, column=7)
    tidlabel2 = Label(frametrainee,text=result[0])
    tidlabel2.grid(row=2, column=0)
    fname2 = Label(frametrainee,text=result[1]+" "+result[2])
    fname2.grid(row=2, column=1)
    contact2 = Label(frametrainee,text=result[3])
    contact2.grid(row=2, column=2)
    email2 = Label(frametrainee,text=result[4])
    email2.grid(row=2, column=3)
    joiningdate2 = Label(frametrainee,text=result[5])
    joiningdate2.grid(row=2, column=4)
    address2 = Label(frametrainee,text=result[6])
    address2.grid(row=2, column=5)
    time_slot2 = Label(frametrainee,text=result[7])
    time_slot2.grid(row=2, column=6)
    coursename2 = Label(frametrainee,text=result[8])
    coursename2.grid(row=2, column=7)
    cursor.close()
    db.close()

    coursedetailbutton = Button(
        frametrainee,
        text = 'Course Details',
        command= lambda: course_details_view(frametrainee,username,'trainee')
    )
    coursedetailbutton.grid(row=3,column=3)
    logoutbutton = Button(
        frametrainee,
        text = 'Log out',
        command=lambda: log_out(frametrainee)
    )
    logoutbutton.grid(row=5,column=3)

my_window.mainloop()
