import json
import time
import requests
import re
from bs4 import BeautifulSoup


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

    urlPortion = re.search('\d+', url)[0]

    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    githubName = soup.find(href=githubLink)

    if githubName:
        githubPayload = parsePayload(
            "https://api.github.com/users/" + githubName.text + "/events/public")
        try:
            emails = findValueByKey(githubPayload, "email")
        except:
            emails = "No url found"
    else:
        emails = "No url found"

    res = requests.put('http://web:5005/update/' +
                       urlPortion + '/bob@gmail.com')

    print(emails)
    return {"emails": emails}
