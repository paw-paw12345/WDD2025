import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# Set your password
PASSWORD = "1234"

# Ask user for password
speak("Welcome. Please enter your password.")
user_input = input("Password: ")

# Check password
if user_input == PASSWORD:
    speak("Access granted.")
    print("You are now logged in.")
else:
    speak("Access denied.")
    print("Wrong password.")
