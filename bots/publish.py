from instagrapi import Client
from .config import *
import sys, os

import requests

# BASE_DIR = sys.path[0]
# img_path = os.path.join(BASE_DIR, "./media/e_post.jpg")

# response = requests.post(
#     "https://api.telegram.org/6393439389:AAG-yzw7fENalufhUXFbdnEdPbWH3b-1bXA/sendPhoto?chat_id=-900186441",
#     img_path,
# )

# Setting up the client/bot account
# try:
#     cl = Client()
#     # cl.set_proxy("http://<aminedevs>:<okcha2009>@<50.17.126.77>:<80>")
#     cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
#     sendText = requests.post(
#         url=f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={'Login Success'}",
#     )


# except Exception as e:
#     sendText = requests.post(
#         url=f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={'Failed to login'}",
#     )


def upload_file(
    caption: str,
    hadith: str,
    refno: str,
    explained: str,
):
    print("uploading image")
    # Getting the base directory where the script resides in
    # And getting the generated image
    BASE_DIR = sys.path[0]
    img_path = os.path.join(BASE_DIR, "./media/e_post.jpg")

    files = {"photo": open("media\e_post.jpg", "rb")}

    sendFile = requests.post(
        url=f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto?chat_id={CHAT_ID}",
        files=files,
    )

    headers = {
        "content-type": "application/json",
    }
    listOfText = [caption, hadith, explained, refno]
    for text in listOfText:
        sendText = requests.post(
            url=f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}",
            headers=headers,
        )

    # Upload
    # try:
    #     media = cl.photo_upload(
    #         path=img_path,
    #         caption=f"{caption} \n\n Hadith: {hadith} \n\n Explained: {explained}",
    #     )

    # except Exception as e:
    #     print("Failed to upload: ", e)
