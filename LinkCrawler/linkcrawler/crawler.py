from downloader import Downloader
from spider import Spider
from queue import Queue


class Crawler(object):
    """description of class"""

    lookup = None
    q = None

    def __init__(self, **kwargs):
        super(Crawler, self).__init__()
        self.downloader = Downloader()
        self.parser = Spider()
        self.lookup = {}
        self.q = Queue()


    def crawl(self, link):
        if len(self.lookup) == 0:
            self.lookup[link] = False
            self.q.put(link)
            print(link)
        while not self.q.empty():
            link = self.q.get()
            if not self.lookup[link]:
                self.get_links(link)

    def get_links(self,link):
        response = self.downloader.getContent(link)
        if response.status_code == 200:
            self.lookup[link] = True
        else:
            pass
        for link in self.parser.parseLinks(response.text):
            self.q.put(link)
            if not link in self.lookup:
                self.lookup[link] = False
                print(self.q.qsize())