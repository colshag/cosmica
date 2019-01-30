# ---------------------------------------------------------------------------
# Cosmica - All rights reserved by NeuroJump Trademark 2018
# launcher.py
# Written by Chris Lewis
# ---------------------------------------------------------------------------
# The COSMICA Launcher
# ---------------------------------------------------------------------------
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang.builder import Builder
from xmlrpclib import ServerProxy

class LoginPage(Screen):
    def login_user(self):
        myInfo = {'email':self.ids['login'].text,
                  'password':self.ids['passw'].text,
                  'name':'testguy',
                  'totallogincount':2}
        #try:
        server = ServerProxy('http://localhost:8090/')
        result = server.register_new_player(myInfo)
        if result == 1:
            popup = Popup(title='Welcome to Cosmica', content=Label(text='Welcome %s' % myInfo['name']),
                          auto_dismiss=True, size_hint=(None, None), size=(400, 400))
            popup.open()
            self.manager.current = 'user_page'
        else:
            popup = Popup(title='Login Error', content=Label(text=result),
                          auto_dismiss=True, size_hint=(None, None), size=(400, 400))
            popup.open()
        #except:
            #pass

class UserPage(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

kv_file = Builder.load_file('login.kv')

class LoginApp(App):
    def builder(self):
        return kv_file

if __name__ == '__main__':
    LoginApp().run()