import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set speech rate
engine.setProperty('rate', 150)

# Set speech volume
engine.setProperty('volume', 0.7)

# Define voice assistant's name
assistant_name = "Nova"

# Define microphone
microphone = sr.Recognizer()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user's voice command"""
    with sr.Microphone() as source:
        audio = microphone.listen(source)
        try:
            command = microphone.recognize_google(audio, language='en-US')
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return None

def greet():
    """Greet user based on time"""
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

def process_command(command):
    """Process user's voice command"""
    if "what's your name" in command:
        speak(f"My name is {assistant_name}.")
    elif "what time is it" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}.")
    elif "search for" in command:
        query = command.replace("search for", "")
        pywhatkit.search(query)
        speak(f"Searching for {query}.")
    elif "tell me about" in command:
        query = command.replace("tell me about", "")
        info = wikipedia.summary(query, sentences=2)
        speak(info)
    elif "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)
    else:
        speak("Sorry, I didn't understand that.")

def main():
    greet()
    while True:
        command = listen()
        if command is not None:
            process_command(command)

if __name__ == "__main__":
    main()

