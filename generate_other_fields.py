import json
import requests

# my files
# import translate_to_ar
from draw import draw_image


def generate(forwarder, hadith, refno):
    url = "https://api.textcortex.com/v1/texts/completions"

    headers = {
        "content-type": "application/json",
        "authorization": "bearer gAAAAABlBJZIWTvwqlGvLvznGNq8_9mbxC7p77XnvLGh4s4_0kwtURKkJMR9x5A4-tDpWA2brNu-7t2g7MQTsaNmv3S5tNGvTnQ_CjC51TVlixgHoAlSY7AsnW3MrX_bWc5IBVVwPH3I",
    }
    print("in generate()")
    # old prompt
    # "text": "give me a hadith in islam without any extra talk and send it as json object with the following keys: forwarder (the text of the one who forwarded/delivered the hadith. example: forwarder: 'the prophet (peace be upon him) said'), hadith (the actual hadith without the forwarder), explained (explaination of the hadith), caption (a nice caption about the hadith for an instagram post that talks about it). do not give me anything you gave me before.",
    payload = {
        "max_tokens": 512,
        "model": "chat-sophos-1",
        "n": 1,
        "source_lang": "en",
        "target_lang": "en",
        "temperature": 0.55,
        "text": f"given this following islamic hadith: '{hadith}' \n explain it in simplified and short terms, and return the explanation as a json object with the following keys: 'explained' - 'the explanation of the islamic hadith', 'caption' - 'a nice and good caption for an instagram post about this islamic hadith with hashtags.'",
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    data = json.loads(response.text).get("data")
    text = data.get("outputs")[0].get("text")
    explained = json.loads(text).get("explained")
    caption = json.loads(text).get("caption")

    # explained = "This Islamic hadith states that if the rulers of Persia or Rome are destroyed, their empires will not be replaced. It also encourages spending their treasures in the cause of Allah."
    # caption = "The fall of empires is inevitable, but what will remain is the good we do in the name of Allah. #Islam #Hadith #Empires #AllahsCause"

    # Hard coded
    draw_image(
        forwarder.replace("ﷺ", "p.b.u.h"),
        hadith.replace("ﷺ", "p.b.u.h"),
        explained.replace("ﷺ", "p.b.u.h"),
        caption.replace("ﷺ", "p.b.u.h"),
        refno=refno,
    )
