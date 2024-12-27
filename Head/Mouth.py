import asyncio
import threading
import os
import edge_tts
import pygame
pygame.init()

VOICE = "en-AU-WilliamNeural"
BUFFER_SIZE = 1024


def remove_file(fiile_path):
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            with open(fiile_path, "wb"):
                pass
            os.remove(fiile_path)
            break
        except Exception as e:
            print(f"error: {e}")
            attempts += 1


async def amain(TEXT, output_file) -> None:
    try:
        cm_txt = edge_tts.Communicate(TEXT, VOICE)
        await cm_txt.save(output_file)
        thread = threading.Thread(target=play_audio, args=(output_file,))
        thread.start()
        thread.join()
    except Exception as e:
            print(f"error: {e}")
    finally:
        remove_file(output_file)


def play_audio(file_path):
    try:
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound(file_path)
        sound.play()
        while pygame.mixer.get_busy():
            pygame.time.get_ticks()
        pygame.quit()
    except Exception as e:
        print(f"error : {e}")


def speak(TEXT, output_file=None):
    if output_file is None:
        output_file = F"{os.getcwd()}/speak.mp3"
    asyncio.run(amain(TEXT, output_file))


speak("welcome sir my name is nova i am hear to help you.");
