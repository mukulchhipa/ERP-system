from tkinter import *
import MySQLdb
from PIL import ImageTk, Image
from tkinter import messagebox
import time
import datetime
import calendar
import random
from twilio.rest import Client
from smtplib import *
import smtplib

a=[]
db=MySQLdb.connect("localhost","root","","Attendance_tracker")
cursor=db.cursor()
user=Entry
admin_password=Entry
email_e=Entry
contact_e=Entry
loginsql=''
new_root=''
u0=''
p0=''
time1=''
send_button=Button
w = datetime.date.today()
name=''
today = "{:%d-%b-%Y}".format(w)
list_days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
value=datetime.datetime.today().weekday()
year=w.year
month_name = calendar.month_name[w.month]
mark_final=[]
dates_final=[]
print(mark_final,dates_final)
sql = """SELECT column_name
    FROM INFORMATION_SCHEMA.COLUMNS 
    WHERE TABLE_SCHEMA=database() 
        AND TABLE_NAME='record_%d'""" % (year)
cursor.execute(sql)
all_col = cursor.fetchall()
month_list = []
for i in range(4, len(all_col)-1):
    month_list.append(''.join(all_col[i]))
def _check_password(reset,u0,new_pass,confirm_pass):
    if new_pass.get()=="" or confirm_pass.get()=="":
        new_pass.configure(highlightbackground="red",highlightthickness=1)
        confirm_pass.configure(highlightbackground="red", highlightthickness=1)
        popup = messagebox.showerror("ERROR", "Kindly fill both the entries.", parent=reset)
        time.sleep(2)
        new_pass.configure(highlightbackground=None, highlightthickness=0)
        confirm_pass.configure(highlightbackground=None, highlightthickness=0)
    elif new_pass.get()!=confirm_pass.get():
        messagebox.showerror("ERROR","Passwords are not matching",parent=reset)
    elif new_pass.get()==confirm_pass.get() :
        if len(new_pass.get())>8 and len(new_pass.get())<13:
            store=cursor.execute("update profile set password='%s' where student_id='%s'"%(new_pass.get(),u0))
            db.commit()
            if store==1:
                messagebox.showinfo("SUCCESS","Password changed successfully.",parent=reset)
                reset.destroy()
        else:
            messagebox.showerror("ERROR!","Password should have a minimum length of 9\nand maximum length of 12",parent=reset)
def _reset_password(new_root,u0):
    reset=Toplevel(new_root)
    reset.geometry("500x150+450+250")
    reset.title("Change password!")
    reset.attributes('-topmost', 'true')
    reset.grab_set()
    Label(reset,text="New Password :",font=3).grid(row=0,column=0,pady=(15,10),padx=(20,0),sticky=NW)
    Label(reset, text="Confirm Password :",font=3).grid(row=1, column=0, pady=(15,10), padx=(20,0),sticky=NW)
    new_pass=Entry(reset,width=50,show="\u2022")
    new_pass.grid(row=0,column=1,pady=(20,0),sticky=NW)
    confirm_pass = Entry(reset, width=50,show="\u2022")
    confirm_pass.grid(row=1, column=1, pady=(20, 0), sticky=NW)
    btn = Button(reset, text='Change Password',width=20,command=lambda : _check_password(reset,u0,new_pass,confirm_pass))
    btn.grid(row=3,column=1,pady=(10,0),padx=(20,0))
def profile_fun(new_root,id):
    import tkinter as tk
    #global profile_root,back_btn
    new_root.destroy()
    profile_user=id
    profile_root=tk.Tk()
    profile_root.geometry("1366x768+0+0")
    profile_root.resizable(False,False)
    profile_root.title("Profile: %s"%(u0.title()))
    back_img = ImageTk.PhotoImage(Image.open('C:/Users/priyanka/Desktop/Icons/back.png'))
    backlbl = Label(profile_root, image=back_img)
    back.image = back_img

    back_btn = tk.Button(profile_root, text="BACK", relief=FLAT, image=back_img, bd=0,
                         command=lambda: _otp_or_password(profile_root,profile_user,name))
    back_btn.place(x=20, y=90)

    p_frame = tk.Frame(profile_root, height=80, width=1366, bg="black").place(x=0, y=0)
    e=tk.Label(p_frame, text="Institute Portal", font=('calibri', 30,'bold'),bg="black",fg="white")
    e.place(x=680, y=30,anchor='center')

    table_frame = tk.LabelFrame(profile_root,font=('arial',13,'bold'),text="Personal Details",bd=5,height=400, width=400)
    table_frame.place(x=150, y=150)

    guardian_frame = tk.LabelFrame(profile_root, font=('arial', 13, 'bold'), text="Guardian Details", bd=5, height=200,
                             width=400)
    guardian_frame.place(x=800, y=150)

    #========================Making Table=============================================================================
    sql="select column_name from INFORMATION_SCHEMA.COLUMNS where table_schema=database() and table_name='profile'"
    cursor.execute(sql)
    res0=cursor.fetchall()
    sql="select * from profile where Student_ID='%s'"%(profile_user)
    cursor.execute(sql)
    res1=cursor.fetchone()
    list0=list(res1)
    j=20
    for r in range(1,10):
        b=tk.Label(table_frame,font=('calibri',13,'bold'),text=res0[r])
        b.place(x=10,y=j)
        tk.Label(table_frame,font=('arial',11,'bold'),text=":").place(x=180,y=j)
        j+=35

    Label(table_frame,font=('calibri',13,'bold'),text=res0[10]).place(x=10,y=j)
    Label(table_frame, font=('arial', 11, 'bold'), text=":").place(x=180, y=j)
    j=20
    for k in range(11,14):
        b = tk.Label(guardian_frame, font=('calibri',13,'bold'), text=res0[k])
        b.place(x=10, y=j)
        tk.Label(guardian_frame, font=('arial', 11, 'bold'), text=":").place(x=140, y=j)
        j+=35
    j=20
    for r in range(1,10):
        b=tk.Label(table_frame,font=('calibri',13),text=list0[r])
        b.place(x=190,y=j)
        j+=35
    tk.Label(table_frame, font=('calibri', 13), text=list0[10]).place(x=190,y=j)
    j=20
    for k in range(11,14):
        b = tk.Label(guardian_frame, font=('calibri',13), text=list0[k])
        b.place(x=150, y=j)
        j+=35
    logout = ImageTk.PhotoImage(Image.open('C:/Users/priyanka/Desktop/Icons/logout.png'))
    logout_0 = Label(profile_root, image=logout)
    logout_0.image = logout

    btn = Button(profile_root, bd=0, image=logout, relief=FLAT, command=lambda :destroy_window(profile_root))
    btn.place(x=1290, y=90)
def student_forgot(user):

    if user.get()=='':
        messagebox.showerror("ERROR","Username is required")
    elif user.get()!='':
        check = cursor.execute("select * from profile where student_id='%s'" % (user.get()))
        if check==0:
            messagebox.showerror("ERROR!","This username is not registered.\nIn case,if you have forgotten your username\n"
                                          "kindly contact your admin.")
        else:
            otp=random.randint(11111,100000)
            otp=str(otp)
            cursor.execute("select contact from profile where student_id='%s'"%(user.get()))
            number=''.join(cursor.fetchone())
            message="Dear %s\n""Your OTP is %s\n""Kindly reset your password."%(user.get(),otp)
            send_sms(message,number)
            cursor.execute("update profile set otp='%s' where student_id='%s'"%(otp,user.get()))
            db.commit()
            messagebox.showinfo("Password","We have messaged you an OTP!\nNow you can reset your password")
def _otp_or_password(any_root,u0,name):
    any_root.destroy()
    new_root = Tk()
    new_root.geometry("1366x768+0+0")
    new_root.resizable(False,False)
    new_root.title("Student: '%s'" % name)
    frame1 = Frame(new_root, height=80, width=1366, bg="black").place(x=0, y=0)
    Label(frame1, text="Institute Portal", font=('calibri', 30,'bold'), fg="white", bg="black").place(x=680, y=30,anchor="center")
    w = datetime.date.today()
    today = "{:%d-%b-%Y}".format(w)
    date = Label(new_root, font=('times', 20, 'bold'), fg="steel blue", text=today)
    date.place(x=400, y=100)
    day_lbl = Label(new_root, font=('times', 20, 'bold'), fg="steel blue")
    day_lbl.place(x=580, y=100)
    day(day_lbl)
    clock = Label(new_root, font=('times', 20, 'bold'), fg="steel blue")
    clock.place(x=755, y=100)
    tick(clock)
    icon_frame = Frame(new_root, height=600, width=1366)
    icon_frame.place(x=0, y=140)

   # ========================IMAGES=============================================================================
    img = ImageTk.PhotoImage(Image.open('C:/Users/priyanka/Desktop/Icons/profile.png'))
    profile = Label(icon_frame, image=img)
    profile.image = img

    att_img = ImageTk.PhotoImage(Image.open('C:/Users/priyanka/Desktop/Icons/attendance.png'))
    att = Label(icon_frame, image=att_img)
    att.image = att_img

    reset_img = ImageTk.PhotoImage(Image.open('C:/Users/priyanka/Desktop/Icons/reset.png'))
    reset = Label(icon_frame, image=reset_img)
    reset.image = reset_img

    logout_img = ImageTk.PhotoImage(Image.open('C:/Users/priyanka/Desktop/Icons/logout.png'))
    logout = Label(icon_frame, image=logout_img)
    logout.image = logout_img

    # =====================image buttons==========================================================
    profile_btn = Button(icon_frame, image=img, relief=FLAT, command=lambda: profile_fun(new_root, u0), bd=0)
    profile_btn.place(x=350, y=90)
    profile_lbl = Label(icon_frame, text="View Profile", font=11).place(x=350, y=170)

    att_btn = Button(icon_frame, image=att_img, relief=FLAT, bd=0,command=lambda :_ViewYourAttendance(new_root,u0))
    att_btn.place(x=650, y=90)
    att_lbl = Label(icon_frame, text="View Attendance", font=11).place(x=650, y=170)

    reset_btn = Button(icon_frame, image=reset_img, relief=FLAT, bd=0,command=lambda:_reset_password(new_root,u0))
    reset_btn.place(x=950, y=90)
    reset_lbl = Label(icon_frame, text="Reset Password", font=11).place(x=950, y=170)

    logout_btn = Button(new_root, image=logout_img, relief=FLAT, command=lambda :destroy_window(new_root))
    logout_btn.place(x=1290, y=90)

    '''logout_btn = Button(icon_frame,command=exit, text="Log out", font=('arial', 15), width=17, fg="black", relief=FLAT)
    logout_btn.place(x=0, y=270)'''
def send_mail(from_user,from_pwd,to_user,subject,message):
    header = 'to:' + to_user + '\n' + 'From:' + from_user + '\n' + 'Subject:' + subject
    #password = random.randint(1, 990000)
    msg = header + str(message)
    try:
        smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
        print("1 from smtp")
        smtpObj.ehlo()
        print("2 from smtp")
        smtpObj.starttls()
        print("3 from smtp")
        smtpObj.login(from_user, from_pwd)
        print(msg)
        smtpObj.sendmail(from_user, to_user, msg)
        print("5 from smtp")


    except SMTPException as e:
        messagebox.showerror("Error!","ENABLE TO SEND MESSAGE.", e)
        admin_password.configure(state='normal')
def send_mail_details(splashscreen,mail_id,Subject,message_entry,username):
    global admin_password
    cursor.execute("select Email_ID from profile")
    email_in_db = cursor.fetchall()
    subject=Subject.get(1.0,"end")
    message = (message_entry.get(1.0, "end"))
    people = []
    from_pwd=admin_password.get()
    admin_password.delete(0,"end")

    list_of_email = [element for tupl in email_in_db for element in tupl]
    print(list_of_email)
    recievers = (mail_id.get())
    search = ","
    search2 = " "
    if search in recievers:
        people = recievers.split(",")
        for match in range(len(people)):
            if (people[match] in list_of_email):
                continue
            else:
                messagebox.showerror("ERROR", people[match] + " is an unregistered E-mail ID")
                break

    elif search2 in mail_id.get():
        messagebox.showerror("Error", "Please remove spaces")


    else:
        people.append(recievers)
        for i in range(len(people)):
            check = cursor.execute(
                "select * from profile where Email_ID ='%s' " % ( people[i]))
            if check != 0:
                if len(message) < 2:
                    messagebox.showerror("Error", "Message body is empty")

                else:
                    cursor.execute("select email_id from admin where username='%s'" % (username))
                    from_user = ''.join(cursor.fetchone())
                    print(str(from_user), from_pwd, recievers, subject, message)

                    try:
                        for person in range(len(people)):
                            send_mail(from_user, from_pwd, people[person], subject, message)
                        messagebox.showinfo("Message sent", "Mail sent successfully")
                        destroy(splashscreen)
                    except:
                        messagebox.showerror("Error!", "Unable to send messsages\nCheck if your password is correct.")

            else:
                messagebox.showerror("Invalid number", people[i]+" is an invalid or unregistered email ID.")
                break


        # button.configure(state="disabled")
def send_mail_setup(any_root,username):
        global admin_password
        splashscreen = Toplevel(any_root, relief=RAISED, bd=2, bg="#CCD6E5")
        splashscreen.title("New Message")
        splashscreen.grab_set()
        splashscreen.geometry("600x350+350+150")
        # Label(splashscreen, text="New Message"+"               ", font=('calibri', 16, 'bold'), fg="black",width=20).grid(row=0,column=0)
        Label(splashscreen, text="To :", font=('calibri', 13, 'bold'), bg="#CCD6E5").grid(row=2, column=0,
                                                                                                   padx=(10, 0),
                                                                                                   pady=(10, 0))
        mail_id = Entry(splashscreen, width=57)
        mail_id.grid(row=2, column=1, pady=(20, 0))

        Label(splashscreen, text="Subject :", font=('calibri', 13, 'bold'), bg="#CCD6E5").grid(row=3, column=0,
                                                                                               padx=(10, 0), pady=(10, 0))
        Subject = Text(splashscreen, width=43, height=2)
        Subject.grid(row=3, column=1, columnspan=2, pady=(10, 0))

        Label(splashscreen, text="Message :", font=('calibri', 13, 'bold'), bg="#CCD6E5").grid(row=4, column=0,
                                                                                               padx=(10, 0), pady=(10, 0))
        message_entry = Text(splashscreen, width=43, height=10)
        message_entry.grid(row=4, column=1, columnspan=2, pady=(10, 0))
        Label(splashscreen, text="Enter your password :", font=('calibri', 13, 'bold'), bg="#CCD6E5").grid(row=5, column=0,
                                                                                               padx=(10, 0),
                                                                                               pady=(10, 0))
        admin_password = Entry(splashscreen, width=57,show="\u2022")
        admin_password.grid(row=5, column=1,  pady=(10, 0))

        send_button = Button(splashscreen, bd=1, relief=RIDGE, activebackground="#CCD6E5", text="Send", width=15,
                             height=1,command=lambda :send_mail_details(splashscreen,mail_id,Subject,message_entry,username))
        send_button.grid(row=6, column=1, pady=(10, 0),columnspan=2)
def register(splashscreen,entry_widgets):
    get=[]
    for check in range(len(entry_widgets)):
        if entry_widgets[check].get()=="":
            messagebox.showerror("Insufficient information","Fill up all the fields.",parent=splashscreen)
            break
        else:
            pass
    for check in range(0,len(entry_widgets)):
        if check==0:
            checking=cursor.execute("select * from profile where student_id='%s'"%(entry_widgets[check].get()))
            if checking==1:
                messagebox.showerror("ERROR","This ID has been taken by someone else\nKindly enter a different ID.")
                break
            else:
                get.append(entry_widgets[check].get())
        if check==3:
            import datetime
            inputDate = entry_widgets[check].get()
            string = ''.join(inputDate)
            count0 = string.count("/")
            if count0 ==2:
                day, month, year = inputDate.split('/')
                isValidDate = True
                try:
                    datetime.datetime(int(year), int(month), int(day))
                except ValueError:
                    isValidDate = False
                if (isValidDate):
                    get.append(inputDate)
                else:
                    messagebox.showerror("Error!", "Invalid date format.")
                    break
            else:
                messagebox.showerror("Format error!","Date format should be dd/mm/yyyy")
                break



        if check==5:
            checking = cursor.execute("select * from profile where Email_id='%s'" % (entry_widgets[check].get()))
            if checking == 1:
                messagebox.showerror("ERROR", "Duplicate entry for email.\nKindly enter a different ID.")
                break
            else:
                lst = re.findall('\S+@\S+', entry_widgets[check].get())
                if len(lst)!=1:
                    messagebox.showerror("Invalid!","This is not an email id")
                    break
                else:
                    for i in range(len(lst)):
                        string = ''.join(lst[i])
                        count0 = string.count("@")
                        if count0 > 1:
                            messagebox.showerror("Invalid!","Invalid format of email id")
                            break
                        else:
                            get.append(entry_widgets[check].get())
        if check==6 or check==12:
            number=entry_widgets[check].get()
            print(number)
            lst0 = []
            for i in range(len(number)):
                if number[i].isdigit():
                    lst0.append(number[i])
                else:
                    break
            print(lst0)
            if len(lst0) != 10:
                messagebox.showerror("Invalid Entry!","Invalid mobile number.")
                break
            else:
                get.append(entry_widgets[check].get())
        if check==7:
            checking = cursor.execute("select * from profile where aadhar_card_number='%s'" % (entry_widgets[check].get()))
            if checking == 1:
                messagebox.showerror("ERROR", "Duplicate entry for aadhar card number\nKindly enter your original aadhar card number.")
                break
            else:
                length=len(entry_widgets[check].get())
                if length!=12:
                    messagebox.showerror("ERROR!","Invalid aadhar card number")
                else:
                    get.append(entry_widgets[check].get())

        else:
            get.append(entry_widgets[check].get())
    get0 = []
    [get0.append(item) for item in get if item not in get0]
    print(get0)#list having no duplicate entry (entries are in order too).

    if get0:
        reciever=get0[6]
        password = random.randint(11111, 100000)
        password = str(password)
        message = "Dear %s,\nYour password is %s\nKindly reset the password after login. " % (get0[1], password)
        return_value = send_sms(message, reciever)
        if return_value == 1:
            import datetime
            cursor.execute(
                "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`=database() AND `TABLE_NAME`='profile'")
            columns = cursor.fetchall()
            string = ''.join(columns[1])

            d = datetime.date.today()
            _year = d.year
            cursor.execute("insert into profile (%s) values ('%s')" % (string, get0[0]))
            db.commit()
            cursor.execute("insert into record_%d (student_id,first_name,last_name) values ('%s','%s','%s')" % (
            _year, get0[0], get0[1], get0[2]))

            db.commit()
            '''if there is a new student or late admission you have to go to local host database to set his previous
                date wise attendance='A' as I haven't created the way of inserting absent for all days 
                before his registration.
                        '''

            for values in range(1, len(get0)):
                string = ''.join(columns[values + 1])
                cursor.execute("update profile set %s= '%s' where student_id='%s';" % (string, get0[values], get0[0]))
                db.commit()
            messagebox.showinfo("Registered", "Successfully registered")
            cursor.execute("update profile set password='%s' where student_id='%s'" % (password, get0[0]))
            db.commit()
            destroy(splashscreen)
        else:
            messagebox.showerror("ERROR", "Wrong student mobile number.")
def send_sms(message,reciever):
    # /usr/bin/env python
    # Download the twilio-python library from twilio.com/docs/libraries/python

    # Find these values at https://twilio.com/user/account
    account_sid = "Get your id from twilio"
    auth_token = "auth token"
    client = Client(account_sid, auth_token)
    try:
        client.api.account.messages.create(
        to="+91" + reciever,
        from_="number generated from twilio",
        body=message)
        return 1
    except:
        return 0
def student_register(any_root,username):
    print("1")
    entry_widgets=[]
    splashscreen=Toplevel(any_root,relief=RAISED,bd=3,bg="#CCD6E5")
    splashscreen.overrideredirect("True")
    splashscreen.grab_set()
    splashscreen.geometry("700x560+350+70")
    Label(splashscreen,text="Enter Student Details",font=('calibri',20,'bold'),fg="black",bg="#CCD6E5").place(x=0,y=40, anchor="c", relx=.50)
    img = ImageTk.PhotoImage(Image.open('C:/Users/priyanka/Desktop/Icons/cross.png'))
    quit_image= Label(splashscreen, image=img)
    quit_image.image = img
    quit_button=Button(splashscreen,image=img,command=lambda:destroy(splashscreen),bd=0,relief=FLAT,highlightthickness=0).place(x=600,y=20)
    Label(splashscreen, text="Provide student id:", font=('calibri', 16), fg="black", bg="#CCD6E5").place(x=30,y=100)
    Id=Entry(splashscreen,width=60)
    Id.place(x=220,y=105)
    entry_widgets.append(Id)
    Label(splashscreen, text="First Name:", font=('calibri', 16), fg="black", bg="#CCD6E5").place(x=30, y=150)
    f_name= Entry(splashscreen, width=40)
    f_name.place(x=30, y=180)
    entry_widgets.append(f_name)
    Label(splashscreen, text="Last Name:", font=('calibri', 16), fg="black", bg="#CCD6E5").place(x=400, y=150)
    l_name = Entry(splashscreen, width=40)
    l_name.place(x=400, y=180)
    entry_widgets.append(l_name)
    Label(splashscreen, text="DOB:", font=('calibri', 16), fg="black", bg="#CCD6E5").place(x=30, y=210)
    dob = Entry(splashscreen, width=40)
    dob.place(x=30, y=240)
    entry_widgets.append(dob)
    Label(splashscreen, text="Gender:", font=('calibri', 16), fg="black", bg="#CCD6E5").place(x=400, y=210)
    gen = Entry(splashscreen, width=40)
    gen.place(x=400, y=240)
    entry_widgets.append(gen)
    Label(splashscreen, text="E-mail ID:", font=('calibri', 16), fg="black", bg="#CCD6E5").place(x=30, y=270)
    email = Entry(splashscreen, width=40)
    email.place(x=30, y=300)
    entry_widgets.append(email)
    Label(splashscreen, text="Student Contact Number:", font=('calibri', 16), fg="black", bg="#CCD6E5").place(x=400, y=270)
    stu_contact = Entry(splashscreen, width=40)
    stu_contact.place(x=400, y=300)
    entry_widgets.append(stu_contact)
    Label(splashscreen, text="Aadhar Card Number:", font=('calibri', 16), fg="black", bg="#CCD6E5").place(x=30, y=330)
    aadhar= Entry(splashscreen, width=40)
    aadhar.place(x=30, y=360)
    entry_widgets.append(aadhar)
    Label(splashscreen, text="Nationality:", font=('calibri', 16), fg="black", bg="#CCD6E5").place(x=400, y=330)
    nationality = Entry(splashscreen, width=40)
    nationality.place(x=400, y=360)
    entry_widgets.append(nationality)
    Label(splashscreen, text="Religion:", font=('calibri', 16), fg="black", bg="#CCD6E5").place(x=30, y=390)
    religion = Entry(splashscreen, width=40)
    religion.place(x=30, y=420)
    entry_widgets.append(religion)
    Label(splashscreen, text="Father's Name:", font=('calibri', 16), fg="black", bg="#CCD6E5").place(x=400, y=390)
    father = Entry(splashscreen, width=40)
    father.place(x=400, y=420)
    entry_widgets.append(father)
    Label(splashscreen, text="Mother's Name:", font=('calibri', 16), fg="black", bg="#CCD6E5").place(x=30, y=450)
    mother = Entry(splashscreen, width=40)
    mother.place(x=30, y=480)
    entry_widgets.append(mother)
    Label(splashscreen, text="Parent's Contact number:", font=('calibri', 16), fg="black", bg="#CCD6E5").place(x=400, y=450)
    parent_contact = Entry(splashscreen, width=40)
    parent_contact.place(x=400, y=480)
    entry_widgets.append(parent_contact)
    _Register_button=Button(splashscreen,text="Register!",width=14,command=lambda :register(splashscreen,entry_widgets)).place(x=0,y=530,relx=0.49,anchor="c")
def student_login(root):
    global new_root,u0,p0,loginsql
    if user.get()=='' or password.get()=='':
        messagebox.showerror("ERROR","Enter both fields to get access!")
    else:
        ID=user.get()
        password_e=password.get()
        #print(username,password_e)
        loginsql=""" select password from profile where Student_ID='%s'"""%(ID)
        u0=ID
        p0=password_e
        back(root)
def back(any_root):
    global name
    cursor.execute("""select First_name from profile where Student_ID='%s'"""%(u0))
    name1=cursor.fetchone()
    name1=''.join(name1)
    cursor.execute("""select Last_name from profile where Student_ID='%s'""" % (u0))
    name2=cursor.fetchone()
    name2 = ''.join(name2)
    name=name1+name2
    _OTPsql = """ select otp from profile where Student_ID='%s'""" % (u0)

    '''sql=s
    password_e=p'''
    #any_root.mainloop()
    if p0=="1":
        messagebox.showerror("Error","Wrong password")
    else:

        res=cursor.execute(loginsql);print(res)
        res1="".join(cursor.fetchone());print(res1)
        OTPsql=cursor.execute(_OTPsql);print(OTPsql)
        otp = cursor.fetchone();print(otp)
        if isinstance(otp,tuple):
            otp = ''.join(otp)
            pass
        else:
            pass
        print(p0,otp)
        if (res!=0 and res1==p0 ) :
            print("password")
            if OTPsql!=0:
                cursor.execute("update profile set otp = 1 where student_id='%s'" % (u0))
                db.commit()
                _otp_or_password(any_root,u0,name)
            else:
                _otp_or_password(any_root, u0, name)
        elif (OTPsql!=0 and otp==p0 ):
            print("otp")

            cursor.execute("update profile set otp = '1' where student_id='%s'" % (u0))
            db.commit()
            _otp_or_password(any_root, u0, name)
        else:
            messagebox.showerror("ERROR!", "Incorrect password or username")
def destroy(splash):
    splash.destroy()
def _ViewYourAttendance(new_root,u0):
    from datetime import datetime
    def record():
        sql = """SELECT column_name
            FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_SCHEMA=database() 
                AND TABLE_NAME='record_%d'""" % (year)
        cursor.execute(sql)
        all_col = cursor.fetchall()
        month_list = []
        for i in range(4, len(all_col) - 1):
            month_list.append(''.join(all_col[i]))
        print(month_list)
        sql = """SELECT column_name
            FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_SCHEMA=database() 
                AND TABLE_NAME='record_%d'""" % (year)
        cursor.execute(sql)
        all_col = cursor.fetchall()
        month_list = []
        for i in range(4, len(all_col) - 1):
            month_list.append(''.join(all_col[i]))
        total_classes_list = []
        whole_attendance = []
        for i in range(len(month_list)):
            sql = """SELECT %s
            FROM
            record_%d where student_id='16bca73'""" % (month_list[i], year)
            cursor.execute(sql)
            ab = cursor.fetchone()
            print(ab)
            total_classes_list.append(ab[0])
            ab = ''.join(ab[0])
            ab = ab.split(',')
            print(ab)
            ab[:] = [item for item in ab if item != ' ' and item != '']
            print(ab)

            whole_attendance.append(ab)
        print(whole_attendance)
        final_list = [[0 for inner in range((len(whole_attendance[outer])))] for outer in range(len(whole_attendance))]
        for outer in range(len(whole_attendance)):
            for inner in range(len(whole_attendance[outer])):
                string = whole_attendance[outer][inner].replace(" ", "")
                final_list[outer][inner] = string
        print("final='%s'"%final_list)  # dates and their respective attendance together (number of months=number of inner lists)
        mark = [[0 for inner in range(len(final_list[outer]))] for outer in
                range(len(final_list))]
        dates = [[0 for _inner in range(len(final_list[_outer]))] for _outer in
                 range(len(final_list))]
        for outer in range(0, len(final_list)):
            for inner in range(0, len(final_list[outer])):
                pos = re.findall(r'[A-Za-z]', final_list[outer][inner])  # searching 'p' and 'a' in final list
                mark[outer][inner] = (pos)
                print(mark[outer][inner])
                _pos = re.findall('\d+', final_list[outer][inner])  # searching dates in final list
                dates[outer][inner] = (_pos)
        print(dates,"\n",mark)
        total_classes=0
        for outer in range(0, len(dates)):
            total_classes += len(dates[outer])#number of classes till date
        for length in range(0,total_classes):
            Label(frame,text=length+1 ,font=('calibri',13),bg="white").grid(row=length,column=0,padx=(43,0),pady=(15,0),sticky="NW")
            Label(frame, text="All", font=('calibri', 13), bg="white").grid(row=length, column=1, padx=(130, 0),
                                                                                 pady=(15, 0), sticky="NW")
        length=0
        for Outer_index in range(len(dates)):
            for Inner_index in range(len(dates[Outer_index])):
                date = str(dates[Outer_index][Inner_index][0])+"-"+str(month_list[Outer_index])+"-"+str(year)
                d = datetime.strptime(date, '%d-%B-%Y')
                _Date=d.date()

                Label(frame, text=_Date, font=('calibri', 13), bg="white")\
                    .grid(row=length, column=2, padx=(130, 0),pady=(15, 0), sticky="NW")

                PA=Label(frame, text=mark[Outer_index][Inner_index][0], font=('calibri', 13), bg="white",fg="black")
                PA.grid(row=length, column=3, padx=(130, 0), pady=(15, 0), sticky="NW")
                if PA.cget("text")=='A':
                    PA.configure(fg='red')
                length+=1
    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    new_root.destroy()
    view_att = Tk()
    view_att.geometry("800x768+341+0")
    view_att.resizable(False,False)
    frame1 = Frame(view_att, height=60, width=800, bg="black").place(x=0, y=0)
    Label(frame1, text="Institute Portal ", font=('calibri', 25,'bold'), fg="white", bg="black").place(x=400, y=10,anchor="center")
    back_img = ImageTk.PhotoImage(Image.open('C:/Users/priyanka/Desktop/Icons/back.png'))
    backlbl = Label(view_att, image=back_img)
    back.image = back_img
    back_btn = Button(view_att, relief=FLAT, image=back_img, bd=0,
                      command=lambda: _otp_or_password(view_att,u0,name))
    back_btn.place(x=20, y=68)
    attendance_frame = Frame(view_att, relief=RAISED, bd=2,
                             height=590, width=774)
    attendance_frame.place(x=10, y=120)

    attendance_frame.grid_propagate(0)
    Label(attendance_frame, text="Lecture", font=('calibri', 14, 'bold')).grid(row=0, column=0, padx=(40, 5),
                                                                             pady=(30, 0))
    Label(attendance_frame, text="Subject", font=('calibri', 14, 'bold')).grid(row=0, column=1, padx=(95, 0),
                                                                               pady=(30, 0))
    Label(attendance_frame, text="Date", font=('calibri', 14, 'bold')).grid(row=0, column=2, padx=(115, 0),
                                                                            pady=(30, 0))
    Label(attendance_frame, text="Status", font=('calibri', 14, 'bold')).grid(row=0, column=3, padx=(133, 0),
                                                                              pady=(30, 0))

    btn = Button(attendance_frame, width=15,bd=3,relief=RIDGE, text="Get PDF")
    btn.place(x=50, y=530)

    cursor.execute("select status from record_%d where student_id='%s'" % (year, u0))
    Status = ''.join(cursor.fetchone())
    filtered = ''.join(re.findall("\d+\.\d+", Status))
    Status_lbl = Label(attendance_frame, text="Your attendance status: " +filtered+"%", font=('calibri', 13))
    Status_lbl.place(x=500, y=530)

    attendance_frame2 = Frame(attendance_frame, bd=4, height=450, width=740).place(x=0, y=80)
    myframe = Frame(attendance_frame2, relief=GROOVE, width=754, height=430, bd=0)
    myframe.place(x=20, y=200)
    myframe.propagate(FALSE)
    canvas = Canvas(myframe, width=710, height=440, bg="white")
    canvas.place(x=10, y=-10)
    canvas.propagate(FALSE)
    frame = Frame(canvas, width=1466, height=768, bg="white")
    frame.place(x=0, y=20)

    frame.propagate(FALSE)

    myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right", fill="y")
    # canvas.pack(side="left")
    canvas.create_window((50, 150), window=frame)  # (0,0)=x,y
    frame.bind("<Configure>", myfunction)

    record()
def check_attendance(new_root_ad,username,sql):
    global mark_final,dates_final,all_col,month_list
    new_root_ad.destroy()
    view_att=Tk()
    view_att.geometry("1366x768+0+0")
    view_att.resizable(False,False)
    frame1 = Frame(view_att, height=60, width=1366, bg="black").place(x=0, y=0)
    Label(frame1, text="Institute Portal ", font=('calibri', 25,'bold'), fg="white", bg="black").place(x=680, y=30,anchor="center")
    back_img = ImageTk.PhotoImage(Image.open('C:/Users/priyanka/Desktop/Icons/back.png'))
    backlbl = Label(view_att, image=back_img)
    back.image = back_img
    back_btn =Button(view_att, relief=FLAT, image=back_img, bd=0,
                         command=lambda: admin_back(view_att,username,sql))
    back_btn.place(x=20, y=68)
    attendance_frame = Frame(view_att, relief=RAISED, bd=2,
                             height=590, width=1340)
    attendance_frame.place(x=10, y=120)

    attendance_frame.pack_propagate(False)
    #_detain_btn=Button(attendance_frame,text="Get detain list",command=get_detain_list)
    cursor.execute("select first_name from record_2018")
    res = cursor.fetchall()
    cursor.execute("select student_ID from record_2018")
    res1 = cursor.fetchall()
    cursor.execute("select last_name from record_2018")
    res2 = cursor.fetchall()
    list3 = []
    list2 = []
    for i in range(len(res2)):
        res_new = "".join(res[i])
        res2_new = "".join(res2[i])
        list3.append(res_new + " " + res2_new)
    for i in range(len(res2)):
        list2.append(''.join(list3[i]))
    attendance_frame.grid_propagate(False)
    '''b = Label(attendance_frame, font=('calibri', 14, 'bold'), text="Check")
    b.grid(row=0,column=1,padx=(70,30),pady=(10,10))'''
    b = Label(attendance_frame, font=('calibri', 14, 'bold'), text="S.No.")
    b.grid(row=0, column=2, padx=(55, 45))
    b = Label(attendance_frame, font=('calibri', 14, 'bold'), text="Student name")
    b.grid(row=0, column=3, padx=(30, 50), pady=(10, 10))
    b = Label(attendance_frame, font=('calibri', 14, 'bold'), text="Student ID")
    b.grid(row=0, column=4, padx=(30, 30), pady=(10, 10))
    b = Label(attendance_frame, font=('calibri', 14, 'bold'), text="Total classes")
    b.grid(row=0, column=5, padx=(30, 30), pady=(10, 10))
    b = Label(attendance_frame, font=('calibri', 14, 'bold'), text="Present")
    b.grid(row=0, column=6, padx=(35, 35), pady=(10, 10))
    b = Label(attendance_frame, font=('calibri', 14, 'bold'), text="Absent")
    b.grid(row=0, column=7, padx=(40, 35), pady=(10, 10))
    b = Label(attendance_frame, font=('calibri', 14, 'bold'), text="Present%")
    b.grid(row=0, column=8, padx=(60, 30), pady=(10, 10))
    b = Label(attendance_frame, font=('calibri', 14, 'bold'), text="Absent%")
    b.grid(row=0, column=9, padx=(50, 30), pady=(10, 10))

    id_list = []
    for i in range(len(res1)):
        id_list.append(''.join(res1[i]))
    listOfRadioB = []
    '''def sel(i):
        a = listOfRadioB[i].get()'''
    var = StringVar()
    w = datetime.date.today()
    year = w.year
    '''sql = """SELECT column_name
    FROM INFORMATION_SCHEMA.COLUMNS 
    WHERE TABLE_SCHEMA=database() 
        AND TABLE_NAME='record_%d'""" % (year)
    cursor.execute(sql)
    all_col = cursor.fetchall()
    month_list = []
    for i in range(4, len(all_col)-1):
        month_list.append(''.join(all_col[i]))'''
    total_classes_list = []
    whole_attendance = ['']
    for i in range(len(month_list)):
        sql = """SELECT %s
        FROM
        record_%d """ % (month_list[i], year)
        cursor.execute(sql)
        ab = cursor.fetchall()
        total_classes_list.append(ab[0])
        whole_attendance.append(ab)
    del whole_attendance[0]
    total_classes_str = ''
    for i in range(len(total_classes_list)):
        total_classes_str += ''.join(total_classes_list[i])
    total_classes_str = total_classes_str.split(",")
    total_classes_str = list(filter(lambda space: space.strip(), total_classes_str))
    list_of_tuples = []
    for i in range(len(whole_attendance)):
        list_of_tuples.append("list" + "%d" % (i))
    for i in range(len(whole_attendance)):
        list_of_tuples[i] = (whole_attendance[i])
    list_of_lists = [list(elements) for elements in list_of_tuples]

    outputarray = []
    for i in range(0, len(list_of_lists[0])):
        outputarray.append("list" + "%d" % i)
    for i in range(0, len(list_of_lists[0])):
        outputarray[i] = []
        for j in list_of_lists:
            outputarray[i].append(j[i])
    print("outputarray=",outputarray)
    ExtractingAttendanceList = []
    for i in range(len(outputarray)):
        extracting_attendance = "".join(map("".join, outputarray[i]))
        extracting_attendance = extracting_attendance.split(",")
        del extracting_attendance[0]
        ExtractingAttendanceList.append(extracting_attendance)
    print("outputarray=",outputarray)
    print("Extractingattendancelist",ExtractingAttendanceList)
    for i in range(len(ExtractingAttendanceList)):
        # for j in range (len(ExtractingAttendanceList[i])):
        ExtractingAttendanceList[i] = list(filter(None, ExtractingAttendanceList[i]))
        # ExtractingAttendanceList[i][j]=ExtractingAttendanceList[i][j].replace(" ","")
    print("outputarray=", outputarray)
    print("Extractingattendancelist", ExtractingAttendanceList)
    mark = [[0 for inner in range(len(ExtractingAttendanceList[outer]))] for outer in
            range(len(ExtractingAttendanceList))]
    dates = [[0 for _inner in range(len(ExtractingAttendanceList[_outer]))] for _outer in
             range(len(ExtractingAttendanceList))]
    for outer in range(0, len(ExtractingAttendanceList)):
        for inner in range(0, len(ExtractingAttendanceList[outer])):
            pos = re.findall(r'[A-Za-z]', ExtractingAttendanceList[outer][inner])
            mark[outer][inner] = (pos)
            print(mark[outer][inner])
            _pos = re.findall('\d+', ExtractingAttendanceList[outer][inner])
            dates[outer][inner] = (_pos)
    flat_mark = [item for sublist in mark for item in sublist]
    flat_dates = [item for sublist in dates for item in sublist]
    flat_mark = [item for sublist in flat_mark for item in sublist]
    flat_dates = [item for sublist in flat_dates for item in sublist]

    # print(flat_dates,"\n",flat_mark)
    mark_final = [flat_mark[sets:sets + len(total_classes_str)] for sets in
                  range(0, len(flat_dates), len(total_classes_str))]
    dates_final = [flat_dates[sets:sets + len(total_classes_str)] for sets in range(0, 1)]
    print(dates_final)
    dates_final = [item for sublist in dates_final for item in sublist]
    print(dates_final)
    def data():

        for i in range(len(res)):
            '''R2 = Radiobutton(frame,variable=var, value=id_list[i], command=lambda :sel(i),bg="white",tristatevalue="x",activebackground="powder blue")
            R2.grid(row=i,column=0,padx=(70,30),pady=(20,20))
            listOfRadioB.append(var)'''
            Label(frame, text=i + 1, bg="white", font='10').grid(row=i, column=1, padx=(50, 30), pady=(20, 20))
            Name = Label(frame, text=list2[i], bg="white", font=10)
            Name.grid(row=i, column=2, padx=(78, 30), pady=(20, 20), sticky="NW")
            ID = Label(frame, text=res1[i], bg="white", font=10)
            ID.grid(row=i, column=3, padx=(30, 30), pady=(20, 20),
                    sticky="NW")
            _totalClasses = Label(frame, text=len(total_classes_str), bg="white", font=10)
            _totalClasses.grid(row=i, column=4, padx=(90, 30), pady=(20, 20),
                               sticky="NW")

            _presentLabel = Label(frame, text=mark_final[i].count('P'), bg="white", font=10)
            _presentLabel.grid(row=i, column=5, padx=(100, 30), pady=(20, 20),
                               sticky="NW")
            _absentLabel = Label(frame, text=mark_final[i].count('A'), bg="white", font=10)
            _absentLabel.grid(row=i, column=6, padx=(90, 30), pady=(20, 20),
                              sticky="NW")
            _presentPercentage = Label(frame, text=((_presentLabel.cget("text") / _totalClasses.cget("text")) * 100),
                                       bg="white", font=10)
            _presentPercentage.grid(row=i, column=7, padx=(90, 30), pady=(20, 20),
                                    sticky="NW")
            _absentPercentage = Label(frame, text=(100 - float(_presentPercentage.cget("text"))), bg="white", font=10)
            _absentPercentage.grid(row=i, column=8, padx=(60, 85), pady=(20, 20),
                                   sticky="NW")
            if _presentPercentage.cget("text") < 75.00:
                _presentPercentage.configure(fg="red")
                Name.configure(fg="red")
                ID.configure(fg="red")

            _presentPercentage.configure(text=("%.2f %%") % _presentPercentage.cget("text"));
            _absentPercentage.configure(text=("%.2f %%") % _absentPercentage.cget("text"))

            cursor.execute("update record_%d set status='%s' where student_id='%s'"%(year,_presentPercentage.cget("text"),ID.cget("text")))
            db.commit()

    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    attendance_frame2 = Frame(attendance_frame, bd=4, height=450, width=1320).place(x=5, y=50)

    attendance_frame.propagate(0)
    myframe = Frame(attendance_frame2, relief=GROOVE, width=1320, height=500, bd=0, bg="green")
    myframe.place(x=20, y=176)
    myframe.propagate(FALSE)
    canvas = Canvas(myframe, width=1466, bg="#F0F0F0", height=500)
    canvas.place(x=0, y=0)
    canvas.propagate(FALSE)
    frame = Frame(canvas, width=1466, height=500, bg="white")
    frame.place(x=0, y=0)

    frame.pack_propagate(0)

    myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right", fill="y")
    # canvas.pack(side="left")
    canvas.create_window((50, 150), window=frame)  # (0,0)=x,y
    frame.bind("<Configure>", myfunction)

    data()

    '''option_frame=Frame(view_att,height=200,width=800)
    option_frame.place( anchor="c", relx=0.5, rely=0.35)
    option_frame.pack_propagate(False)'''
def admin_login(win):
    global new_root_ad
    username = user.get()
    password_e = password.get()
    # print(username,password_e)
    sql = """ select password from admin where username='%s'""" % (username)
    print(sql)
    admin_back(win,username,sql)
def send_message(splashscreen,numbers,message_entry):
    cursor.execute("select contact , contact_number from profile")
    contact=cursor.fetchall()
    message=(message_entry.get(1.0,"end"))
    print(len(message))
    list_of_contacts = [element for tupl in contact for element in tupl]
    print(list_of_contacts)
    recievers=''.join(numbers.get())
    if len(recievers)>10:
        search = ","
        search2=" "
        if search in recievers:
            recievers=recievers.split(",")
            for match in range(len(recievers)):
                if (recievers[match]==list_of_contacts[match] )and (len(recievers[match])==10):
                    if len(message) < 2:
                        messagebox.showerror("Error", "Message body is empty")

                    else:
                        try:
                            for person in range(len(recievers)):
                                send_sms(message, recievers[person])
                            messagebox.showinfo("Message sent", "Message sent successfully")
                            destroy(splashscreen)
                        except:
                            messagebox.showerror("Error!", "Unable to send messsages.")
                else:
                    messagebox.showerror("ERROR",recievers[match]+" is an unregistered number")
                    break
        else:
            messagebox.showerror("Error","Please separate mobile numbers with comma (,) if there are multiple."
                                         "\nAlso there should be no spaces. ")
        if search2 in recievers:
            messagebox.showerror("Error","Remove spaces")

    elif len(recievers)<=10:
        check=cursor.execute("select * from profile where contact ='%s' or contact_number='%s'"%(recievers,recievers))
        if check!=0:
            recievers=recievers.split(" ")
            print(recievers)
            if len(message) < 2:
                messagebox.showerror("Error", "Message body is empty")

            else:
                try:
                    for person in range(len(recievers)):
                        send_sms(message, recievers[person])
                    messagebox.showinfo("Message sent", "Message sent successfully")
                    destroy(splashscreen)
                except:
                    messagebox.showerror("Error!", "Unable to send messsages.")
        else:
            messagebox.showerror("Invalid number","Invalid or unregistered number.")

        #button.configure(state="disabled")
def send_sms_setup(any_root):
    splashscreen = Toplevel(any_root, relief=RAISED, bd=2, bg="#CCD6E5")
    splashscreen.title("New Message")
    splashscreen.grab_set()
    splashscreen.geometry("490x300+350+150")
    # Label(splashscreen, text="New Message"+"               ", font=('calibri', 16, 'bold'), fg="black",width=20).grid(row=0,column=0)
    Label(splashscreen, text="Recipient(s):", font=('calibri', 13, 'bold'), bg="#CCD6E5").grid(row=2, column=0,
                                                                                               padx=(10, 0),
                                                                                               pady=(10, 0))
    numbers = Entry(splashscreen, width=54)
    numbers.grid(row=2, column=1, padx=(10, 0), pady=(10, 0))

    Label(splashscreen, text="Message :", font=('calibri', 13, 'bold'), bg="#CCD6E5").grid(row=3, column=0,
                                                                                           padx=(10, 0), pady=(10, 0))
    message_entry = Text(splashscreen, width=40, height=10)
    message_entry.grid(row=3, column=1, columnspan=2, pady=(20, 0))

    send_button = Button(splashscreen, bd=1, relief=RIDGE, activebackground="#CCD6E5", text="Send", width=15,
                         height=1,command=lambda :send_message(splashscreen,numbers,message_entry))
    send_button.grid(row=4, column=1, pady=(15, 0))
def admin_back(any_root,username,sql):
    try:
        res = cursor.execute(sql)
        if res != 0:
            any_root.destroy()
            new_root_ad = Tk()
            new_root_ad.title(username)
            new_root_ad.geometry("1366x768+0+0")
            new_root_ad.resizable(False,False)
            frame1 = Frame(new_root_ad, height=60, width=1366, bg="black").place(x=0, y=0)
            Label(frame1, text="Institute portal", font=('calibri', 30,'bold'), fg="white", bg="black").place(x=688, y=30,anchor="center")

            date = Label(new_root_ad, font=('times', 20, 'bold'), fg="steel blue",text=today)
            date.place(x=400, y=100)


            day_lbl = Label(new_root_ad, font=('times', 20, 'bold'), fg="steel blue")
            day_lbl.place(x=600, y=100)
            day(day_lbl)
            clock = Label(new_root_ad, font=('times', 20, 'bold'), fg="steel blue")
            clock.place(x=750, y=100)
            tick(clock)

            icon_frame = Frame(new_root, height=600, width=1366)
            icon_frame.place(x=0, y=140)

            # ========================IMAGES=============================================================================
            img = ImageTk.PhotoImage(Image.open('C:/Users/priyanka/Desktop/Icons/updateattendance1.png'))
            up_att = Label(icon_frame, image=img)
            up_att.image = img

            att_img = ImageTk.PhotoImage(Image.open('C:/Users/priyanka/Desktop/Icons/checkattendance.png'))
            view_att = Label(icon_frame, image=att_img)
            view_att.image = att_img

            mail_img = ImageTk.PhotoImage(Image.open('C:/Users/priyanka/Desktop/Icons/sendmail1.png'))
            mail = Label(icon_frame, image=mail_img)
            mail.image = mail_img

            sms = ImageTk.PhotoImage(Image.open('C:/Users/priyanka/Desktop/Icons/sendsms1.png'))
            sms_att = Label(icon_frame, image=sms)
            sms_att.image = sms

            insert = ImageTk.PhotoImage(Image.open('C:/Users/priyanka/Desktop/Icons/register1.png'))
            insert_stu = Label(icon_frame, image=insert)
            insert_stu.image = insert

            logout_img = ImageTk.PhotoImage(Image.open('C:/Users/priyanka/Desktop/Icons/logout.png'))
            logout = Label(icon_frame, image=logout_img)
            logout.image = logout_img

            # =====================image buttons==========================================================
            update_btn = Button(icon_frame, image=img, relief=FLAT,bd=0,command=lambda:update_attendance(new_root_ad,username,sql))
            update_btn.place(x=350, y=90)
            update_lbl = Label(icon_frame, text="Update attendance", font=11).place(x=320, y=170)

            viewatt_btn = Button(icon_frame, image=att_img, relief=FLAT,bd=0,command=lambda:check_attendance(new_root_ad,username,sql))
            viewatt_btn.place(x=650, y=90)
            viewatt_lbl = Label(icon_frame, text="Check student attendance", font=11).place(x=610, y=170)

            send_mail_btn = Button(icon_frame, image=mail_img, relief=FLAT,bd=0,command=lambda :send_mail_setup(new_root_ad,username))
            send_mail_btn.place(x=950, y=90)
            send_mail_lbl = Label(icon_frame, text="Send mail", font=11).place(x=960, y=170)

            sms_btn = Button(icon_frame, image=sms, relief=FLAT,bd=0,command=lambda :send_sms_setup(new_root_ad))
            sms_btn.place(x=500, y=250)
            sms_lbl = Label(icon_frame, text="Send Message", font=11).place(x=485, y=340)

            insert_btn = Button(icon_frame, image=insert, relief=FLAT, bd=0,command=lambda :student_register(new_root_ad,username))
            insert_btn.place(x=800, y=270)
            insert_lbl = Label(icon_frame, text="Student Registration", font=11).place(x=775, y=340)

            logout_btn = Button(new_root_ad, image=logout_img, relief=FLAT,bd=0, command=lambda :destroy_window(new_root_ad))
            logout_btn.place(x=1290, y=90)




        else:
            messagebox.showerror("error","incorrect username or password")
    except:
        db.rollback()
        messagebox.showerror("Error!","Connection error")
def day(day_lbl):

    for d in range(0,len(list_days)):
        if value==d:
            day_str=list_days[d]
            day_lbl.config(text=day_str)
def tick(clock):
    global time1
    time2=time.strftime('%H:%M:%S')
    if time1!=time2:
        time1=time2
        clock.config(text=time2)
    clock.after(200,lambda :tick(clock))
def get_spinbox(res1,sb_list):
    '''add_new = cursor.execute("call add_col(%s)" % (today))
    db.commit()
    for i in range(0,len(res_len)):
        if sb_list[i].get()=="Mark!":
            messagebox.showerror("ERROR!", "Someone is left unmarked!")
        else:
            attendance=sb_list[i].get()
            cursor.execute("call attend (`%s`) (`%s`)"%(today,attendance))
            db.commit()'''
    attendance=[]
    for i in range(len(sb_list)):
            attendance.append(sb_list[i].get())
    for obj in sb_list:
            obj.config(state="normal")
            obj.delete(0,END )
            obj.insert(0,"Mark!")
            obj.config(state="readonly")
    j=0
    for i in range(len(attendance)):
        if attendance[i]=="Mark!":
            j+=1
    if j>0:
        messagebox.showerror("ERROR","Someone is left unmarked.")
    else:

        print(attendance)
        res=cursor.execute(
            "select * from INFORMATION_SCHEMA.COLUMNS where table_schema=database() and table_name='record_%d'AND COLUMN_NAME = '%s' "%(year,month_name))

        if res==0:
            cursor.execute("alter table  record_%d add %s varchar(300) after %s"%(year,month_name,month_list[-1]))
            db.commit()
            cursor.execute("update record_%d set %s=''"%(year,month_name))
            db.commit()
        res = cursor.execute(
            "select * from INFORMATION_SCHEMA.COLUMNS where table_schema=database() and table_name='record_%d'AND COLUMN_NAME = '%s' " % (
            year, month_name))
        if res==1:
            cursor.execute("select %s from record_%d"%(month_name,year))
            column_tuple=cursor.fetchall()
            print(column_tuple,len(column_tuple))
            '''column_list=[list(i) for i in column_tuple]
            print(column_list)'''
            w=datetime.date.today()
            w=w.day
            cursor.execute("select student_id from record_%d"%year)
            id=cursor.fetchall()
            print(id[0])
            print(len(attendance))
            length=len(column_tuple)
            for i in range (0,length):
                j=''.join(id[i])
                cursor.execute("UPDATE record_%d SET %s = CONCAT(%s, ' %d %s,') where student_id='%s'"%(year,month_name,month_name,w ,attendance[i],j))
                db.commit()
            messagebox.showinfo("Success!","Attendance Updated Successfully")
def update_attendance(new_root_ad,username,sql):

    new_root_ad.destroy()
    upd_att=Tk()
    upd_att.geometry("1366x768+0+0")
    upd_att.resizable(False,False)
    frame1 = Frame(upd_att, height=60, width=1366, bg="black").place(x=0, y=0)
    Label(frame1, text="Institute Portal", font=('calibri', 30,'bold'), fg="white", bg="black").place(x=680, y=30,anchor="center")
    back_img = ImageTk.PhotoImage(Image.open('C:/Users/priyanka/Desktop/Icons/back.png'))
    backlbl = Label(upd_att, image=back_img)
    back.image = back_img

    back_btn =Button(upd_att, text="BACK", relief=FLAT, image=back_img, bd=0,
                         command=lambda: admin_back(upd_att,username,sql))
    back_btn.place(x=20, y=65)

    day_lbl = Label(upd_att, font=('times', 14, 'bold'), fg="steel blue")
    day_lbl.grid(column=1, row=2, padx=(420, 0), pady=75)
    day(day_lbl)
    clock = Label(upd_att, font=('times', 14, 'bold'), fg="steel blue")
    clock.grid(row=2, column=1, padx=(700, 0), pady=75)
    tick(clock)

    '''logout_img = ImageTk.PhotoImage(Image.open('C:/Users/priyanka/Desktop/Icons/logout.png'))
    logout = Label(upd_att, image=logout_img)
    logout.image = logout_img

    logout_btn = Button(upd_att, image=logout_img, relief=FLAT, bd=0, command=quit,height=35)
    logout_btn.place(x=1290, y=62)'''

    attendance_frame = LabelFrame(upd_att, text="Update Attendance", relief=RAISED, font=('calibri', 16, 'bold'), bd=4,
                                  height=630, width=1345)
    attendance_frame.place(x=10, y=105)

    attendance_frame.grid_propagate(False)

    Label(attendance_frame, font=('calibri', 14, 'bold'), text="S.No.").grid(column=1,row=0,padx=(35,0),pady=(10,10))
    cursor.execute(
        "select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where table_schema=database() and table_name='record_%d' "%year)
    res0 = cursor.fetchall()
    print(res0)
    cursor.execute("select first_name from record_%d"%year)
    res = cursor.fetchall()
    print(res)

    cursor.execute("select student_ID from record_%d"%year)
    res1 = cursor.fetchall()
    print(res1)

    cursor.execute("select last_name from record_%d"%year)
    res2 = cursor.fetchall()
    print(res2)
    attendance_frame.propagate(0)

    for column in range(1, 4):
        field = "".join(res0[column])
        b = Label(attendance_frame, font=('calibri', 14, 'bold'), text=field.title())
        b.grid(column=column+1, row=0,padx=(105,5),pady=(10,10))

    b = Label(attendance_frame, font=('calibri', 14, 'bold'), fg="steel blue", text=today)
    b.grid(column=5,row=0,padx=(140,0),pady=(10,10))
    print(value)

    b = Label(attendance_frame, font=('calibri', 14, 'bold'), fg="steel blue", text="Status")
    b.grid(column=6, row=0, padx=(115, 50), pady=(10, 10))



    n = 80

    sb_list = []

    def data():
        k = 1
        i = 40
        list_of_variables=[]
        for r in range(0, len(res)):
            field = "".join(res[r])
            field2 = "".join(res2[r])
            field1 = "".join(res1[r])
            Label(frame, text="%d." % k, font=14, bg="white").grid(column=2, row=i, padx=(25, 15), pady=15,sticky="NW")
            Label(frame, text=field.title(), font=14, bg="white").grid(column=17, row=i, padx=(130, 0), pady=15,sticky="NW")
            Label(frame, text=field2.capitalize(), font=14, bg="white").grid(column=37, row=i, padx=(130, 0), pady=15,sticky="NW")
            ID=Label(frame, text=field1.capitalize(), font=14, bg="white")
            ID.grid(column=55, row=i, padx=(130, 0), pady=15,sticky="NW")

            s = Spinbox(frame, values=('P', 'A'), width=20, relief=RIDGE, bd=3)

            sb_list.append(s)
            s.delete(0, "end")
            s.insert(0, "Mark!")
            s.config(state="readonly")
            s.grid(column=70, row=i, padx=(155,20), pady=15,sticky="NW")
            cursor.execute("select status from record_%d where student_id='%s' " % (year, ID.cget("text")))
            status = cursor.fetchone()
            status = ''.join(status)
            print(status)
            status.strip("{")
            status.strip("}")
            Label(frame, text=status, font=13, bg="white").grid(column=80, row=i, padx=(80, 0), pady=15, sticky="NW")

            i += 10
            k += 1


    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    btn = Button(attendance_frame, width=15, text="Submit", command=lambda: get_spinbox(res1, sb_list))
    btn.place(x=50, y=550)

    attendance_frame2 = Frame(attendance_frame, bd=4, height=450, width=1330).place(x=0, y=80)
    sizex = 1366
    sizey = 768
    posx = 0
    posy = 0
    upd_att.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

    myframe = Frame(attendance_frame2, relief=GROOVE, width=1320, height=450, bd=0)
    myframe.place(x=20, y=200)
    myframe.propagate(FALSE)
    canvas = Canvas(myframe, width=1300, height=460,bg="white")
    canvas.place(x=10, y=-10)
    canvas.propagate(FALSE)
    frame = Frame(canvas, width=1466, height=450, bg="white")
    frame.place(x=0, y=20)

    frame.propagate(FALSE)

    myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right", fill="y")
    # canvas.pack(side="left")
    canvas.create_window((50, 150), window=frame)  # (0,0)=x,y
    frame.bind("<Configure>", myfunction)

    data()
    '''for row in range(0,len(res)):
        Label(attendance_frame,)'''
def prompt(root,ask_frame):
    global  user, password
    ask_frame.destroy()

    win=Frame(root, height=400, width=400, bg="white", padx=4, pady=4)
    win.place(x=420, y=400, anchor='center')
    Label(win, text="ADMINISTRATOR", font=('calibri', 20, 'bold'), fg="steel blue",bg="white").place(x=110, y=10)
    Label(win, text="Please log-in to get access", font=('calibri', 15), fg="steel blue",bg="white").place(x=90, y=50)
    '''back_img = ImageTk.PhotoImage(Image.open('C:/Users/priyanka/Desktop/Icons/back.png'))
    backlbl = Label(win, image=back_img)
    back.image = back_img'''

    LabelFrame(win, text="Log-In", bd=3, height=250, width=300,bg="white").place(x=50, y=100)
    Label(win, text="Username:", font=('Arial', 11),bg="white").place(x=80, y=130)
    user = Entry(win, font=('Arial', 11), bd=3, width=30,bg="#F0F0F0")
    user.place(x=80, y=170)
    Label(win, text="Password:", font=('Arial', 11),bg="white").place(x=80, y=210)
    password = Entry(win, show="*", font=('Arial', 11), bd=3, width=30,bg="#F0F0F0")
    password.place(x=80, y=250)

    log_button = Button(win, text="Log in", bg="grey", bd=5, width=15,command=lambda :admin_login(root))
    log_button.place(x=140, y=290)
    back_btn = Button(win, relief=FLAT, text="Go to main window", bd=0,
                      command=lambda: destroy_window(root),font=('calibri', 12), fg="steel blue",bg="white",activebackground="white")
    back_btn.place(x=120, y=360)
def prompt1(root,ask_frame):
    global  user, password, s1, s2, s3, s4, s5, log_button, register_button, forgot_button
    ask_frame.destroy()
    win1=Frame(root,height=420,width=420,bg="white",padx=4,pady=4)
    win1.place(x=420,y=400,anchor='center')
    s1 = Label(win1, text="STUDENT PANEL", font=('calibri', 20, 'bold'), fg="steel blue",bg="white")
    s1.place(x=110, y=10)
    s2 = Label(win1, text="Please log-in to get access", font=('calibri', 15), fg="steel blue",bg="white")
    s2.place(x=90, y=50)

    s4 = LabelFrame(win1, text="Log-In", bd=3, height=250, width=300,bg="white")
    s4.place(x=55, y=100)
    s3 = Label(win1, text="Student ID:", font=('Arial', 11),bg="white")
    s3.place(x=80, y=130)
    user = Entry(win1, font=('Arial', 11), bd=3, width=30,bg="#F0F0F0")
    user.place(x=80, y=170)
    s5 = Label(win1, text="Password:", font=('Arial', 11),bg="white")
    s5.place(x=80, y=210)
    password = Entry(win1, show="*", font=('Arial', 11), bd=3, width=30,bg="#F0F0F0")
    password.place(x=80, y=250)

    log_button = Button(win1, text="Log in", bg="grey", command=lambda :student_login(root), bd=5, width=15)
    log_button.place(x=140, y=290)

    forgot_button = Button(win1, text="Forgot Password?", activeforeground="steel blue",bg="white", relief=FLAT,bd=0,command=lambda:student_forgot(user), width=15)
    forgot_button.place(x=55, y=350)

    back_btn = Button(win1, relief=FLAT, text="Go to main window", bd=0,
                      command=lambda: destroy_window(root), font=('calibri', 12), fg="steel blue", bg="white",activebackground="white")
    back_btn.place(x=130, y=380)
def destroy_window(any_root):
    any_root.destroy()
    main_window()
def main_window():
    root=Tk()
    root.geometry("800x700")
    root.resizable(False,False)
    root.title("Attendance Tracker")
    root.config(background="#EBEBEC")
    label_frame=Frame(root,height=70,width=800,bg="black").place(x=0,y=0)
    root1=Label(label_frame,text="Institute's Portal",font=('calibri',22,'bold'),fg="white",bg="black")
    root1.place(x=400,y=30,anchor='center')
    #b=tk.Button(root,text="create",command=a)
    ask_frame=Frame(root,height=350,width=400,bg="white",padx=4,pady=4)
    ask_frame.place(x=420,y=400,anchor='center')
    root2=Label(ask_frame,text="You are?",bg="white",fg="steel blue",font=('calibri',15,'bold'))
    root2.place(x=200,y=40,anchor='center')
    adm_button=Button(ask_frame,text="I'm Admin!",font=('Calibri',11,'bold'),width=25,bd=3,relief=RIDGE,command=lambda:prompt(root,ask_frame))
    adm_button.place(x=200,y=120,anchor='center')
    stu_button=Button(ask_frame,text="I'm Student!",font=('Calibri',11,'bold'),width=25,bd=3,relief=RIDGE,command=lambda :prompt1(root,ask_frame))
    stu_button.place(x=200,y=220,anchor='center')
    root.mainloop()
main_window()
