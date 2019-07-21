from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
import subprocess
from datetime import datetime
import pyperclip as clip
import os
import pyautogui as g

from time import sleep
g.FAILSAFE = True
sleep(2)
g.size()
g.position()

def c():
    g.mouseDown()
    g.mouseUp()

def c2():
    c()
    c()

def rc():
    g.click(button='right')

def select_all_and_copy():
    rc()
    g.keyDown('a')
    g.keyUp('a')
    g.keyDown('ctrl')
    g.keyDown('c')
    g.keyUp('c')
    g.keyUp('ctrl')






class GuiApp(App):
    my_string = StringProperty('default')
    start_date = None
    end_date = None
    license_plate = None
    table_name = None
    i = 1


    def get_urls_and_json_to_csv(self, instance):
        for license_plate in self.license_plate.text.split(","):
            license_plate = license_plate.strip()
            g.moveTo(12, 632)
            c()
            g.keyDown('command')
            g.keyDown('t')
            g.keyUp('command')
            g.keyUp('t')
            sleep(0.3)
            import pyperclip as clip
            clip.copy("http://propassva.portofvirginia.com/api/gate?startDateTime={}T07:00:00.000Z&endDateTime={}T07:00:00.000Z&licensePlate={}".\
                        format(self.start_date.text, self.end_date.text, license_plate))
            sleep(0.3)
            g.keyDown('command')
            g.keyDown('v')
            g.keyUp('command')
            g.keyUp('v')
            sleep(0.1)
            g.keyDown('enter')
            g.keyUp('enter')
            sleep(0.1)
            c()
            sleep(0.1)
            g.keyDown('command')
            g.keyDown('a')
            g.keyUp('a')
            sleep(0.05)
            g.keyDown('c')
            g.keyUp('c')
            g.keyUp('command')
            self.json_to_csv(None)

    def get_url(self, instance):
        pass
        url = "http://propassva.portofvirginia.com/api/gate?startDateTime={}T07:00:00.000Z&endDateTime={}T07:00:00.000Z&licensePlate={}".\
            format(self.start_date.text, self.end_date.text, self.license_plate.text)
        clip.copy(url)
        # copied_text = clip.paste()

    def json_to_csv(self, instance):
        # Make JSON
        file = open("data.json", "w")
        file.write(clip.paste())
        file.close()

        # JSON to CSV
        run_command('in2csv "data.json" > "data{}.csv"'.format(self.i))
        self.i = self.i + 1

        # Remove JSON
        os.remove("data.json")

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
        self.license_plate = TextInput(text="UN11316,UN11316,UN11316")
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
        button = Button(
            text="List of Licenses to CSV", font_size=24)
        button.bind(on_press=self.get_urls_and_json_to_csv)
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
