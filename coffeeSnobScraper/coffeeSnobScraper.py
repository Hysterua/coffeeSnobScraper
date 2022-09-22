import requests
from sendEmail import send_email
from bs4 import BeautifulSoup

URL = "https://coffeesnobs.com.au/forum/market-square/pay-it-forward"
page = requests.get(URL)

results = BeautifulSoup(page.content, "html.parser")
coffeeListing = results.find_all("a",class_="topic-title js-topic-title")

# opens a textfile that holds any previously saved listings so the code doesn't have to stay active
with open('coffeeText.txt', 'r+') as f:

    textHolder = f.read()

    # checks if the coffeeListing text is in the string 'textHolder'
    for c in coffeeListing:
        print(f"c is {c.text}")

        # if text isn't found sends an email to the user
        if c.text not in textHolder:
            print("New Listing Detected!")

            print("Sending Email...")
            send_email(c.text)
            print("Email Sent!")

            f.write(f"{c.text} \n")

        else:
            print("--- Already In List --- \n")
        