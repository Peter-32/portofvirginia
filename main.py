from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
import pyperclip as clip
import subprocess
from datetime import datetime


class GuiApp(App):
    my_string = StringProperty('default')
    start_date = None
    end_date = None
    license_plate = None
    table_name = None


    def get_url(self, instance):
        pass

    def json_to_csv(self, instance):
        pass


    def build(self):
        root = Accordion(orientation='vertical')
        item = AccordionItem(title='Gate Transactions')
        item.add_widget(Label(text=\
        """1) Login to Port of Virginia
2) Fill in these fields
3) Click "Get URL" and paste the URL into the browser
4) Copy all text (Command or Control+A) on this page
5) Click this button to create the CSV"""))
        page = BoxLayout(orientation='vertical')
        subpage = BoxLayout(orientation='vertical')
        input1 = BoxLayout(orientation='horizontal')
        input2 = BoxLayout(orientation='horizontal')
        input3 = BoxLayout(orientation='horizontal')
        input1.add_widget(Label(text='Start Date (yyyy-mm-dd):'))
        self.start_date = TextInput(text=datetime.now().strftime("%Y-%m-01"))
        input1.add_widget(self.start_date)
        input2.add_widget(Label(text='End Date (yyyy-mm-dd):'))
        self.end_date = TextInput(text=datetime.now().strftime("%Y-%m-%d"))
        input2.add_widget(self.end_date)
        input3.add_widget(Label(text='License Plate:'))
        self.license_plate = TextInput(text="UN11316")
        input3.add_widget(self.license_plate)
        buttons = GridLayout(cols=1)
        button = Button(
            text="Get URL", font_size=24)
        button.bind(on_press=self.get_url)
        buttons.add_widget(button)
        button = Button(
            text="JSON to CSV", font_size=24)
        button.bind(on_press=self.json_to_csv)
        buttons.add_widget(button)
        page.add_widget(subpage)
        subpage.add_widget(input1)
        subpage.add_widget(input2)
        subpage.add_widget(input3)
        page.add_widget(buttons)
        item.add_widget(page)
        root.add_widget(item)
        return root

def run_command(command):
    try:
        subprocess.check_output(command, shell=True)
    except:
        raise

if __name__ == '__main__':
    GuiApp().run()
