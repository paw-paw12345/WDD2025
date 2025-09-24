import openai
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import webbrowser

# 💡 Put your OpenAI API key here
openai.api_key = "sk-Your-OpenAI-Key"

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print("🗣️ Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("🧑 You:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

def ask_chatgpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    answer = response['choices'][0]['message']['content']
    return answer.strip()

def run_assistant():
    speak("Hi, I am your AI assistant. What can I do for you?")
    while True:
        command = listen()

        if "stop" in command or "bye" in command:
            speak("Goodbye! Talk to you later.")
            break

        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {now}")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "play" in command:
            song = command.replace("play", "")
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif "what is" in command or "who is" in command:
            response = ask_chatgpt(command)
            speak(response)

        elif "joke" in command:
            response = ask_chatgpt("Tell me a short joke")
            speak(response)

        elif "weather" in command:
            response = ask_chatgpt(f"What is the {command}")
            speak(response)

        elif "password" in command:
            response = ask_chatgpt("Generate a strong random password")
            speak(response)

        else:
            response = ask_chatgpt(command)
            speak(response)

# 🚀 Start the assistant
run_assistant()
