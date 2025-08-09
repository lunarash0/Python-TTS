import sys, os, pyttsx3

# pick stinky driver
if sys.platform == "darwin":
    DRIVER = "nsss"
elif os.name == "nt":
    DRIVER = "sapi5"
else:
    DRIVER = "espeak"

rate = int(input("WPM (150 is semi-slow): ") or 150)
vol  = float(input("Volume 0.0–1.0: ") or 1.0)

# begin ai
tmp_engine = pyttsx3.init(DRIVER)
# end ai
voices = tmp_engine.getProperty('voices')
for i, v in enumerate(voices):
    print(f"{i}: {v.name}")
sel = int(input("Select voice #: "))
voice_id = voices[sel].id
# begin ai
tmp_engine.stop(); del tmp_engine
# end ai

print("Type text (exit to quit):")
while True:
    for i in range(30):
        print(" ")
    text = input("> ").strip()
    if text.lower() == "exit":
        break
    if not text:
        continue

    engine = pyttsx3.init(DRIVER)
    engine.setProperty('rate', rate)
    engine.setProperty('volume', vol)
    engine.setProperty('voice', voice_id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    del engine