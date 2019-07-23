# portofvirginia

## Check to See If You Have Python 3 Installed

- python --version
- Otherwise download Python3: https://www.python.org/downloads/release/python-369/

## Run these Commands

- sudo apt-get install python3-pip
  - If that command didn't work install this and run from this program: https://gitforwindows.org/
- pip3 install --upgrade pip

## Change directory to the downloaded portofvirginia

- cd ~/Desktop/portofvirginia
- pip3 install -r requirements.txt

## Run This Command to Run the Program

- cd ~/Desktop/portofvirginia
- /c/python37-32/python ~/Desktop/portofvirginia-master/portofvirginia-master/main.py

## Using the Program

- The program relies on Chrome being open against the left side of the screen, not covered by other windows. Also you have to have logged into portofvirginia in Chrome lately. Let me know if it works for you.
- You must fill out the input.csv file with the start_date, end_date, and license_plate.  The first row should be the column name, and following rows are the dates and license plates you want to check.  The dates should be in yyyy-mm-dd format.  If Excel autocorrects it to be in a different date format, you can also open the input.csv file as a text file.
- The output will be saved in the output folder.
- Log into the portofvirginia website and visit the page "Gate Transactions" (Under POV Tracking)
- If you need to stop the program, move the mouse to the top left corner of the screen to stop it from controlling your mouse any longer
