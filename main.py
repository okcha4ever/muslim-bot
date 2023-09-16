import json
import requests
import random

from generate_other_fields import generate

book = random.choice(["bukhari", "muslim", "ibnmajah", "tirmidhi"])

url = f"https://random-hadith-generator.vercel.app/{book}/"

headers = {
    "Content-Type": "application/json",
}


def main():
    # Making the call
    print("in main()")
    response = requests.request("GET", url=url, headers=headers)

    # Saving the data key
    data = json.loads(response.text).get("data")
    # Getting the hadith_english key and removing "\n"
    hadith_english_list = data.get("hadith_english").split("\n")
    hadith_english = ""
    for i in hadith_english_list:
        hadith_english += i
    # print(f"hadith_english: {hadith_english}")

    # Same for the bookName key
    bookName = ""
    for i in data.get("bookName").split("\n")[1].split("\t"):
        if i == "":
            continue
        bookName = i

    # The hadith's number and book
    refno = data.get("refno")

    # Who narrated the hadith
    if book == "bukhari":
        header = data.get("header").split("\n")[1]
    else:
        header = data.get("header")

    generate(
        forwarder=header,
        hadith=hadith_english,
        refno=refno,
    )


if __name__ == "__main__" and __package__ is None:
    main()
    # import schedule
    # import time

    # schedule.every(1).minute.do(main)
    # # schedule.every(1).hour.do(main)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
