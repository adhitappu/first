import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 4000
    recognizer.dynamic_energy_adjustment_damping = 0.010  # less more active
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.5
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.2

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            print("I am Listening...", end="", flush=True)
            try:
                audio = recognizer.listen(source, timeout=None)
                print("\r" + "Got it, Now Recognizing...", end="", flush=True)
                recognized_txt = recognizer.recognize_google(audio).lower()
                if recognized_txt:
                    print("\r" + "Mr Adithyan: " + recognized_txt)
            except sr.UnknownValueError:
                recognized_txt = ""
            finally:
                print("\r", end="", flush=True)


