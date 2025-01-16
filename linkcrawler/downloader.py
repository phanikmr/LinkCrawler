import requests

class Downloader(object):
    def __init__(self, **kwargs):
        super().__init__()
        self.verify = kwargs.get('verify', True)

    def getContent(self, link):
        return requests.get(link, verify=self.verify)

# new set of lines to test