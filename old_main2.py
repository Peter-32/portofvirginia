import pyforms
from pyforms.basewidget import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton
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


class SimpleExample1(BaseWidget):

    def __init__(self):
        super(SimpleExample1,self).__init__('Simple example 1')

        #Definition of the forms fields
        self.start_date = ControlText('Start Date', default=datetime.now().strftime("%Y-%m-01"))
        self.end_date = ControlText('End Date', default=datetime.now().strftime("%Y-%m-%d"))
        self.license_plate = ControlText('License Plates', default='UN11316,UN11316,UN11316')
        self._button        = ControlButton('Press this button')
        self.i = 1

        self._button.value = self.__buttonAction

    def __buttonAction(self):
        for license_plate in self.license_plate.value.split(","):
            license_plate = license_plate.strip()
            g.moveTo(12, 632)
            c()
            g.keyDown('ctrl')
            g.keyDown('t')
            g.keyUp('ctrl')
            g.keyUp('t')
            sleep(0.3)
            import pyperclip as clip
            clip.copy("http://propassva.portofvirginia.com/api/gate?startDateTime={}T07:00:00.000Z&endDateTime={}T07:00:00.000Z&licensePlate={}".\
                        format(self.start_date.value, self.end_date.value, license_plate))
            sleep(0.3)
            g.keyDown('ctrl')
            g.keyDown('v')
            g.keyUp('ctrl')
            g.keyUp('v')
            sleep(0.1)
            g.keyDown('enter')
            g.keyUp('enter')
            sleep(3.0)
            c()
            sleep(3.0)
            g.keyDown('ctrl')
            g.keyDown('a')
            g.keyUp('a')
            sleep(0.5)
            g.keyDown('c')
            g.keyUp('c')
            g.keyUp('ctrl')
            self.json_to_csv()

    def json_to_csv(self):
        # Make JSON
        file = open("data.json", "w")
        file.write(clip.paste())
        file.close()

        try:
            # JSON to CSV
            run_command('in2csv "data.json" > "data{}.csv"'.format(self.i))
            self.i = self.i + 1

            # Remove JSON
            os.remove("data.json")
        except Exception as e:
            print(e)



def run_command(command):
    try:
        subprocess.check_output(command, shell=True)
    except:
        raise

#Execute the application
from pyforms import start_app
if __name__ == "__main__":   start_app( SimpleExample1 )
