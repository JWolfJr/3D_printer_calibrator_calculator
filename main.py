from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton



class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.primary_hue = '200'
        self.theme_cls.theme_style = "Dark"
    
        screen = Screen()
        extrude_btn = MDRectangleFlatButton(text="Hello World", pos_hint={'center_x': 0.5, 'center_y': 0.6})
        flow_btn = MDRectangleFlatButton(text="Hello World 2", pos_hint={'center_x': 0.5, 'center_y': 0.2})
        screen.add_widget(extrude_btn)
        screen.add_widget(flow_btn)
        return screen

    

MainApp().run()