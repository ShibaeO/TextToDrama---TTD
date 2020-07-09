def composeImgSound(id, image, sound):
    import os

    os.system(f"ressources\\ffmpeg -i content/{image} -i content/{sound} -c:v libx264 -pix_fmt yuv420p -vf scale=1280:100 outpout/{id}.mp4")
    # os.system(f"ffmpeg -loop 1 -i {inpath} -i {inpath3} -c:v libx264 -t {duration} -pix_fmt yuv420p -vf scale=1280:100 {outpath}.mp4")
