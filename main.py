import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ''  # Initialize command variable
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()  # Strip whitespace
                print(f"Command received: {command}")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Could not request results; check your network connection.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return command  # Always return command, even if it's an empty string

def run_alexa():
    command = take_command()
    if command:
        if 'play' in command:
            song = command.replace('play', '').strip()  # Strip whitespace
            talk(f'Playing {song}')
            pywhatkit.playonyt(song)
        elif 'stop' in command:
            talk("Goodbye!")
            exit()  # Exit the program
        else:
            talk('Please say the command again.')

while True:
    run_alexa()
