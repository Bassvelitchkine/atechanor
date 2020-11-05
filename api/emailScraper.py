import json


def githubLink(href):
    return href and "github.com" in href


def findValueByKey(myjson, key):
    if type(myjson) is dict:
        for jsonkey in myjson:
            if type(myjson[jsonkey]) in (list, dict):
                findValueByKey(myjson[jsonkey], key)
            elif jsonkey == key:
                yield myjson[jsonkey]
    elif type(myjson) is list:
        for item in myjson:
            if type(item) in (list, dict):
                findValueByKey(item, key)


def emailScraper(url):
    """
    """
    import time
    import requests
    import re
    from bs4 import BeautifulSoup

    urlPortion = re.search('\d+', url)[0]

    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    githubName = soup.find(href=githubLink)

    if githubName:
        githubPayload = requests.get(
            "https://api.github.com/users/" + githubName.text + "/events/public").json()
        try:
            emails = [email for email in findValueByKey(
                githubPayload, "email")]
        except:
            emails = "No url found"
    else:
        emails = "No url found"

    res = requests.put('http://web:5005/update/' +
                       urlPortion + '/bob@gmail.com')

    print(emails)
    return {"emails": emails}
