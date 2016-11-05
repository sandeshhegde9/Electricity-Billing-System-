import MySQLdb
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

db=MySQLdb.connect(host='localhost',user='root',passwd='sandesh123',db='ElectricityBill')
cur=db.cursor()

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
		print "jhgd"
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
                print "jhgd"
	def goback(self,a):
		App.get_running_app().stop()
		MyApp().run()




class UserLogin(App):

    def build(self):
        return UserLoginScreen()
#END userlogin


if __name__ == '__main__':
	MyApp().run()
	db.close()
