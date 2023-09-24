from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

from kivy.core.image import Image
from config import width, hieght
class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        with layout.canvas.before:
            bg = Image('bg.png').texture
            self.rect = Rectangle(texture=bg, size=(width, hieght), pos=layout.pos)
        
        self.prompt_input = TextInput(hint_text='Введите промпт', size_hint=(None, None), size=(400, 50), multiline=False, pos_hint={'center_x': 0.5})
        layout.add_widget(self.prompt_input)
        send_button = Button(text='Отправить промпт', size_hint=(None, None), size=(200, 50), disabled=False, pos_hint={'center_x': 0.5})
        send_button.bind(on_release=self.send_prompt)
        layout.add_widget(send_button)
        
        help_button = Button(text='?', size_hint=(None, None), size=(50, 50), pos_hint={'right': 1, 'top': 1})
        help_button.background_color = (0.8, 0.2, 0.2, 1) 
        help_button.bind(on_release=self.show_help_text)
        layout.add_widget(help_button)
        
        self.help_label = Label(text='', size_hint=(None, None), size=(400, 200), pos_hint={'right': 1, 'top': 0.9})
        layout.add_widget(self.help_label)
        
        return layout
    
    def send_prompt(self, instance):  # TODO create a function to send prompt to server
        print('Промпт отправлен. Спасибо!. Промпт:', self.prompt_input.text)
        self.prompt_input.text = ""
        pass
    
    def show_help_text(self, instance):
        from config import help_text
        self.help_label.text = help_text
    
    def on_layout(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    MyApp().run()