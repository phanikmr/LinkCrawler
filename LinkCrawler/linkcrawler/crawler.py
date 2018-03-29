from downloader import Downloader
from spider import Spider
from link import Link
from queue import Queue
import sys
import os

clear = None
if sys.platform == 'win32':
    clear = lambda : os.system('cls')
else:
    clear = lambda : os.system('clear')
del sys

class Crawler(object):
    """description of class"""

    lookup = None
    q = None
    feed = None

    def __init__(self, **kwargs):
        super(Crawler, self).__init__()
        self.downloader = Downloader()
        self.parser = Spider()
        self.lookup = {}
        self.q = Queue()
        self.feed = kwargs.get('feed_link', None)


    def crawl(self, link=feed):
        if len(self.lookup) == 0:
            self.lookup[link] = Link()
            self.q.put(link)
        while not self.q.empty():
            link = self.q.get()
            if not self.lookup[link].crawled:
                self.__get_links(link)

    def __get_links(self,link):
        try:
            response = self.downloader.getContent(link)
            if response.status_code == 200:
                self.lookup[link].crawled = True               
                links = self.parser.parseLinks(response.text)
                self.lookup[link].extracted_links_count = len(links)                           
                for link in links:
                    self.q.put(link)
                    if not link in self.lookup:
                        self.lookup[link] = Link()
                clear()
                for pair in self.lookup:
                    print(pair)
                    print(self.lookup[pair].crawled, self.lookup[pair].res_code, self.lookup[pair].attempts, self.lookup[pair].extracted_links_count)
            else:
                self.lookup[link].res_code = response.status_code
                self.lookup[link].attempts += 1 
                self.q.put(link)            
        except err:
            print(err)
            self.q.put(link)