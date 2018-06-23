# Birthday Reminder Application

import time # Reminder is set with the help of dates
import os # Notify user using default "Ubuntu" notification bar

birthdayFile = "/home/vish/Documents/birthdays.txt"

def checkBirthday():
    fileName = open(birthdayFile, "r")
    today = time.strftime("%m%d")
    status = 0 # Used to check whether today there is any birthday or not. If not notify according to it.
    for line in fileName:
        if today in line:
            status = 1
            # line[1] contains first name & line[2] contains last name
            os.system('notify-send "Birthdays Today: ' + line[1]+ ' ' + line[2] + '"')
    if status = 0:
        os.system('notify-send "No Birthdays Today."')

if __name__ == '__main__':
    checkBirthday()
