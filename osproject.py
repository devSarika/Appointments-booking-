from tkinter import *
from tkinter import messagebox
import sqlite3




def click1():

	window2=Toplevel()
	window2.title("Appointments")
	window2.configure(background="black")
	#window2.attributes("-fullscreen", True)
	picture=PhotoImage(file=r"C:\Users\DEVISETTY SAI SARIKA\Pictures\book.gif",width=700,height=700)
	l3=Label(window2,image=picture,bg="black")
	l3.image=picture
	l3.place(x=580,y=200)
	b4=Button(window2,text="SIGN UP",font="none 14 bold",command=signup)
	b4.place(x=650,y=400)
	b5=Button(window2,text="LOGIN",font="none 14 bold",command=login)
	b5.place(x=800,y=400)

	window2.mainloop()

def click2():
	window8=Toplevel()
	window8.title("Health-Tips")
	window8.configure(background="black")
	showtextbox=Text(window8,width=500,height=500,bg="black",fg="white",font="none 14 bold")
	showtextbox.grid(row=5,column=0,padx=(10,0),pady=(10,0))
	scroll=Scrollbar(window8,orient="vertical",command=showtextbox.yview)
	scroll.grid(row=7,column=0,columnspan=3,padx=(20,0),pady=(10,0))
	showtextbox.configure(yscrollcommand=scroll.set)
	obj=open(r"C:\Users\DEVISETTY SAI SARIKA\Desktop\health tips.txt","r")
	lines=obj.readlines()
	no=len(lines)
	for i in range(no):
		showtextbox.insert(INSERT,lines[i])

	
	obj.close()
	window8.mainloop()


def login():
	
	username=StringVar()
	password=StringVar()
	variable=StringVar()
	var1=StringVar()

		



	def database2():
	
		while True:
			user=username.get()
			pwd2=password.get()
			if(user =='Admin' and pwd2== 'admin'):
				conn=sqlite3.connect('newsign.db')
				with conn:
					cursor=conn.cursor()
					#cursor.execute("UPDATE newdetails SET Specialist=?,Issue=? WHERE Name=? and Password=?",(drop,prob,user,pwd2))
				cursor.execute("SELECT * FROM form ORDER BY Issue ASC")

				conn.commit()
				break

			with sqlite3.connect("newsign.db") as db:
				cursor=db.cursor()

			find_user=("SELECT * FROM form WHERE Name=? AND Password=?")
			cursor.execute(find_user,[(user),(pwd2)])
			results=cursor.fetchall()

			if results:

				#cursor.execute("UPDATE newdetails SET Specialist=?,Issue=? WHERE Name=? and Password=?",(drop,prob,name1,pwd))
				def database4():
					drop=variable.get()
					prob=var1.get()
					user=username.get()
					pwd2=password.get()

					


				
					conn=sqlite3.connect('newsign.db')
					with conn:
						cursor=conn.cursor()
			#cursor.execute('CREATE TABLE IF NOT EXISTS ndetails(Name TEXT,LastName TEXT,Age TEXT,Gender TEXT,Email TEXT,Password TEXT,Specialist TEXT,Issue Text)')
			#cursor.execute('INSERT INTO ndetails(Specialist,Issue) VALUES (?,?)',(drop,prob) )
			#cursor.execute('UPDATE ndetails SET (Specialist=drop , Issue=prob) FROM ndetails WHERE Name=name1 and Password=pwd')
					cursor.execute("UPDATE form SET Specialist=?,Issue=? WHERE Name=? and Password=?",(drop,prob,user,pwd2))
					conn.commit()

				variable=StringVar()
				var1=IntVar()

				window6=Toplevel()
				window6.title("Apponiment login")
				window6.configure(background="black")

				l10=Label(window6,text="Specialist:",font="none 16 bold",bg="black",fg="white")
				l10.place(x=500,y=200)

				options=["DENTIST","GYNACOLOGIST","NEUROLOGIST","CARDIOLOGIST","DERMATOLOGIST","ENT","PSYCIATRIST","PEDITRICIAN","GENERAL PHYSICIAN"]
				variable.set(options[8])
				w=OptionMenu(window6,variable,*options)
				w.place(x=640,y=200)

				l10=Label(window6,text="Task :",font="none 16 bold",bg="black",fg="white")
				l10.place(x=500,y=256)

				R4 = Radiobutton(window6, text="Surgery",bg="black",fg="white",variable=var1,value=1,borderwidth=4)
				R4.place(x=600,y=256)
				R5 = Radiobutton(window6, text="Checkup",bg="black",fg="white",variable=var1,value=2,borderwidth=4)
				R5.place(x=700,y=256)
				R6 = Radiobutton(window6, text="Consultancy",bg="black",fg="white",variable=var1,value=3,borderwidth=4)
				R6.place(x=800,y=256)

				l10=Label(window6,text="Problem Description :",font="none 16 bold",bg="black",fg="white")
				l10.place(x=500,y=306)
				name2=Entry(window6,width=70,bg="white")
				name2.place(x=740,y=310)

				b6=Button(window6,text="SUBMIT",font="none 12 bold",command=database4)
				b6.place(x=520,y=356)





				window6.mainloop()
				
			else:
				messagebox.showinfo('Information','User Name & Password Not matched ')
				break

	window4=Toplevel()
	window4.title("LOGIN")
	window4.configure(background="black")
	#window4.attributes("-fullscreen", True)

	l11=Label(window4,text="User Name :",font="none 16 bold",bg="black",fg="white")
	l11.place(x=500,y=200)
	name6=Entry(window4,width=30,bg="white",textvar=username)
	name6.place(x=630,y=206)

	l12=Label(window4,text="Password :",font="none 16 bold",bg="black",fg="white")
	l12.place(x=500,y=250)
	name7=Entry(window4,width=30,bg="white",textvar=password,show="*")
	name7.place(x=630,y=256)

	



	b7=Button(window4,text="SUBMIT",font="none 12 bold",command=database2)
	b7.place(x=540,y=300)


	

	window4.mainloop()




def signup():
	Name=StringVar()
	LastName=StringVar()
	var=StringVar()
	Age=IntVar()
	EmailID=StringVar()
	Password=StringVar()
	conn=sqlite3.connect('newsign.db')
	with conn:
		cursor=conn.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS form(Name TEXT,LastName TEXT,Age TEXT,Gender TEXT,Email TEXT,Password TEXT,Specialist TEXT,Issue Text)')
	conn.commit()
	def appointment():

	



		def database3():
			name1=Name.get()
			name2=LastName.get()
			age=Age.get()
			gender=var.get()
			mail=EmailID.get()
			pwd=Password.get()
			drop=variable.get()
			prob=var1.get()

			conn=sqlite3.connect('newsign.db')
			with conn:
				cursor=conn.cursor()
			#cursor.execute('CREATE TABLE IF NOT EXISTS ndetails(Name TEXT,LastName TEXT,Age TEXT,Gender TEXT,Email TEXT,Password TEXT,Specialist TEXT,Issue Text)')
			#cursor.execute('INSERT INTO ndetails(Specialist,Issue) VALUES (?,?)',(drop,prob) )
			#cursor.execute('UPDATE ndetails SET (Specialist=drop , Issue=prob) FROM ndetails WHERE Name=name1 and Password=pwd')
			cursor.execute("UPDATE form SET Specialist=?,Issue=? WHERE Name=? and Password=?",(drop,prob,name1,pwd))
			conn.commit()

		variable=StringVar()
		var1=IntVar()

		window5=Toplevel()
		window5.title("Apponiment")
		window5.configure(background="black")

		l10=Label(window5,text="Specialist:",font="none 16 bold",bg="black",fg="white")
		l10.place(x=500,y=200)

		options=["DENTIST","GYNACOLOGIST","NEUROLOGIST","CARDIOLOGIST","DERMATOLOGIST","ENT","PSYCIATRIST","PEDITRICIAN","GENERAL PHYSICIAN"]
		variable.set(options[8])
		w=OptionMenu(window5,variable,*options)
		w.place(x=640,y=200)

		l10=Label(window5,text="Task :",font="none 16 bold",bg="black",fg="white")
		l10.place(x=500,y=256)

		R4 = Radiobutton(window5, text="Surgery",bg="black",fg="white",variable=var1,value=1,borderwidth=4)
		R4.place(x=600,y=256)
		R5 = Radiobutton(window5, text="Checkup",bg="black",fg="white",variable=var1,value=2,borderwidth=4)
		R5.place(x=700,y=256)
		R6 = Radiobutton(window5, text="Consultancy",bg="black",fg="white",variable=var1,value=3,borderwidth=4)
		R6.place(x=800,y=256)

		l10=Label(window5,text="Problem Description :",font="none 16 bold",bg="black",fg="white")
		l10.place(x=500,y=306)
		name2=Entry(window5,width=70,bg="white")
		name2.place(x=740,y=310)

		b6=Button(window5,text="SUBMIT",font="none 12 bold",command=database3)
		b6.place(x=520,y=356)





		window5.mainloop()

	def database():
		name1=Name.get()
		name2=LastName.get()
		age=Age.get()
		gender=var.get()
		mail=EmailID.get()
		pwd=Password.get()
		
		conn=sqlite3.connect('newsign.db')
		with conn:
			cursor=conn.cursor()
		#cursor.execute('CREATE TABLE IF NOT EXISTS ndetails(Name TEXT,LastName TEXT,Age TEXT,Gender TEXT,Email TEXT,Password TEXT,Specialist TEXT,Issue Text)')
		cursor.execute('INSERT INTO form(Name,LastName,Age,Gender,Email,Password) VALUES (?,?,?,?,?,?)',(name1,name2,age,gender,mail,pwd) )
		conn.commit()
		#messagebox.showinfo('Information','Submitted Successfully click on the Appointment  ')

	var=StringVar()
	var1=StringVar()
	variable=StringVar()
	window3=Toplevel()
	window3.title("SIGN-UP")
	window3.configure(background="black")
	#window3.attributes("-fullscreen", True)
	l5=Label(window3,text="Please fill your Details ",bg="black",fg="white",font="none 40 bold")
	l5.place(x=400,y=50)
	l4=Label(window3,text="Name :",font="none 16 bold",bg="black",fg="white")
	l4.place(x=500,y=200)
	name1=Entry(window3,width=30,bg="white",textvar=Name)
	name1.place(x=580,y=206)

	l6=Label(window3,text="Last Name:",font="none 16 bold",bg="black",fg="white")
	l6.place(x=500,y=250)
	name2=Entry(window3,width=30,bg="white",textvar=LastName)
	name2.place(x=630,y=256)

	l7=Label(window3,text="Age:",font="none 16 bold",bg="black",fg="white")
	l7.place(x=500,y=300)
	name3=Entry(window3,width=30,bg="white",textvar=Age)
	name3.place(x=560,y=306)

	l7=Label(window3,text="Sex:",font="none 16 bold",bg="black",fg="white")
	l7.place(x=500,y=350)
	R1 = Radiobutton(window3, text="F",bg="black",fg="white",variable=var,value="Female",borderwidth=4)
	R1.place(x=560,y=356)
	R2 = Radiobutton(window3, text="M",bg="black",fg="white",variable=var,value="Male",borderwidth=4)
	R2.place(x=600,y=356)
	R3 = Radiobutton(window3, text="O",bg="black",fg="white",variable=var,value="Others",borderwidth=4)
	R3.place(x=650,y=356)

	l8=Label(window3,text="Email ID:",font="none 16 bold",bg="black",fg="white")
	l8.place(x=500,y=400)
	name4=Entry(window3,width=30,bg="white",textvar=EmailID)
	name4.place(x=600,y=406)

	l9=Label(window3,text="Password:",font="none 16 bold",bg="black",fg="white")
	l9.place(x=500,y=450)
	name5=Entry(window3,show='*',width=30,bg="white",textvar=Password)
	name5.place(x=620,y=456)

	name1=Name.get()
	name2=LastName.get()
	age=Age.get()
	gender=var.get()
	mail=EmailID.get()
	pwd=Password.get()
		

	





	b6=Button(window3,text="SUBMIT",font="none 12 bold",command=database)
	b6.place(x=520,y=500)


	b7=Button(window3,text="APPOINTMENT",font="none 12 bold",command=appointment)
	b7.place(x=620,y=500)

	window3.mainloop()


window=Tk()
window.title("Seva Online services")
window.configure(background="black")
#window.attributes("-fullscreen", True)
#window.geometry("%dx%d+0+0" % (1400, 1050))
l2=Label(window,text="Welcome to Seva Online services ",bg="black",fg="white",font="none 40 bold")
l2.place(x=400,y=1)
pic=PhotoImage(file=r"C:\Users\DEVISETTY SAI SARIKA\Pictures\healthcare.jpg",width=500,height=500)
l1=Label(window,image=pic,bg="black")
l1.image=pic
l1.place(x=500,y=60)
b1 = Button(window, text = "Health Tips",font="none 14 bold",command=click2)
b2 = Button(window, text = "Reports",font="none 14 bold",command=click1)
b3 = Button(window, text = "Appointments",font="none 14 bold",command=click1)
b1.place(x=550,y=600)
b2.place(x=750 ,y=600)
b3.place(x=900,y=600)
window.mainloop( )