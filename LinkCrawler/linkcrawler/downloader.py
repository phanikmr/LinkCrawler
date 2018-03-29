import requests

class Downloader(object):
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    def getContent(self, link):
        return requests.get(link, verify=False)