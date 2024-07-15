import os
import glob
from kaki.app import App
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.factory import Factory
from kivy.core.window import Window
from kivy import Config
from PIL import ImageGrab

resolution = ImageGrab.grab().size

# Change the values of the application window size as you need.
Config.set("graphics", "height", "700")
Config.set("graphics", "width", "317")

# Place the application window on the right side of the computer screen.
Window.top = 30
Window.left = resolution[0] - Window.width + 5

class HomeScreen(MDScreen):
    def __init__(self, *args,**kwargs):
        super(HomeScreen, self).__init__(*args,**kwargs)

class LoginScreen(MDScreen):
    def __init__(self, *args,**kwargs):
        super(LoginScreen, self).__init__(*args,**kwargs)

class ContentNavigationDrawer(MDNavigationDrawer):
    def __init__(self, *args, **kwargs):
        super(ContentNavigationDrawer, self).__init__(*args,**kwargs)
        
class ContentNavigationLayout(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super(ContentNavigationLayout, self).__init__(*args,**kwargs)

class UI(Factory.ScreenManager):
    def __init__(self, *args,**kwargs):
        super(UI, self).__init__(*args,**kwargs)

class Novfensec(MDApp,App):
    def __init__(self, *args,**kwargs):
        super(Novfensec, self).__init__(*args,**kwargs)
        self.DEBUG=True
        self.KV_FILES=[]
        for file in glob.glob(f"{self.directory}/kv_files/*.kv"):
            self.KV_FILES.append(file) # load all kv file in a certain directory
        self.CLASSES={
            "UI":"main" # main file name or root file name
        }
        self.AUTORELOADER_PATHS=[
            (".",{"recursive":True}),
        ]
        self.theme_cls.primary_palette="Indigo"
        self.theme_cls.primary_dark_hue="800"
        self.theme_cls.primary_light_hue="50"
        self.theme_cls.accent_palette="Indigo"
        self.theme_cls.accent_dark_hue="600"
        self.theme_cls.accent_light_hue="100"
        
    def build_app(self):
        self.manager_screens=Factory.UI()
        self.generate_application_screens()
        self.manager_screens.current="home screen"
        return self.manager_screens
    
    def generate_application_screens(self):
       # adds different screen widgets to the screen manager 
        self.manager_screens.add_widget(HomeScreen(name="home screen"))
        self.manager_screens.add_widget(LoginScreen(name="login screen"))

if __name__ == '__main__':
    Novfensec().run()

'''
For Production uncomment the below code and comment out the above code
'''

# from kivymd.app import MDApp
# from kivymd.uix.screenmanager import MDScreenManager
# from kivymd.uix.screen import MDScreen
# from kivymd.uix.navigationdrawer import MDNavigationDrawer
# from kivymd.uix.boxlayout import MDBoxLayout

# class HomeScreen(MDScreen):
#     def __init__(self, *args,**kwargs):
#         super(HomeScreen, self).__init__(*args,**kwargs)

# class LoginScreen(MDScreen):
#     def __init__(self, *args,**kwargs):
#         super(LoginScreen, self).__init__(*args,**kwargs)

# class ContentNavigationDrawer(MDNavigationDrawer):
#     def __init__(self, *args, **kwargs):
#         super(ContentNavigationDrawer, self).__init__(*args,**kwargs)
        
# class ContentNavigationLayout(MDBoxLayout):
#     def __init__(self, *args, **kwargs):
#         super(ContentNavigationLayout, self).__init__(*args,**kwargs)

# class Novfensec(MDApp):
#     def __init__(self, *args,**kwargs):
#         super(Novfensec, self).__init__(*args,**kwargs)
#         self.load_all_kv_files(self.directory)
#         self.theme_cls.primary_palette="Indigo"
#         self.theme_cls.primary_dark_hue="800"
#         self.theme_cls.primary_light_hue="50"
#         self.theme_cls.accent_palette="Indigo"
#         self.theme_cls.accent_dark_hue="600"
#         self.theme_cls.accent_light_hue="100"
#         self.manager_screens=MDScreenManager()
        
#     def build(self):
#         self.generate_application_screens()
#         self.manager_screens.current="home screen"
#         return self.manager_screens
    
#     def generate_application_screens(self):
#        # adds different screen widgets to the screen manager 
#         self.manager_screens.add_widget(HomeScreen(name="home screen"))
#         self.manager_screens.add_widget(LoginScreen(name="login screen"))

# if __name__ == '__main__':
#     Novfensec().run()
