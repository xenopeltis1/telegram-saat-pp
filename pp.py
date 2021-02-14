from pyrogram import Client
from PIL import Image, ImageDraw, ImageFont
import time
import datetime


def createProfilePhoto(time):
    img = Image.new('RGB', (1000, 1000), color = (73, 109, 137))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 200)
    d.text((200, 400), time, fill=(255, 255, 0), font=font)
    
    img.save("profilePhoto.png")


config = open(r"config.json", "r")
config = json.loads(config.read())

app = Client(
    session_name="0x1D",
    api_id=config["api_id"],
    api_hash=config["api_hash"]
    )

def getTime():
    time = datetime.datetime.now()
    print(str(time.hour) + " : " + str(time.minute))
    return str(time.hour) + " : " + str(time.minute)


def changePp():
    createProfilePhoto(getTime())
    for i in app.get_profile_photos("me"):
        app.delete_profile_photos(i.file_id)

    app.set_profile_photo(photo="profilePhoto.png")


with app:
    while True:
        changePp()
        time.sleep(60)

app.run()
