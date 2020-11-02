def emailScraper(url):
    """
    """
    import time
    import requests
    import re

    urlPortion = re.search("\d*", url).group(1)
    return urlPortion
    # res = requests.put('http://localhost:5000/update/' +
    #                    urlPortion + '/bob@gmail.com')
