def emailScraper(url):
    """
    """
    import time
    import requests
    import re

    urlPortion = re.search('\d+', url)[0]

    res = requests.put('http://192.168.99.100:5000/update/' +
                       urlPortion + '/bob@gmail.com')

    return 'Job Result'
