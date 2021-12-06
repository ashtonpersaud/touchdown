from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import serial
import time
import subprocess
import decimal

class touchdownSkill(MycroftSkill):

    def __init__(self):
        super().__init__()
        self.learning = True

    def initialize(self):
        my_setting = self.settings.get('my_setting')

    @intent_handler('touchdown.intent')
    def handle_not_are_you_intent(self, message):
        serA = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        serB = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
        serC = serial.Serial('/dev/ttyACM2', 9600, timeout=1)
        serD = serial.Serial('/dev/ttyACM3', 9600, timeout=1)
        time.sleep(0.5)
        serA.flush()
        serB.flush()
        serC.flush()
        serD.flush()
        time.sleep(0.5)
        serA.write(b"touch")
        serB.write(b"touch")        
        serC.write(b"touch")
        serD.write(b"touch") 
        time.sleep(0.5)
        self.speak_dialog("Touch down by the knights")

    def stop(self):
        pass

def create_skill():
    return touchdownSkill()
