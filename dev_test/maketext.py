def makeText(id, text):
    import pyttsx3

    engine = pyttsx3.init()

    engine.setProperty("rate", 175)

    engine.setProperty("volume", 0.7)

    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)

    voices = engine.getProperty("voices")

    engine.save_to_file(f"{text}", f"content/{id}.mp3")
    engine.runAndWait()


mytext = "MastocGame a dit : @Nitrox.mp4 je pense sincèrement que vos provocations envers la modération, nous pouvons très largement nous en passer. Si vous n'êtes pas content du fonctionnement de la modération, ou si vous estimez, selon vos paroles, que la mentialité du staff est enfantine, pourquoi ne pas réaliser une candidature ? Vous vous rendrez sûrement compte du contraire."
makeText("1", mytext)
