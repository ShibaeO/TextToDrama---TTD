import json
from jsonpath_rw import parse
import pyttsx3
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
import unicodedata
import subprocess
from subprocess import DEVNULL
import time


def makeText(id, text):

    engine = pyttsx3.init()

    engine.setProperty("rate", 175)

    engine.setProperty("volume", 0.7)

    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)

    voices = engine.getProperty("voices")

    engine.save_to_file(f"{text}", f"content/{id}.mp3")
    engine.runAndWait()


def makeImage(id, author, text):

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
    # check_call(["ressources/ffmpeg", f"-i content/{image} -i content/{sound} -c:v libx264 -pix_fmt yuv420p -vf scale=1920:100 outpout/{id}.mp4"], stdout=DEVNULL, stderr=STDOUT)
    # os.system(f"ressources\\ffmpeg -i content/{image} -i content/{sound} -c:v libx264 -pix_fmt yuv420p -vf scale=1920:100 outpout/{id}.mp4")
    subprocess.run(f"ressources/ffmpeg -i content/{image} -i content/{sound} -c:v libx264 -pix_fmt yuv420p -vf scale=1920:100 outpout/{id}.mp4", stdout=DEVNULL, stderr=subprocess.STDOUT)
    # , stdout=DEVNULL, stderr=subprocess.STDOUT


def main():
    with open("msg.json", "rb") as f:
        a = json.load(f)
        jsonpath_expr = parse("$..isPinned")
        listId = [match.value for match in jsonpath_expr.find(a)]
        countr = 0
        for count in range(len(listId)):
            start_time = time.time()
            author = unicodedata.normalize("NFKD", a["messages"][count]["author"]["name"]).encode("ASCII", "ignore").decode("utf-8")
            content = unicodedata.normalize("NFKD", a["messages"][count]["content"]).encode("ASCII", "ignore").decode("utf-8")
            makeImage(count, author, content)
            makeText(count, f"{author} a dit : {content}")
            composeImgSound(count, f"{count}.png", f"{count}.mp3")
            end_time = time.time()
            execTime = end_time - start_time
            left = len(listId) - countr
            aa = time.strftime("%H:%M:%S", time.gmtime(int(float(execTime) * float(left))))
            os.system("cls")
            print(f"[+]    Finish : {count} | Left : {left} | Estimate time : {aa}")
            countr += 1


if __name__ == "__main__":
    main()
