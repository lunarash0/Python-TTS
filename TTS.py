import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', int(input("Please enter the wpm you would like me to speak at (150 is semi-slow): ")))
engine.setProperty('volume', float(input("Volume level (0.0 to 1.0): ")))

# yap ff alle voices available

voices = engine.getProperty('voices')

for i, voice in enumerate(voices):
    print(f"\033[92mVoice {i}: {voice.name}, {voice.gender}\033[0m")

sel_voice = int(input("Select a voice (#) : "))

while True:
    text = input("Text to speak (say exit to quit): ")
    if text.lower() == "exit":
        break
    engine.say(text)
    engine.runAndWait()