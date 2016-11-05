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

	def goback(self,a):
		App.get_running_app().stop()
		MyApp().run()


class AdminLogin(App):

    def build(self):
        return AdminLoginScreen()
#END adminlogin

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
		self.add_widget(Label(text='Bills to be paid:',pos=(150,400),size_hint=(None,None)))
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
			st+='\n\nTotal Amount:'+str(tot)
		except:
			print 'jhs'
		self.add_widget(Label(text=st,pos=(400,280),size_hint=(None,None)))
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
				st+=str(row[0])+'         '+str(row[1])+'\n\n'

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
