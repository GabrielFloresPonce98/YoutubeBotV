import random

from PIL import Image, ImageDraw, ImageFont,ImageFilter

class MakeYoutubeTitle:

    def __init__(self):
        self


    def human_format(self):
        s = random.randint(1, 13000000)
        magnitude = 0
        if s >= 1000:
            while abs(s) >= 1000:
                magnitude += 1
                s /= 1000.0
            return '{}{}'.format('{:f}'.format(s).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])
        else:
            return s

    def time_ago(self):
        time = ['day','month','year',"hour","minute"]

        c = random.choice(time)
        if c == "day":
            return  str(random.randint(1, 31)) + " day ago"
        elif c == "month":
            return str(random.randint(1, 12)) + " month ago"
        elif c == "year":
            return str(random.randint(1, 18)) + " yeat ago"
        elif c == "hour":
            return str(random.randint(1, 24)) + " hour ago"
        elif c == "minute":
            return str(random.randint(1, 60)) + " minute ago"

    def make_text_title_and_views(self,text,number,timeago):
        image = Image.open("resources/template/Template.png")
        draw  = ImageDraw.Draw(image)
        font = ImageFont.truetype("resources/fonts/youtube-sans-light.ttf",65)
        fontv = ImageFont.truetype("resources/fonts/youtube-sans-light.ttf", 40)
        draw.text((45,789),text,font=font,fill="white")
        textView = number + " views " + timeago
        draw.text((45, 869), textView, font=fontv, fill="grey")
        image.save("resources/template/TemplateCambiado.png")

    def merges_tamplate_image(self):
        s = random.randint(0,9)
        im1 = Image.open("resources/template/TemplateCambiado.png")
        im2 = Image.open("resources/images/00000"+str(s)+".jpg").resize((610,698))
        im1.paste(im2,(339,5))
        im1.save("resources/output/FinalResult.png",quality=95)
