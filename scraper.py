# I used this to scrape the bible text files.

import requests
from bs4 import BeautifulSoup

BIBLE_URL = "http://stewartonbibleschool.org/bible/text"
bible = requests.get(BIBLE_URL)
soup = BeautifulSoup(bible.text, features="lxml")


def download_verse(filename: str):
    full_url = BIBLE_URL + f"/{filename}"
    response = requests.get(full_url)
    open("bible/" + filename, "wb").write(response.content)


for a_tag in soup.find_all("a"):
    if not a_tag.attrs["href"].endswith(".txt"):
        continue

    download_verse(a_tag.attrs["href"])
