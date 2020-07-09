from moviepy.editor import *
import os
import time

clipList = []

a = os.listdir("outpout/")

for i in a:
    print(i)
    clipList.append(VideoFileClip(f"outpout/{i}"))

print(clipList)
final = concatenate_videoclips(clipList)
final.write_videofile("final/final.mp4", fps=30, codec="libx264")
