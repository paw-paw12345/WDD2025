import pyttsx3

engine = pyttsx3.init()

name = input("Enter your name: ")
age = input("Enter your age: ")
hobby = input("Enter your favorite hobby: ")


text = "Hello, my name is {name}. I am {age} years old, and I love {hobby}."


print(text)

engine.say(text)
engine.runAndWait()
