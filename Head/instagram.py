import webbrowser
from Mouth import speak
from gtts import gTTS

def get(text):
    if "instagram" in text.lower():
        speak("Opening Instagram, sir.")
        print("Opening Instagram, sir.")
        url = "https://www.instagram.com"
        webbrowser.open(url)
    else:
        speak("I'm sorry, I didn't catch that. Please say Instagram.")
        print("I'm sorry, I didn't catch that. Please say Instagram.")

text = "instagram"  # Call the listen function to get the text
get(text)  # Pass the text to the get function
