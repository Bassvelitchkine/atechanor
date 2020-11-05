def emailScraper(url):
    """
    """
    import time
    import requests
    import re
    from bs4 import BeautifulSoup

    urlPortion = re.search('\d+', url)[0]

    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    title = soup.title.text

    res = requests.put('http://web:5005/update/' +
                       urlPortion + '/bob@gmail.com')

    return title
