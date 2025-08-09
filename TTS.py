import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', int(input("Please enter the wpm you would like me to speak at (150 is semi-slow): ")))
engine.setProperty('volume', float(input("Volume level (0.0 to 1.0): ")))


while True:
    text = input("Text to speak (say exit to quit): ")
    if text.lower() == "exit":
        break
    engine.say(text)
    engine.runAndWait()