from moviepy.editor import *
import os
import time

clipList = []

a = os.listdir("outpout/")

countr = 0
for i in range(len(a)):
    start_time = time.time()
    clipList.append(VideoFileClip(f"outpout/{i}.mp4"))

    end_time = time.time()
    execTime = end_time - start_time
    left = len(a) - countr
    aa = time.strftime("%H:%M:%S", time.gmtime(int(float(execTime) * float(left))))
    os.system("cls")
    print(f"[+]    Finish : {i} | Left : {left} | Estimate time : {aa}")
    countr += 1

final = concatenate_videoclips(clipList)
final.write_videofile("final/final.mp4", fps=30, codec="libx264")

os.system("cls")
print("[+]    Clean Up !!")

for i in range(len(a)):
    os.remove(f"outpout/{i}.mp4")
    os.remove(f"content/{i}.mp3")
    os.remove(f"content/{i}.png")
