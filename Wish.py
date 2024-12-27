from Mouth import speak
import random
from datetime import datetime, date
from dlg import morning_greetings,afternoon_greetings,evening_greetings,goodnight_greetings
from Welcome import welcome
today = date.today()
formatted_data = today.strftime("%d %b %y")
nowx = datetime.now()

def wish():
    current_hour = nowx.hour
    if 5 <= current_hour < 12:
        gd_dlg = random.choice(morning_greetings)
        speak(gd_dlg)
    elif 12 <= current_hour < 17:
        ga_dlg = random.choice(afternoon_greetings)
        speak(ga_dlg)
    elif 17 <= current_hour <21:
        ge_dlg = random.choice(evening_greetings)
        speak(ge_dlg)
    else:
        gn_dlg = random.choice(goodnight_greetings)
        speak(gn_dlg)

