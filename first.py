import MySQLdb
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

db=MySQLdb.connect(host='localhost',user='root',passwd='sandesh123',db='blah')
cur=db.cursor()
username=str()
address=str()
userid=str()
tot=0

#Design of starting screen.
class StartScreen(FloatLayout):
        def __init__(self, **kwargs):
                super(StartScreen, self).__init__(**kwargs)
		#But`ton 1
                self.cols = 1
		self.but1=Button(text="I'm a user",size_hint=(None,None),width=300,height=50,font_size=20,pos=(250,300))
		self.but1.bind(on_press=self.user)
		self.add_widget(self.but1)

		#Button 2
		self.but2=Button(text="I'm an admin",size_hint=(None,None),width=300,height=50,font_size=20,pos=(250,355))
		self.but2.bind(on_press=self.admin)
		self.add_widget(self.but2)

	def user(self,a):
		App.get_running_app().stop()
		UserLogin().run()
		#Open new app for user login page.


	def admin(self,a):
		App.get_running_app().stop()
		#Open new app for admin login
		AdminLogin().run()

                

class MyApp(App):

    def build(self):
        return StartScreen()
#END start screen

#Design of adminlogin screen.
class AdminLoginScreen(FloatLayout):
        def __init__(self, **kwargs):
                super(AdminLoginScreen, self).__init__(**kwargs)
                self.cols = 2
                self.but=Button(text="Login",font_size=14,pos=(250,200),size_hint=(None,None),width=100,height=30)
		self.but.bind(on_press=self.adminlogin)
                self.add_widget(Label(text='Password:',pos=(200,240),size_hint=(None,None)))
                self.password = TextInput(password=True, multiline=False,size_hint=(None,None),width=300,height=35,pos=(300,270),focus=True)
                self.add_widget(self.password)
                self.add_widget(self.but)
		self.bck=Button(text="Back",font_size=14,pos=(350,200),size_hint=(None,None),width=100,height=30)
		self.bck.bind(on_press=self.goback)
		self.add_widget(self.bck)
	
	def adminlogin(self,a):
		#Run query to check for password. 
		query="select * from admin where password='"+str(self.password.text)+"';"

		result=''
                try:
			cur.execute(query)
			result=cur.fetchall()
		except:
			 self.add_widget(Label(text='Please enter correct password',pos=(400,130),size_hint=(None,None)))
		if len(result)<1:	 
			self.add_widget(Label(text='Please enter correct password',pos=(400,130),size_hint=(None,None)))
		else:
			#Store the user info to display in next window in global variables.
			

			#Close this app and open next app.
			App.get_running_app().stop()
			AdminApp().run()

	def goback(self,a):
		App.get_running_app().stop()
		MyApp().run()


class AdminLogin(App):

    def build(self):
        return AdminLoginScreen()
#END adminlogin

#Design of admin screen.
class AdminScreen(FloatLayout):
        def __init__(self, **kwargs):
                super(AdminScreen, self).__init__(**kwargs)
                self.cols = 2
		self.add_widget(Label(text='Admin',font_size=20,pos=(600,500),size_hint=(None,None)))
             	self.adduserButton=Button(text='Add User',font_size=14,pos=(350,500),size_hint=(None,None),height=30,width=200)
		self.adduserButton.bind(on_press=self.adduser)
		self.add_widget(self.adduserButton)
		
		self.addserviceButton=Button(text='Add Service',font_size=14,pos=(350,450),size_hint=(None,None),height=30,width=200)
		self.addserviceButton.bind(on_press=self.addservice)
		self.add_widget(self.addserviceButton)

		self.deleteuserButton=Button(text='Delete User',font_size=14,pos=(350,400),size_hint=(None,None),height=30,width=200)
		self.deleteuserButton.bind(on_press=self.deleteuser)
		self.add_widget(self.deleteuserButton)

		self.deleteserviceButton=Button(text='Delete Service',font_size=14,pos=(350,350),size_hint=(None,None),height=30,width=200)
		self.deleteserviceButton.bind(on_press=self.deleteservice)
		self.add_widget(self.deleteserviceButton)

		self.addbillButton=Button(text='Add Bill',font_size=14,pos=(350,300),size_hint=(None,None),height=30,width=200)
		self.addbillButton.bind(on_press=self.addbill)
		self.add_widget(self.addbillButton)

		self.billButton=Button(text='Get Unpaid bills',font_size=14,pos=(350,250),size_hint=(None,None),height=30,width=200)
		self.billButton.bind(on_press=self.getdue)
		self.add_widget(self.billButton)

		self.bck=Button(text="Logout",font_size=14,pos=(350,100),size_hint=(None,None),width=100,height=30)
		self.bck.bind(on_press=self.goback)
		self.add_widget(self.bck)

	def adduser(self,a):
		App.get_running_app().stop()
		AddUser().run()

	def deleteuser(self,a):
		App.get_running_app().stop()
		DeleteUser().run()

	def addservice(self,a):
		App.get_running_app().stop()
		AddServiceApp().run()
	
	def deleteservice(self,a):
		App.get_running_app().stop()
		DeleteServiceApp().run()
	
	def addbill(felf,a):
		App.get_running_app().stop()
		AddBillApp().run()

	def getdue(self,a):
		App.get_running_app().stop()
		BillApp().run()
		#Fetch and display unpaid bills.

	def goback(self,a):
		App.get_running_app().stop()
		AdminLogin().run()


class AdminApp(App):

    def build(self):
        return AdminScreen()
#END adminScreen

#Design of get due bills screen.
class BillScreen(FloatLayout):
        def __init__(self, **kwargs):
                super(BillScreen, self).__init__(**kwargs)
                self.cols = 2
               
		self.bck=Button(text="Back",font_size=14,pos=(600,500),size_hint=(None,None),width=100,height=30)
		self.add_widget(self.bck)
		self.bck.bind(on_press=self.goback)
	
		query='select u.user_id,u.name,b.bill_no,b.amt,u.ph_no,u.email from users u,bill b,enrollment e where u.user_id=b.user_id and b.status="unpaid";'
		try:
			cur.execute(query)
			result=cur.fetchall()
			st='User ID               Name               Bill No.            Amount             Phone               Email\n\n\n'
			for row in result:
				st+=str(row[0])+'             '+str(row[1])+'             '+str(row[2])+'          '+str(row[3])+'             '+str(row[4])+'              '+str(row[5])
				st+='\n\n'
			self.add_widget(Label(text=st,color=[255,255,255,8]))

		except:print ''
	
	def goback(self,a):
		App.get_running_app().stop()
		AdminApp().run()


class BillApp(App):

    def build(self):
        return BillScreen()
#END Deleteservice



#Design of AddBill screen.
class AddBillScreen(FloatLayout):
        def __init__(self, **kwargs):
                super(AddBillScreen, self).__init__(**kwargs)
                self.cols = 2
               

		self.userid = TextInput(multiline=False,size_hint=(None,None),width=200,height=30,pos=(300,400),focus=True,text="User ID")
                self.add_widget(self.userid)

		self.serid = TextInput(multiline=False,size_hint=(None,None),width=200,height=30,pos=(300,350),focus=True,text="Service ID")
                self.add_widget(self.serid)

		self.amt = TextInput(multiline=False,size_hint=(None,None),width=200,height=30,pos=(300,300),focus=True,text="Meter Reading")
                self.add_widget(self.amt)
		
		self.bck=Button(text="Back",font_size=14,pos=(600,500),size_hint=(None,None),width=100,height=30)
		self.bck.bind(on_press=self.goback)
		
		self.submit=Button(text="Submit",font_size=14,pos=(320,250),size_hint=(None,None),width=100,height=30)
		self.submit.bind(on_press=self.submitt)
		self.add_widget(self.submit)
		self.add_widget(self.bck)
	
	def submitt(self,a):
		query='select reading from enrollment where user_id='+str(self.userid.text)+' and service_id='+str(self.serid.text)+';'
		lb1=Label(text="",size_hint=(None,None),pos=(320,170))
		self.add_widget(lb1)
		try:
			cur.execute(query)
			res=cur.fetchall()
			res=res[0][0]
			amount=int(self.amt.text)-res
			if amount<0:j=1/0

			query='select cost from service where service_id='+str(self.serid.text)+';'
			cur.execute(query)
			q=cur.fetchall()
			amount=amount*float(q[0][0])
			query='select max(bill_no) from bill;'
			cur.execute(query)
			res=cur.fetchall()
			b_no=res[0][0]+1
			
			query='insert into bill values('+str(b_no)+','+str(self.userid.text)+','+str(amount)+',0000-00-00,"unpaid");'
			cur.execute(query)
			query='update enrollment set reading='+str(self.amt.text)+' where user_id='+str(self.userid.text)+' and service_id='+str(self.serid.text)+';'
	
			cur.execute(query)
			db.commit()
			lb1.text='Success'
			self.userid.text='User ID'
			self.serid.text='Servie Id'
			self.amt.text="Meter Reading"

		except:
			lb1.text='Please input valid values.'

	def goback(self,a):
		App.get_running_app().stop()
		AdminApp().run()


class AddBillApp(App):

    def build(self):
        return AddBillScreen()
#END Addservice


#Design of DeleteSerivice screen.
class DeleteServiceScreen(FloatLayout):
        def __init__(self, **kwargs):
                super(DeleteServiceScreen, self).__init__(**kwargs)
                self.cols = 2
               

		self.userid = TextInput(multiline=False,size_hint=(None,None),width=200,height=30,pos=(300,400),focus=True,text="User ID")
                self.add_widget(self.userid)

		self.serid = TextInput(multiline=False,size_hint=(None,None),width=200,height=30,pos=(300,350),focus=True,text="Service ID")
                self.add_widget(self.serid)


		self.bck=Button(text="Back",font_size=14,pos=(600,500),size_hint=(None,None),width=100,height=30)
		self.bck.bind(on_press=self.goback)
		
		self.submit=Button(text="Delete",font_size=14,pos=(320,300),size_hint=(None,None),width=100,height=30)
		self.submit.bind(on_press=self.submitt)
		self.add_widget(self.submit)
		self.add_widget(self.bck)
	
	def submitt(self,a):
		query='delete from enrollment where user_id='+str(self.userid.text)+' and service_id='+str(self.serid.text)+';'
		print query
		try:
			cur.execute(query)
			db.commit()
			self.add_widget(Label(text="Success",size_hint=(None,None),pos=(320,250)))
			self.userid.text='User ID'
			self.serid.text='Servie Id'
		except:
			self.add_widget(Label(text="Please enter Correct User ID and service ID.",size_hint=(None,None),pos=(320,250)))

	def goback(self,a):
		App.get_running_app().stop()
		AdminApp().run()


class DeleteServiceApp(App):

    def build(self):
        return DeleteServiceScreen()
#END Deleteservice


#Design of AddSerivice screen.
class AddServiceScreen(FloatLayout):
        def __init__(self, **kwargs):
                super(AddServiceScreen, self).__init__(**kwargs)
                self.cols = 2
               

		self.userid = TextInput(multiline=False,size_hint=(None,None),width=200,height=30,pos=(300,400),focus=True,text="User ID")
                self.add_widget(self.userid)

		self.serid = TextInput(multiline=False,size_hint=(None,None),width=200,height=30,pos=(300,350),focus=True,text="Service ID")
                self.add_widget(self.serid)


		self.bck=Button(text="Back",font_size=14,pos=(600,500),size_hint=(None,None),width=100,height=30)
		self.bck.bind(on_press=self.goback)
		
		self.submit=Button(text="ADD",font_size=14,pos=(320,300),size_hint=(None,None),width=100,height=30)
		self.submit.bind(on_press=self.submitt)
		self.add_widget(self.submit)
		self.add_widget(self.bck)
	
	def submitt(self,a):
		query='insert into enrollment values('+str(self.userid.text)+','+str(self.serid.text)+',0);'
		print query
		try:
			cur.execute(query)
			db.commit()
			self.add_widget(Label(text="Success",size_hint=(None,None),pos=(320,250)))
			self.userid.text='User ID'
			self.serid.text='Servie Id'
		except:
			self.add_widget(Label(text="Please enter Correct User ID and service ID.",size_hint=(None,None),pos=(320,250)))

	def goback(self,a):
		App.get_running_app().stop()
		AdminApp().run()


class AddServiceApp(App):

    def build(self):
        return AddServiceScreen()
#END Addservice


#Design of DeleteUser screen.
class DeleteUserScreen(FloatLayout):
        def __init__(self, **kwargs):
                super(DeleteUserScreen, self).__init__(**kwargs)
                self.cols = 2
               

		self.userid = TextInput(multiline=False,size_hint=(None,None),width=200,height=30,pos=(300,400),focus=True,text="User ID")
                self.add_widget(self.userid)

		self.bck=Button(text="Back",font_size=14,pos=(600,500),size_hint=(None,None),width=100,height=30)
		self.bck.bind(on_press=self.goback)
		
		self.submit=Button(text="Delete User",font_size=14,pos=(320,350),size_hint=(None,None),width=100,height=30)
		self.submit.bind(on_press=self.submitt)
		self.add_widget(self.submit)
		self.add_widget(self.bck)
	
	def submitt(self,a):
		query='delete from users where user_id='+str(self.userid.text)+';'
		print query
		try:
			cur.execute(query)
			db.commit()
			self.add_widget(Label(text="Success",size_hint=(None,None),pos=(320,280)))
			self.userid.text='User ID'
		except:
			self.add_widget(Label(text="Please enter Correct User ID.",size_hint=(None,None),pos=(320,250)))

	def goback(self,a):
		App.get_running_app().stop()
		AdminApp().run()


class DeleteUser(App):

    def build(self):
        return DeleteUserScreen()
#END Deleteuser

#Design of AddUser screen.
class AddUserScreen(FloatLayout):
        def __init__(self, **kwargs):
                super(AddUserScreen, self).__init__(**kwargs)
                self.cols = 2
               

		self.userid = TextInput(multiline=False,size_hint=(None,None),width=200,height=30,pos=(40,500),focus=True,text="User ID")
                self.add_widget(self.userid)
		#Add textBoxes here. u left coding coz submission is postponed. moron
		self.password=TextInput(multiline=False,size_hint=(None,None),width=200,height=30,pos=(270,500),focus=True,text="password")
		self.add_widget(self.password)

		self.name=TextInput(multiline=False,size_hint=(None,None),width=200,height=30,pos=(40,460),focus=True,text="Name")
		self.add_widget(self.name)
		
		self.address=TextInput(multiline=True,size_hint=(None,None),width=200,height=30,pos=(270,460),focus=True,text="Address")
		self.add_widget(self.address)

		self.ph=TextInput(multiline=False,size_hint=(None,None),width=200,height=30,pos=(40,420),focus=True,text="Phone No")
		self.add_widget(self.ph)

		self.mail=TextInput(multiline=False,size_hint=(None,None),width=200,height=30,pos=(270,420),focus=True,text="Email")
		self.add_widget(self.mail)

		self.bck=Button(text="Back",font_size=14,pos=(600,500),size_hint=(None,None),width=100,height=30)
		self.bck.bind(on_press=self.goback)
		
		self.submit=Button(text="Submit",font_size=14,pos=(320,350),size_hint=(None,None),width=100,height=30)
		self.submit.bind(on_press=self.submitt)
		self.add_widget(self.submit)
		self.add_widget(self.bck)
	
	def submitt(self,a):
		query="insert into users values("+str(self.userid.text)+",'"+str(self.password.text)+"','"+str(self.name.text)+"','"+str(self.address.text)+"','"+str(self.ph.text)+"','"+str(self.mail.text)+"');"
		print query
		try:
			cur.execute(query)
			db.commit()
			self.add_widget(Label(text="Success",size_hint=(None,None),pos=(320,280)))
			self.userid.text='User ID'
			self.password.text='password'
			self.name.text='Name'
			self.address.text="Address"
			self.ph.text="Phone no"
			self.mail.text="Email"
		except:
			self.add_widget(Label(text="Please enter all fields correctly.",size_hint=(None,None),pos=(320,250)))

	def goback(self,a):
		App.get_running_app().stop()
		AdminApp().run()


class AddUser(App):

    def build(self):
        return AddUserScreen()
#END adduser


#Design of userlogin screen.
class UserLoginScreen(FloatLayout):
        def __init__(self, **kwargs):
                super(UserLoginScreen, self).__init__(**kwargs)
                self.cols = 2
                self.but=Button(text="Login",font_size=14,pos=(250,200),size_hint=(None,None),width=100,height=30)
                self.but.bind(on_press=self.userlogin)
                self.add_widget(Label(text='Password:',pos=(200,240),size_hint=(None,None)))
                self.password = TextInput(password=True, multiline=False,size_hint=(None,None),width=300,height=35,pos=(300,270),focus=True)
                self.add_widget(self.password)
		self.add_widget(Label(text='User ID:',pos=(200,270),size_hint=(None,None)))
                self.userid = TextInput(multiline=False,size_hint=(None,None),width=300,height=35,pos=(300,310),focus=True)
                self.add_widget(self.userid)
                self.add_widget(self.but)	
		self.bck=Button(text="Back",font_size=14,pos=(350,200),size_hint=(None,None),width=100,height=30)
		self.bck.bind(on_press=self.goback)
		self.add_widget(self.bck)


        def userlogin(self,a):
                #Run query to check for userid and password. 
		query="select user_id,name,address from users where user_id="+str(self.userid.text)+" and password='"+str(self.password.text)+"';"
		result=''
		global userid,username,address
                try:
			cur.execute(query)
			result=cur.fetchall()
		except:
			 self.add_widget(Label(text='Please enter username and password correctly.',pos=(400,130),size_hint=(None,None)))
		if len(result)<1:	 
			self.add_widget(Label(text='Please enter username and password correctly.',pos=(400,130),size_hint=(None,None)))
		else:
			#Store the user info to display in next window in global variables.
			userid=result[0][0]
			username=result[0][1]
			address=result[0][2]
			#Close this app and open next app.
			App.get_running_app().stop()
			UserApp().run()

	def goback(self,a):
		App.get_running_app().stop()
		MyApp().run()

class UserLogin(App):

    def build(self):
        return UserLoginScreen()
#END userlogin

#Design of USER SCREEN.
class UserScreen(FloatLayout):
        def __init__(self, **kwargs):
                super(UserScreen, self).__init__(**kwargs)
                self.cols = 2
		global userid,username,address,tot
                self.add_widget(Label(text=str(userid),pos=(320,500),size_hint=(None,None)))
		self.add_widget(Label(text=str(username),pos=(320,480),size_hint=(None,None)))
		self.add_widget(Label(text=str(address),pos=(320,460),size_hint=(None,None)))
		self.logoutButton=Button(text='Logout',font_size=14,size_hint=(None,None),height=30,width=60,pos=(600,500))
		self.logoutButton.bind(on_press=self.logout)
		self.add_widget(self.logoutButton)
		self.lbl1=Label(text='Bills to be paid:',pos=(150,400),size_hint=(None,None))
		self.add_widget(self.lbl1)
		query='select * from bill where user_id="'+str(userid)+'"and status="unpaid";'
		st='Bill_no      Amount      Due Date        Status\n\n\n'
		try:
			cur.execute(query)
			result=cur.fetchall()
			tot=0
			for row in result:
				st+=str(row[0])+'             '+str(row[2])+'             '+str(row[3])+'          '+str(row[4])
				st+='\n\n'
				tot+=row[2]
			st+='\n\nTotal Amount: '+str(tot)
		except:
			print 'jhs'
		self.lbl2=Label(text=st,pos=(400,280),size_hint=(None,None))
		self.add_widget(self.lbl2)
		self.payButton=Button(text='Make Payment',font_size=14,pos=(320,100),size_hint=(None,None),height=30,width=100)
		self.payButton.bind(on_press=self.pay)
		self.add_widget(self.payButton)
		self.but=Button(text='See payment history',font_size=14,size_hint=(None,None),height=30,width=200,pos=(270,60))
		self.add_widget(self.but)
		self.but.bind(on_press=self.history)
		
	def history(self,a):
		global userid
		query='select p.payment_id,p.amount from users u,payment p where u.user_id=p.user_id and u.user_id='+str(userid)+';'
		print query
		st='Payment ID      Amount\n\n'
		try:
			cur.execute(query)
			result=cur.fetchall()
			for row in result:
				st+=str(row[0])+'               '+str(row[1])+'\n'
			self.remove_widget(self.lbl2)
			self.lbl1.text="Payments:"
			self.lbl3=Label(text=st,pos=(400,280),size_hint=(None,None))
			self.add_widget(self.lbl3)

		#Remove the old label and display new label.
		except:print 'Something went wrong'

	def pay(self,a):
		App.get_running_app().stop()
		PayApp().run()

	def logout(self,a):
		App.get_running_app().stop()
		UserLogin().run()


class UserApp(App):

    def build(self):
	print username,userid,address
        return UserScreen()
#END USER SCREEN


#Design of apyment screen.
class PaymentScreen(FloatLayout):
        def __init__(self, **kwargs):
                super(PaymentScreen, self).__init__(**kwargs)
                self.cols = 2
                self.but=Button(text="Pay",font_size=14,pos=(250,200),size_hint=(None,None),width=100,height=30)
                self.but.bind(on_press=self.userlogin)
                self.add_widget(Label(text='Password:',pos=(200,240),size_hint=(None,None)))
                self.password = TextInput(password=True, multiline=False,size_hint=(None,None),width=300,height=35,pos=(300,270),focus=True)
                self.add_widget(self.password)
		self.add_widget(Label(text='Card No:',pos=(200,270),size_hint=(None,None)))
                self.userid = TextInput(multiline=False,size_hint=(None,None),width=300,height=35,pos=(300,310),focus=True)
                self.add_widget(self.userid)
                self.add_widget(self.but)	
		self.bck=Button(text="Back",font_size=14,pos=(350,200),size_hint=(None,None),width=100,height=30)
		self.bck.bind(on_press=self.goback)
		self.add_widget(self.bck)


        def userlogin(self,a):
		global userid,tot
                query='update bill set status="paid" where user_id='+str(userid)+';'
		try:cur.execute(query)
		except:print 'Something went wrong'
		query='select max(payment_id) from payment'
		try:
			cur.execute(query)
			result=cur.fetchall()
			payid=result[0][0]+1
		except:print ''
		try:query='insert into payment values('+str(payid)+','+str(tot)+',05-11-2016,'+str(userid)+');'
		except:print ''
		cur.execute(query)
		db.commit()
		App.get_running_app().stop()
		UserApp().run()

	def goback(self,a):
		App.get_running_app().stop()
		UserApp().run()

class PayApp(App):

    def build(self):
        return PaymentScreen()
#END userlogin


if __name__ == '__main__':
	MyApp().run()
	db.close()
