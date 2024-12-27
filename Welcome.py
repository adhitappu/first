from Mouth import speak
from dlg import welcomedlg
import random


def welcome():
    welcome = random.choice(welcomedlg)
    speak(welcome)

welcome()
