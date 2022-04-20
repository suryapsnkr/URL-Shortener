import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
import pyshorteners



Builder.load_string("""#:kivy 2.1.0
<MyLayout>
    canvas.before:
        Color:
            rgba: 0, 1, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation:"vertical"
        size:root.width,root.height
        padding: 50
        scalling: 50


        TextInput:
            id: main_url
            multiline: False

        Button:
            text:"Generate URL"
            font_size: 50
            on_press:root.gen_url()
            background_color: (2, 0, 0, 1)

        TextInput:
            id: short_url
            multiline:False
""")

class MyLayout(Widget):        
    def gen_url(self):
        #create variable for our widget
        prior=self.ids.main_url.text
        
        try:
            url_short = pyshorteners.Shortener().tinyurl.short(prior)
            #output the short url
            self.ids.short_url.text=url_short
        except:
            self.ids.short_url.text="Invalid URL OR Network Issues"  

class URLShortenerApp(App):
    def build(self):
        self.icon='url_s.png'
        return MyLayout()

if __name__=='__main__':
    URLShortenerApp().run()