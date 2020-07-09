def makeImage(id, author, text):
    from PIL import Image, ImageDraw, ImageFont
    import textwrap

    a = textwrap.wrap(text, width=195)
    text = "".join(f"{a[i]}\n" for i in range(len(a)))

    li = 55
    for lineHeigh in range(len(a)):
        li += 20

    img = Image.new("RGB", (1280, li), color=(32, 34, 37))
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("ressources/Whitney.ttf", 15)

    d.text((10, 10), f"{author}", font=fnt, fill=(41, 128, 185))
    d.text((10, 40), f"{text}", font=fnt, fill=(236, 240, 241))

    img.save(f"content/{id}.png")


author = "MastocGame"
text = "MastocGame a dit : @Nitrox.mp4 je pense sincèrement que vos provocations envers la modération, nous pouvons très largement nous en passer. Si vous n'êtes pas content du fonctionnement de la modération, ou si vous estimez, selon vos paroles, que la mentialité du staff est enfantine, pourquoi ne pas réaliser une candidature ? Vous vous rendrez sûrement compte du contraire."
makeImage("1", author, text)
