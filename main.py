from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
import os
from kivymd.uix.screen import MDScreen

class HomeScreen(MDScreen):
    def __init__(self, *args,**kwargs):
        super(HomeScreen, self).__init__(*args,**kwargs)

class LoginScreen(MDScreen):
    def __init__(self, *args,**kwargs):
        super(LoginScreen, self).__init__(*args,**kwargs)

class UI(Factory.ScreenManager):
    def __init__(self, *args,**kwargs):
        super(UI, self).__init__(*args,**kwargs)

class Novfensec(MDApp,App):
    def __init__(self, *args,**kwargs):
        super(Novfensec, self).__init__(*args,**kwargs)
        self.KV_FILES={
            os.path.join(os.getcwd(),"kv_files/app.kv")
            #all kv files path here
        }
        self.CLASSES={
            "UI":"main" # main file name or root file name
        }
        self.AUTORELOADER_PATHS=[
            (".",{"recursive":True}),
        ]
        self.theme_cls.primary_palette="Indigo"
        self.DEBUG=True
        
    def build_app(self):
        self.manager_screens=Factory.UI()
        self.generate_application_screens()
        self.manager_screens.current="home screen"
        return self.manager_screens
    
    def generate_application_screens(self):
        self.manager_screens.add_widget(HomeScreen(name="home screen"))
        self.manager_screens.add_widget(LoginScreen(name="login screen"))

if __name__ == '__main__':
    Novfensec().run()
    
