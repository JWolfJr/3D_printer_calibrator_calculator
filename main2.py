from kivymd.app import MDApp
from kivy.lang import Builder
#from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
#from main import KV


class MainApp(MDApp):
    dialog = None

    def build(self):
        #screen = Screen()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        #self.extrusion = Builder.load_string(KV)
        #screen.add_widget(self.extrusion)
        return Builder.load_file('main.kv')

    #Calculate rotation_distance as: rotation_distance = <previous_rotation_distance> * <actual_extrude_distance> / <requested_extrude_distance> Round the new rotation_distance to three decimal places.
    def calc_extrusion(self):
        prev_num = float(self.root.ids.prev_rotation.text)
        ext_dist = float(self.root.ids.extrude_dist.text)
        new_rot = prev_num * ext_dist / 100
        self.dialog = MDDialog(
            text="Rotate this beeotch! " + str(round(new_rot, 3)),
            radius=[20,7,20,7],
            auto_dismiss=False,
            buttons=[MDRaisedButton(text="Close",
            on_release=self.close_dialog)]
        )
        self.dialog.open()

    # Adjust your extrusion multiplier to: (current extrusion multiplier × extrusion width) / measured wall thickness.
    def calc_flow(self):
        old_mult = float(self.root.ids.prev_flow_wall.text)
        curr_flow = float(self.root.ids.flow_wall.text)
        new_flow = old_mult * .40 / curr_flow
        
        self.dialog = MDDialog( 
            text="Get that flow right! " + str(round(new_flow)), 
            radius=[20,7,20,7],
            auto_dismiss=False, 
            buttons=[MDRaisedButton(text="Close", 
            on_release=self.close_dialog)]
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

if __name__ == "__main__":
    app = MainApp()
    app.run()