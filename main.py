import json
from jsonpath_rw import parse


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


def makeImage(id, author, text):
    from PIL import Image, ImageDraw, ImageFont
    import textwrap

    a = textwrap.wrap(text, width=195)
    text = "".join(f"{a[i]}\n" for i in range(len(a)))

    li = 65
    for lineHeigh in range(len(a)):
        li += 20

    img = Image.new("RGB", (1920, li), color=(32, 34, 37))
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("ressources/Whitney.ttf", 20)

    d.text((20, 10), f"{author}", font=fnt, fill=(41, 128, 185))
    d.text((20, 40), f"{text}", font=fnt, fill=(236, 240, 241))

    img.save(f"content/{id}.png")


def composeImgSound(id, image, sound):
    import os

    os.system(f"ressources\\ffmpeg -i content/{image} -i content/{sound} -c:v libx264 -pix_fmt yuv420p -vf scale=1920:100 outpout/{id}.mp4")


def main():
    with open("msg.json", "r", encoding="utf-8") as f:
        a = json.load(f)
        jsonpath_expr = parse("$..id")
        listId = [match.value for match in jsonpath_expr.find(a)]
        print(len(listId))
        count = 0
        for count in range(len(listId)):
            author = a["messages"][count]["author"]["name"].encode("cp850", "replace").decode("cp850")
            content = a["messages"][count]["content"].encode("cp850", "replace").decode("cp850")
            makeImage(count, author, content)
            makeText(count, f"{author} a dit : {content}")
            composeImgSound(count, f"{count}.png", f"{count}.mp3")
            count += 1


if __name__ == "__main__":
    main()
