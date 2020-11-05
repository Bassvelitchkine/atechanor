def emailScraper(url):
    """
    """
    import time
    import requests
    import re

    urlPortion = re.search('\d+', url)[0]

    res = requests.put('http://web:5005/update/' +
                       urlPortion + '/bob@gmail.com')

    return 'Job Result'
