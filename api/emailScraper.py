import json
import time
import requests
from bs4 import BeautifulSoup
from random import random, randint


def aux(res, myjson, key):
    """
    """
    temp = []

    if type(myjson) is str:
        return res
    else:
        if type(myjson) is dict:
            for jsonkey in myjson.keys():
                if jsonkey == key:
                    temp += aux(res + [myjson[jsonkey]], myjson[jsonkey], key)
                else:
                    temp += aux(res, myjson[jsonkey], key)
        elif type(myjson) is list:
            for elem in myjson:
                temp += aux(res, elem, key)
        return temp


def findValueByKey(myjson, key):
    temp = aux([], myjson, key)
    return list(set(temp))


def parsePayload(url):
    return requests.get(url).json()


def githubLink(href):
    return href and "github.com" in href


def emailScraper(url):
    """
    """

    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    githubName = soup.find(href=githubLink)
    emails = []

    if githubName:
        githubPayload = parsePayload(
            "https://api.github.com/users/" + githubName.text + "/events/public")

        try:
            emails = findValueByKey(githubPayload, "email")
        except:
            None

    res = requests.put('http://web:5005/update',
                       json={"profileUrl": url, "emails": emails})

    # 10% chance to wait for 10 minutes before moving on to the next job
    randomFloat = random()
    if randomFloat > 0.9:
        time.sleep(600)
    else:
        time.sleep(randint(20, 40))

    return "OK"
