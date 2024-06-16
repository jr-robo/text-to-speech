import pyttsx3
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFillRoundFlatButton
# engine = pyttsx3.init()
#
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# # for male 0 and female 1
# engine.say("hey jeevan")
# engine.runAndWait()


from kivymd.uix.screen import MDScreen

Window_size = (900, 650)

kv="""
MDBoxLayout:
    orientation:"vertical"
    spacing:45
    padding:200

    MDLabel:
        
        text:"Speaker"
        font_style:"H2"
        halign:"center"
        theme_text_color:"Hint"
        
        
    MDTextField:
        mode:"rectangle"
        id:name
        #hint_text:"Write"
        
        pos_hint:{"center_x":0.5,"center_y":0.5}
        size_hint_x:0.5
        
    MDFillRoundFlatButton:
        text:"Speak"
        pos_hint:{"center_x":0.5,"center_y":0.5}
        on_press:app.word()
        
    MDFillRoundFlatButton:
        text:"close"
        pos_hint:{"center_x":0.5,"center_y":0.5}
        on_press:app.close()
"""





class SpeakApp(MDApp):
    def build(self):
        #self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(kv)

    def word(self):
        bol=self.root.ids.name.text

        engine = pyttsx3.init()
        engine.say(bol)
        engine.runAndWait()

    def close(self):
        app=MDApp.get_running_app()
        app.stop()

SpeakApp().run()


