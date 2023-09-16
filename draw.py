from PIL import Image, ImageFont, ImageDraw
import os
import arabic_reshaper
from bidi.algorithm import get_display
import textwrap
from bots.publish import upload_file


# -- reshape arabic letters
# reshaped = arabic_reshaper.reshape("الله أكبر")
# text = get_display(reshaped)


# Draw the text on image
def draw_image(forwarder: str, hadith: str, explained: str, caption: str, refno: str):
    print("in draw_image()")
    # Set width and height of the image
    W, H = 1080, 1080
    show_explained = True

    print("Drawing text on image")

    img = Image.new("RGBA", (W, H), "white")

    # CAIRO = ImageFont.truetype("media/fonts/Cairo-Black.ttf", size=60)
    ROBOTO = ImageFont.truetype("media/fonts/Roboto-Black.ttf", size=40)

    e_img = ImageDraw.Draw(img)

    offset = 105
    forwarder_wraped = textwrap.wrap(forwarder, width=52)

    for line in range(len(forwarder_wraped)):
        if forwarder_wraped[line] != "null" or forwarder != "null":
            e_img.text(
                (50, offset + line * 70),
                forwarder_wraped[line],
                font=ROBOTO,
                fill="red",
            )

    hadith_wraped = textwrap.wrap(hadith, width=52)
    if len(hadith_wraped) >= 7:
        show_explained = False

    if len(hadith_wraped) >= 11:
        show_explained = False
        hadith_wraped = hadith_wraped[:10]
        hadith_wraped.append("Continued in caption...")

    for line in range(len(hadith_wraped)):
        if len(forwarder_wraped) >= 2:
            e_img.text(
                (50, offset + 370 + line * 70),
                hadith_wraped[line],
                font=ROBOTO,
                fill="black",
            )

            return

        if hadith_wraped[line].lower() == "continued in caption...":
            e_img.text(
                (50, offset + 110 + line * 70),
                hadith_wraped[line],
                font=ROBOTO,
                fill="#2596be",
            )
            return

        e_img.text(
            (50, offset + 70 + line * 70),
            hadith_wraped[line],
            font=ROBOTO,
            fill="black",
        )

    explained_wraped = textwrap.wrap(explained, width=49)
    if show_explained and len(explained_wraped) <= 5:
        for line in range(len(explained_wraped)):
            e_img.text(
                (50, offset + 300 + len(hadith_wraped) * 50 + line * 70),
                explained_wraped[line],
                font=ROBOTO,
                fill="gray",
            )

    if show_explained == False:
        e_img.text(
            (50, offset + 300 + len(hadith_wraped) * 50 + line * 70),
            "Explanation below...",
            font=ROBOTO,
            fill="gray",
        )

    # if 0 < len(explained_wraped) < 5:
    e_img.text((50, H - 100), refno, font=ROBOTO, fill="black")

    try:
        jpeg_img = img.convert("RGB")
        jpeg_img.save("media/e_post.jpg")

    except Exception as e:
        print("something went wrong")

    # Upload after generating image

    upload_file(
        caption=caption,
        hadith=hadith,
        explained=explained,
        refno=refno,
    )
