import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")
            return ""
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results. Check your internet connection.")
            return ""

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {now}")
    elif "date" in command:
        today = datetime.datetime.today().strftime("%Y-%m-%d")
        speak(f"Today's date is {today}")
    elif "search" in command:
        speak("What would you like to search for?")
        query = recognize_speech()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Here are the search results for {query}")
    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("open -a TextEdit")  # For macOS
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm not sure how to respond to that.")

def main():
    speak("Voice assistant activated. How can I help you?")
    while True:
        command = recognize_speech()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()
